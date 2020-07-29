## asyncio

asyncio 是用来编写 并发 代码的库，使用 async/await 语法。asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。

* 并发是指一次处理多件事。并行是指一次做多件事。本章介绍 asyncio 包，这个包使用事件循环驱动的协程实现并发。这是 Python 中最大也是最具雄心壮志的库之一。asyncio 大量使用 yield from 表达式，yield from在asyncio模块中得以发扬光大。


* asyncio 包使用的“协程”是较严格的定义。适合 asyncio API 的协程在定义体中必须使用 yield from ，而不能使用 yield 。此外，适合 asyncio 的协程要由调用方驱动，并由调用方通过 yield from 调用；或者把协程传给 asyncio 包中的某个函数，例如 asyncio.async。


备注：除非想阻塞主线程，从而冻结事件循环或整个应用，否则不要在 asyncio 协程中使用 time.sleep(...) 。如果协程需要在一段时间内什么也不做，应该使用 yield from asyncio.sleep(DELAY) 。使用 @asyncio.coroutine 装饰器不是强制要求，但是强烈建议这么做，因为这样能在一众普通的函数中把协程凸显出来，也有助于调试。

* 无锁的协程：对协程来说，无需保留锁，在多个线程之间同步操作，协程自身就会同步，因为在任意时刻只有一个协程运行。

* 使用指南：在 asyncio 包中，BaseEventLoop.create_task(...) 方法接收一个协程，排定它的运行时间，然后返回一个 asyncio.Task 实例——也是 asyncio.Future 类的实例，因为 Task 是 Future 的子类，用于包装协程。这与调用 Executor.submit(...) 方法创建 concurrent.futures.Future 实例是一个道理。asyncio.Future 类的 .result() 方法没有参数，因此不能指定超时时间。

## 异步框架基础

* 任何一个协程框架都首先必须是一个异步框架，一个异步框架通常主要包括事件循环【核心】、事件队列【可以执行的队列和未来需要执行的队列】、polling【监控socket活动】、timer队列保存定时器。
    * asyncio的事件队列里面就是普通的callable，每个callable都是一小份工作，当这部分工作做完之后，会等待下一个条件：如果要等socket，就设置polling回调。如果要等超时时间，就设置timer，timer也有回调【延迟执行】，回调是一个基础。
    
    * 事件循环：事件循环是一个死循环，事件循环（也就是所谓EventLoop）开始的时候，会不断从事件队列里取callable，然后一个一个call过去，call完换下一个，当时间满足的时候也会调用这个callable。遇到socket就设置是一个异步并yield配合select调用和回调来完成。
    ```
    协程不知道自己的IO好了没有，协程把自己使用的文件（socket）注册到事件循环里，事件循环负责监测IO好了没有，
    同时协程负责在IO上增加一个小的回调在IO完成的时候把自己唤醒放到队列里等待执行。
    ```
    


## 避免阻塞型调用

## 相关阅读

http://www.dabeaz.com/coroutines/index.html

https://www.zhihu.com/question/294188439/answer/555273313