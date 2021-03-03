from multiprocessing import Pool
import logging;
import time
def f(x):
    return x*x
def test(p):
        print(p)
        time.sleep(1)
def test2(p):
    print('2');

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    # test 1
    # for Pool().map来说，其实就是相当于 pool.apply_async， 只不过apply_async参数一个一个输入， in map, we can input by list.
    # for pool.map, return is the list of test return, and all the thread in pool can run immediately.
    logging.info("test1")
    with Pool(3) as p:
        print(p.map(test, [1, 2, 3,4,5,6,7]));
        print('test')
    # test 2
    # async means I don't block the main threading.
    logging.info("test2")
    with Pool(3) as p:
        print(p.map_async(test, [1, 2, 3,4,5,6,7]));
        print('test')
        p.close();
        p.join();

    # test 3
    # 如果要完美的实现pool的功能，就要用apply_async();
    logging.info("test3")
    pool = Pool(processes=4)
    for i in range(10):
        pool.apply(test, args=(i,))  # 维持执行的进程总数为10，当一个进程执行完后启动一个新进程.
        # pool.apply(test2, args=(i,))  # 维持执行的进程总数为10，当一个进程执行完后启动一个新进程.
    print('test')
    # pool.close()
    # pool.join()

    # test 4
    logging.info("test4")
    pool = Pool(processes=4)
    for i in range(10):
        pool.apply_async(test, args=(i,))  # 维持执行的进程总数为10，当一个进程执行完后启动一个新进程.

    print('test')
    pool.close()
    pool.join()

    # test 5
    logging.info("test5")
    with Pool(processes=4) as pool:         # start 4 worker processes
        result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
        print(result.get(timeout=1))        # prints "100" unless your computer is *very* slow

        print(pool.map(f, range(10)))       # prints "[0, 1, 4,..., 81]"

        it = pool.imap(f, range(10))
        print(next(it))                     # prints "0"
        print(next(it))                     # prints "1"
        print(it.next(timeout=1))           # prints "4" unless your computer is *very* slow
        result = pool.apply_async(time.sleep, (0.1,))
        print(result.get(timeout=1))        # raises multiprocessing.TimeoutError if time sleep is large
        # return none because time.sleep don't return value; 


# summary
# apply_async == map_async, it doesn't block the main thread, and apply_async return the function return value
# map it block the main thread, but the thread inside can work in parallel, and map return the list of function return value
# apply it block the main thread, and the thread inside work one by one. so it like doesn't have a pool

# close(); 防止任何更多的任务被提交到池中。 一旦完成所有任务，工作进程将退出
# terminate() 立即停止工作进程而不完成未完成的工作。当池对象被垃圾收集时，terminate()将立即调用。
# join() 等待工作进程退出。必须打电话close()或 terminate()使用之前join()。

