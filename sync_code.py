# Example 1:

# import time 

# start_code_time = time.time()

# def waiter(customer_request,duration):
#     print(f"start {customer_request} request ...")
#     time.sleep(duration)
#     print(f"finished {customer_request} request ...")

# def main():
#     waiter("cofee",3)
#     waiter("tea",2)
#     waiter("water",1)

# if __name__ == '__main__':
#     main()
#     print(f" code time finished: {round(time.time()-start_code_time,1)}")


# Example 2:

import requests
import os 
import time 


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
    print(response.status_code)

def main():
    for url in urls:
        get_info(url)

if __name__ == '__main__':
    main()
    print(f" code time finished: {round(time.time()-start_code_time,1)}")