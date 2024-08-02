# Example 1

# import asyncio
# import time 
# import requests


# start_code_time = time.time()

# async def waiter(customer_request,duration):
#     print(f"start {customer_request} request ...")
#     await asyncio.sleep(duration)
#     print(f"finished {customer_request} request ...")

# async def main():
#     customer_request = [
#         {
#             "req":"cofee",
#             "dur":3
#         },
#         {
#             "req":"tea",
#             "dur":2
#         },
#         {
#             "req":"water",
#             "dur":1
#         }
#     ]

#     tasks = []

#     for cr in customer_request:
#         tasks.append(asyncio.create_task(waiter(cr['req'],cr['dur'])))

#     await asyncio.gather(* tasks)

# if __name__ == '__main__':
#     asyncio.run(main())
#     print(f" code time finished: {round(time.time()-start_code_time,1)}")


# ===============================================================
# ===============================================================

# Example 2

import asyncio
import time 
# import requests
import aiohttp


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

def get_tasks(session,urls):
    tasks = []
    for url in urls:
        tasks.append(session.get(url,ssl=False))
    return tasks

async def get_info(urls):
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,urls)
        response = await asyncio.gather(* tasks)
        for result in response:
            print(result._real_url)

if __name__ == '__main__':
    asyncio.run(get_info(urls))
    print(f" code time finished: {round(time.time()-start_code_time,1)}")
