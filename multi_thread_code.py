# Example 1

# import concurrent.futures
# import time

# start_code_time = time.time()

# def waiter(customer_request, duration):
#     print(f"start {customer_request} request ...")
#     time.sleep(duration)
#     print(f"finished {customer_request} request ...")

# def main():
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # Create a thread for each task
#         futures = [
#             executor.submit(waiter, "coffee", 3),
#             executor.submit(waiter, "tea", 2),
#             executor.submit(waiter, "water", 1)
#         ]
#         # Wait for all threads to complete
#         concurrent.futures.wait(futures)

# if __name__ == '__main__':
#     main()
#     print(f" code time finished: {round(time.time()-start_code_time,1)}")

# '''
# The code time finished: approximately 3 seconds because tasks are executed concurrently using multiple threads.
# '''


# ===============================================================
# ===============================================================

# Example 2

import concurrent.futures
import time
import requests

start_code_time = time.time()

urls = [
    'https://www.scrapingcourse.com/ecommerce/page/1/',
    'https://www.scrapingcourse.com/ecommerce/page/2/',
    'https://www.scrapingcourse.com/ecommerce/page/3/',
    'https://www.scrapingcourse.com/ecommerce/page/4/',
    'https://www.scrapingcourse.com/ecommerce/page/5/',
    'https://www.scrapingcourse.com/ecommerce/page/6/',
    'https://www.scrapingcourse.com/ecommerce/page/7/',
    'https://www.scrapingcourse.com/ecommerce/page/8/',
    'https://www.scrapingcourse.com/ecommerce/page/9/',
    'https://www.scrapingcourse.com/ecommerce/page/10/',
    'https://www.scrapingcourse.com/ecommerce/page/11/',
    'https://www.scrapingcourse.com/ecommerce/page/12/',
]

def get_info(url):
    response = requests.get(url)
    print(response.url)

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit all URLs to the thread pool
        futures = [executor.submit(get_info, url) for url in urls]
        # Wait for all threads to complete
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    main()
    print(f" code time finished: {round(time.time()-start_code_time,1)}")

'''
The code time finished: the total time will be significantly reduced compared to the synchronous version because tasks are executed concurrently using multiple threads.
'''
