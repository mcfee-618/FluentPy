## asyncio

* 并发是指一次处理多件事。并行是指一次做多件事。本章介绍 asyncio 包，这个包使用事件循环驱动的协程实现并发。这是 Python 中最大也是最具雄心壮志的库之一。asyncio 大量使用 yield from 表达式，yield from在asyncio模块中得以发扬光大。


* asyncio 包使用的“协程”是较严格的定义。适合 asyncio API 的协程在定义体中必须使用 yield from ，而不能使用 yield 。此外，适合 asyncio 的协程要由调用方驱动，并由调用方通过 yield from 调用；或者把协程传给 asyncio 包中的某个函数，例如 asyncio.async。


备注：除非想阻塞主线程，从而冻结事件循环或整个应用，否则不要在 asyncio 协程中使用 time.sleep(...) 。如果协程需要在一段时间内什么也不做，应该使用 yield from asyncio.sleep(DELAY) 。使用 @asyncio.coroutine 装饰器不是强制要求，但是强烈建议这么做，因为这样能在一众普通的函数中把协程凸显出来，也有助于调试。

* 无锁的协程：对协程来说，无需保留锁，在多个线程之间同步操作，协程自身就会同步，因为在任意时刻只有一个协程运行。

* 使用指南：在 asyncio 包中，BaseEventLoop.create_task(...) 方法接收一个协程，排定它的运行时间，然后返回一个 asyncio.Task 实例——也是 asyncio.Future 类的实例，因为 Task 是 Future 的子类，用于包装协程。这与调用 Executor.submit(...) 方法创建 concurrent.futures.Future 实例是一个道理。asyncio.Future 类的 .result() 方法没有参数，因此不能指定超时时间。


## 相关阅读

http://www.dabeaz.com/coroutines/index.html