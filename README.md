# Synchronous vs. Asynchronous vs. Multithreading

![Synchronous vs. Asynchronous](https://miro.medium.com/v2/resize:fit:1558/1*6YjH0YEvGBxhdOHb3FRfqQ.png)

In software development, understanding the differences between synchronous, asynchronous, and multithreading programming is crucial for optimizing performance and responsiveness. This article provides a comprehensive overview of these concepts, including practical examples.

## 1. Synchronous

- Executes tasks one after the other. If there are multiple tasks, they are processed sequentially, blocking subsequent tasks until the current one finishes.

### Example:
- Imagine we have 3 customers in our café:
    - Customer 1: needs coffee, which takes 3 seconds.
    - Customer 2: needs tea, which takes 2 seconds.
    - Customer 3: needs water, which takes 1 second.
- The waiter takes the order from Customer 1 first, goes to the kitchen, finishes it, then moves to Customer 2, and so on.
- Total time: 3 + 2 + 1 = 6 seconds.

- In the main thread, the CPU executes code line by line and cannot proceed to the next line until the current one is finished.

```python
import time

start_code_time = time.time()

def waiter(customer_request, duration):
    print(f"start {customer_request} request ...")
    time.sleep(duration)
    print(f"finished {customer_request} request ...")

def main():
    waiter("coffee", 3)
    waiter("tea", 2)
    waiter("water", 1)

if __name__ == '__main__':
    main()
    print(f" code time finished: {round(time.time()-start_code_time, 1)}")

```

# Output

```sql
start coffee request ...
finished coffee request ...
start tea request ...
finished tea request ...
start water request ...
finished water request ...
code time finished: 6.0

```


## 2. Asynchronous

- Allows tasks to run independently of the main program flow, using a scheduler to manage task execution without blocking the main thread.

### Example:
- Using asynchronous programming:
    - The waiter takes all orders immediately and processes them as the kitchen becomes available.
- Tasks can start before the previous one finishes, and the total time can be as short as the longest single task (3 seconds in this case).


# Using a Coroutine Object:

- Adds a wrapper to the function, which has three statuses: [start, pending, end].
- Allows for non-blocking, cooperative multitasking within a single thread.
- Components include:

    - **Task**: Represents an asynchronous operation.
    - **Special Thread**: A thread dedicated to handling asynchronous tasks.
    - **Schedulerv**: Manages the order and timing of task execution.
    - **Await**: Pauses the execution of a coroutine until the awaited task is completed.
    - **Event Loop**: Continuously checks for and executes tasks.
    - **Result**: The outcome of an asynchronous operation.

```python
import asyncio
import time

start_code_time = time.time()

async def waiter(customer_request, duration):
    print(f"start {customer_request} request ...")
    await asyncio.sleep(duration)
    print(f"finished {customer_request} request ...")

async def main():
    await asyncio.gather(
        waiter("coffee", 3),
        waiter("tea", 2),
        waiter("water", 1)
    )

if __name__ == '__main__':
    asyncio.run(main())
    print(f" code time finished: {round(time.time()-start_code_time, 1)}")

```

# Output

```sql
start coffee request ...
start tea request ...
start water request ...
finished water request ...
finished tea request ...
finished coffee request ...
code time finished: 3.0

```


# Multithreading

![Multithreading](https://miro.medium.com/v2/resize:fit:1276/1*0KqxBjbiEriVNjbnZWkRfA.jpeg)

- Utilizes multiple threads to execute tasks concurrently, reducing overall time by performing multiple operations simultaneously.

### Example:
- Using the previous example:
    - Each customer's order is handled by a separate thread.
- Total time: 3 seconds, as all tasks are executed in parallel.


```python
import concurrent.futures
import time

start_code_time = time.time()

def waiter(customer_request, duration):
    print(f"start {customer_request} request ...")
    time.sleep(duration)
    print(f"finished {customer_request} request ...")

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(waiter, "coffee", 3),
            executor.submit(waiter, "tea", 2),
            executor.submit(waiter, "water", 1)
        ]
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    main()
    print(f" code time finished: {round(time.time()-start_code_time, 1)}")


```

# Output

```sql
start coffee request ...
start tea request ...
start water request ...
finished water request ...
finished tea request ...
finished coffee request ...
code time finished: 3.0

```
