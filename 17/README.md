## 使用future处理并发

* future一种对象，表示异步执行的操作。这个概念的作用很大，是 concurrent.futures 模块和 asyncio 包（第 18 章讨论）的基础。

* 为了高效处理网络 I/O，需要使用并发，因为网络有很高的延迟，所以为了不浪费 CPU 周期去等待，最好在收到网络响应之前做些其他的事。

* concurrent.futures 模块的主要特色是 ThreadPoolExecutor 和 ProcessPoolExecutor 类，这两个类实现的接口能分别在不同的线程或进程中执行可调用对象。

## 谈谈future

* 从 Python 3.4 起，标准库中有两个名为 Future 的类：concurrent.futures.Future 和 asyncio.Future 。这两个类的作用相同：两个 Future 类的实例都表示可能已经完成或者尚未完成的延迟计算。future(期物)封装待完成的操作，可以放入队列，完成的状态可以查询，得到结果（或抛出异常）后可以获取结果（或异常）。

    ```
    通常情况下自己不应该创建期物，而只能由并发框架（concurrent.futures 或 asyncio ）实例化。
    ```

* 两种期物都有 .done() 方法，这个方法不阻塞，返回值是布尔值，指明期物链接的可调用对象是否已经执行。客户端代码通常不会询问期物是否运行结束，而是会等待通知。因此，两个 Future 类都有 .add_done_callback() 方法：这个方法只有一个参数，类型是可调用的对象，期物运行结束后会调用指定的可调用对象。还有 .result() 方法。在期物运行结束后调用的话，这个方法在两个 Future 类中的作用相同：返回可调用对象的结果，或者重新抛出执行可调用的对象时抛出的异常。可是，如果期物没有运行结束，result 方法在两个 Future 类中的行为相差很大。

* Future 表示终将发生的事情，而确定某件事情会发生的唯一方式是执行的时间已经排定。因此只有把某件事交给 concurrent.futures.Executor 子类处理时，才会创建 concurrent.futures.Future 实例。
    
    ```
    调用Executor.submit() 方法的参数是一个可调用的对象，调用这个方法后会为传入的可调用对象排期，并返回一个Future。
    ```
    
## GIL（Global Interpreter Lock）和阻塞型I/O
    
* CPython 解释器本身就不是线程安全的，因此有全局解释器锁（GIL），一次只允许使用一个线程执行 Python 字节码。因此，一个 Python 进程通常不能同时使用多个 CPU 核心。这是 CPython 解释器的局限，与 Python 语言本身无关。Jython 和 IronPython 没有这种限制。不过，目前最快的 Python 解释器 PyPy 也有 GIL。

* 标准库中所有执行阻塞型 I/O 操作的函数，在等待操作系统返回结果时都会释放 GIL。这意味着在 Python 语言这个层次上可以使用多线程，而 I/O 密集型 Python 程序能从中受益：一个 Python 线程等待网络响应时，阻塞型 I/O 函数会释放 GIL，再运行一个线程。Python 标准库中所有阻塞型I/O函数都会释放GIL，允许其他线程运行。time.sleep()函数也会释放GIL。
    ```
    python的多线程对I/O密集型应用十分友好，会自动释放GIL，切换另一个线程
    ```

* 编写 Python 代码时无法控制 GIL；不过，执行耗时的任务时，可以使用一个内置的函数或一个使用 C 语言编写的扩展释放 GIL。其实，有个使用 C 语言编写的 Python 库能管理 GIL。

## 真正的并行进程级别

* 使用 ProcessPoolExecutor 类，使用这个模块可以在做CPU密集型工作是绕开GIL，利用所有可用核心。ThreadPoolExecutor 和 ProcessPoolExecutor都实现了通用的 Executor 接口，所以，我们可以轻松的将基于线程的方案改为使用进程的方案。ProcessPoolExecutor 的价值体现在 CPU 密集型作业上，I/O密集型作用意义不是很大，不如使用多线程。在 ProcessPoolExecutor 类中，那个参数是可选的，而且大多数情况下不使用——默认值是 os.cpu_count() 函数返回的 CPU 数量。这样处理说得通，因为对 CPU 密集型的处理来说，不可能要求使用超过 CPU 数量的职程。
    ```
    如果使用 Python 处理 CPU 密集型工作，应该试试 PyPy（http://pypy.org ）。使用 PyPy 运行 arcfour_futures.py 脚本，速度快了 3.8~5.1 倍
    ```

* 对简单的程序来说，可以用 multiprocessing 模块代替 threading 模块，少量改动即可。不过，multiprocessing 模块还能解决协作进程遇到的最大挑战：在进程之间传递数据。multiprocessing 支持进程之间的两种通信通道，分别是管道和队列。


## 延伸阅读

PEP 3148—futures —execute computations asynchronously”（https://www.python.org/dev/peps/pep-3148/ ）。在这个 PEP 中，Quinlan 写道，concurrent.futures 库“受 Java 的 java.util.concurrent 包影响很大”。Jan Palach 写的 Parallel Programming with Python （Packt 出版社）一书介绍了几个并发编程的工具，包括 concurrent.futures 、threading 和 multiprocessing 库。除了标准库之外，这本书还讨论了 Celery（http://celery.readthedocs.org/en/latest/getting-started/introduction.html ）。这是一个任务队列，用于把工作分配给多个线程和进程，甚至是不同的设备。