from concurrent.futures import ProcessPoolExecutor       # 进程池
import multiprocessing

# 多进程编程
import time

def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n

class MyProcess(multiprocessing.Process):
    def run(self):
        pass


if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    # 使用线程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(3,))   # 异步提交任务

    #等待所有任务完成
    pool.close()      # 关闭，不再接受新的任务进来，才不会出错
    pool.join()

    print(result.get())

    # imap
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))
    #
    # for result in pool.imap_unordered(get_html, [1, 5, 3]):
    #     print("{} sleep success".format(result))
