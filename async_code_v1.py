# Example 1

# import asyncio
# import time 

# start_code_time = time.time()

# async def waiter(customer_request,duration):
#     print(f"start {customer_request} request ...")
#     await asyncio.sleep(duration)
#     print(f"finished {customer_request} request ...")

# async def main():
#     await waiter("cofee",3)
#     await waiter("tea",2)
#     await waiter("water",1)

# if __name__ == '__main__':
#     asyncio.run(main())
#     print(f" code time finished: {round(time.time()-start_code_time,1)}")


# '''
# The code time finished : 6 sec also because it using async but not using task so we call the function like sync
# '''


# ===============================================================
# ===============================================================

# Example 2

import asyncio
import time 
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

async def get_info(urls):
    async with aiohttp.ClientSession() as session:
        for url in urls:
            response = await session.get(url, ssl=False)
            print(response._real_url)


if __name__ == '__main__':
    asyncio.run(get_info(urls))
    print(f" code time finished: {round(time.time()-start_code_time,1)}")