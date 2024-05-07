import time
from bs4 import BeautifulSoup
import requests

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('Enter Unfamiliar tool: ').split()
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").text.replace(' ', '')
        # Check if 'today' is in the date posted and print
        if 'today' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            for skill in unfamiliar_skill:
                if skill.lower() in skills.lower():
                    break
            else:
                with open(f'venv/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f"File Saved: {index}")

# Timer to scrape every 10 minutes
if __name__ == '__main__':
    while True:
         find_jobs()
         time_wait = 10
         print(f"Waiting {time_wait} minutes...")
         time.sleep(time_wait * 60)
