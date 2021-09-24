import requests
from bs4 import BeautifulSoup


URL = "https://stackoverflow.com/jobs?q=python"

def get_last_page():
  results = requests.get(URL)
  soup = BeautifulSoup(results.text, "html.parser")
  links = soup.find_all("a", {"class":"s-pagination--item"})
  
  pages = []
  for link in links[:-1]:
    pages.append(int(link.find("span").string))
  last_page = pages[-1]
  return last_page


def extract_job(html): 
  title = html.find("a", {"class": "s-link"})["title"]
  name = html.find("h3", {"class":"fc-black-700"}).find("span").string
  # because of the NoneType. I removed strip() for the name
  location = html.find("span", {"class":"fc-black-500"}).string.strip()
  job_id = html["data-jobid"]
  
  # print(f"title: {title}, name: {name}, location: {location}, link: https://stackoverflow.com/jobs/{job_id}")

  return {"title": title, "company": name, "location": location, "link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
  jobs = []
  # for i in range(2):
  for page in range(last_page):
    print(f"SO Scrapping Page : {page}")
    results = requests.get(f"{URL}&pg={page}")  
    soup = BeautifulSoup(results.text, "html.parser")
    results = soup.find_all("div", {"class": "js-result"})
    for result in results:
      job = extract_job(result)

  jobs.append(job)
  return jobs


def get_so_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
  
  
  