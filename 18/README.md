## asyncio

asyncio 是用来编写 并发 代码的库，使用 async/await 语法。asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。

* 并发是指一次处理多件事。并行是指一次做多件事。本章介绍 asyncio 包，这个包使用事件循环驱动的协程实现并发。这是 Python 中最大也是最具雄心壮志的库之一。asyncio 大量使用 yield from 表达式，yield from在asyncio模块中得以发扬光大。


* asyncio 包使用的“协程”是较严格的定义。适合 asyncio API 的协程在定义体中必须使用 yield from ，而不能使用 yield 。此外，适合 asyncio 的协程要由调用方驱动，并由调用方通过 yield from 调用；或者把协程传给 asyncio 包中的某个函数，例如 asyncio.async。


备注：除非想阻塞主线程，从而冻结事件循环或整个应用，否则不要在 asyncio 协程中使用 time.sleep(...) 。如果协程需要在一段时间内什么也不做，应该使用 yield from asyncio.sleep(DELAY) 。使用 @asyncio.coroutine 装饰器不是强制要求，但是强烈建议这么做，因为这样能在一众普通的函数中把协程凸显出来，也有助于调试。

* 无锁的协程：对协程来说，无需保留锁，在多个线程之间同步操作，协程自身就会同步，因为在任意时刻只有一个协程运行。

* 使用指南：在 asyncio 包中，BaseEventLoop.create_task(...) 方法接收一个协程，排定它的运行时间，然后返回一个 asyncio.Task 实例——也是 asyncio.Future 类的实例，因为 Task 是 Future 的子类，用于包装协程。这与调用 Executor.submit(...) 方法创建 concurrent.futures.Future 实例是一个道理。asyncio.Future 类的 .result() 方法没有参数，因此不能指定超时时间。

## async/await语法

* async关键字：协程的另一种声明方式：函数前面加上 async 关键字，这个函数对象是一个协程，通过isinstance函数，它确实是Coroutine类型，相比之前@asyncio.coroutine装饰器，这是一个更新的语法，Python3.5 对这两种调用协程的方法都提供了支持。
    ```
    @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
    ```

* async不能脱离事件循环：推荐 async/await 作为首选。调用他们中的任意一个，实际上并未立即运行，而是返回一个协程对象，然后将其传递到 Eventloop 中，之后再执行【await隐式地将协程加入到EventLoop中并yield】。async 定义的方法就会变成一个无法直接执行的 coroutine 对象，必须将其注册到事件循环中才可以执行。

* 从yield from 到 async/await：要使用新的语法，只需要做两步简单的替换：
    * 把@asyncio.coroutine替换为async。
    * 把yield from替换为await。 
    
* 使用：如果要判断一个函数是不是协程， asyncio 提供了 asyncio.iscoroutinefunction(func) 方法，如果要判断一个函数返回的是不是协程对象，则可以使用 asyncio.iscoroutine(obj)。用 asyncio 提供的 @asyncio.coroutine 可以把一个 generator 标记为 coroutine 类型，然后在 coroutine 内部用 yield from 调用另一个 coroutine 实现异步操作。
    ```
    标记了@asyncio.coroutine装饰器的函数称为协程函数，iscoroutinefunction()方法返回True调用协程函数返回的对象称为协程对象，iscoroutine()函数返回True
    ```
    


## 异步框架基础

* 任何一个协程框架都首先必须是一个异步框架，一个异步框架通常主要包括事件循环【核心】、事件队列【可以执行的队列和未来需要执行的队列】、polling【监控socket活动】、timer队列保存定时器。
    * asyncio的事件队列里面就是普通的callable，每个callable都是一小份工作，当这部分工作做完之后，会等待下一个条件：如果要等socket，就设置polling回调。如果要等超时时间，就设置timer，timer也有回调【延迟执行】，回调是一个基础。
    
    * 事件循环：事件循环是一个死循环，事件循环（也就是所谓EventLoop）开始的时候，会不断从事件队列里取callable，然后一个一个call过去，call完换下一个，当时间满足的时候也会调用这个callable。遇到socket就设置是一个异步并yield配合select调用和回调来完成。
    ```
    协程不知道自己的IO好了没有，协程把自己使用的文件（socket）注册到事件循环里，事件循环负责监测IO好了没有，
    同时协程负责在IO上增加一个小的回调在IO完成的时候把自己唤醒放到队列里等待执行。
    ```
    


## 避免阻塞型调用

把每个阻塞型操作转换成非阻塞的异步调用使用，为了降低内存的消耗，通常使用回调来实现异步调用。这是一种低层概念，类似于所有并发机制中最古老、最原始的那种——硬件中断。使用回调时，我们不等待响应，而是注册一个函数，在发生某件事时调用。这样，所有调用都是非阻塞的。
```
把生成器当作协程使用是异步编程的另一种方式。对事件循环来说，调用回调与在暂停的协程上调用 .send() 方法效果差不多【其实回调函数就是调用send】。各个暂停的协程是要消耗内存，但是比线程消耗的内存数量级小。
```

## 协程API

* Task:asyncio.create_task() 函数用来并发运行作为 asyncio 任务的多个协程。任务被用来设置日程以便 并发执行协程。

* 可等待对象:如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象。许多 asyncio API 都被设计为接受可等待对象。可等待 对象有三种主要类型: 协程, 任务 和 Future。

* Future:Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的最终结果。当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕，可以设置回调函数。

    ```
    协程函数: 定义形式为 async def 的函数;协程对象: 调用 协程函数 所返回的对象。
    ```


## 总结

在应用中，我们只需确保没有阻塞的代码，事件循环会在背后处理并发。异步系统能避免用户级线程的开销，这是它能比多线程系统管理更多并发连接的主要原因。此外，收集 asyncio 资源的还有 Asyncio.org 网站（http://asyncio.org/ ）和 GitHub 中的 aio-libs 组织（https://github.com/aio-libs ），在这两个网站中能找到 PostgreSQL、MySQL 和多种 NoSQL 数据库的异步驱动。


## 相关阅读

http://www.dabeaz.com/coroutines/index.html

https://www.zhihu.com/question/294188439/answer/555273313

https://blog.csdn.net/SL_World/article/details/86597738