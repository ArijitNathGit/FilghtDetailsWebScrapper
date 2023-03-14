from bs4 import BeautifulSoup
import requests
import time


def get_requests():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills_name = job.find('span', class_='srp-skills').text.strip()
        posted_time = job.find('span', class_='sim-posted').text.strip()

        print(f"Company Name: {company_name}")
        print(f"Required Skills: {skills_name}")
        print(f"Published: {posted_time}")
        print()

if __name__ == '__main__':
    while True:
        get_requests()
        time_wait = 10
        print(f'Waiting {time_wait} secomds ...\n')
        time.sleep(time_wait)

