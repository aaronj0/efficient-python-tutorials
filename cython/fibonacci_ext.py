import os
import threading
import time
import fibmodule

# To store results from each thread
results = []

def call_fib():
    def thread_func():
        result = fibmodule.fib(38)
        results.append(result)

    threads = []
    for _ in range(os.cpu_count()):
        thread = threading.Thread(target=thread_func)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)

a = time.time()
total_sum = call_fib()
print("Sum of Fibonacci results:", total_sum)
print("Time taken:", time.time() - a)
