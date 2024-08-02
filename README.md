# Synchronous vs. Asynchronous vs. Multithreading

![Sample Image](https://miro.medium.com/v2/resize:fit:1558/1*6YjH0YEvGBxhdOHb3FRfqQ.png)


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


## 2. Asynchronous

- Allows tasks to run independently of the main program flow, using a scheduler to manage task execution without blocking the main thread.

### Example:
- Using asynchronous programming:
    - The waiter takes all orders immediately and processes them as the kitchen becomes available.
- Tasks can start before the previous one finishes, and the total time can be as short as the longest single task (3 seconds in this case).

### Using a Coroutine Object:
- Adds a wrapper to the function, which has three statuses: [start, pending, end].
- Allows for non-blocking, cooperative multitasking within a single thread.
- Components include:
    - **Task**: Represents an asynchronous operation.
    - **Special Thread**: A thread dedicated to handling asynchronous tasks.
    - **Scheduler**: Manages the order and timing of task execution.
    - **Await**: Pauses the execution of a coroutine until the awaited task is completed.
    - **Event Loop**: Continuously checks for and executes tasks.
    - **Result**: The outcome of an asynchronous operation.

![Sample Image](https://miro.medium.com/v2/resize:fit:1276/1*0KqxBjbiEriVNjbnZWkRfA.jpeg)


## 3. Multithreading

- Utilizes multiple threads to execute tasks concurrently, reducing overall time by performing multiple operations simultaneously.

### Example:
- Using the previous example:
    - Each customer's order is handled by a separate thread.
- Total time: 3 seconds, as all tasks are executed in parallel.

