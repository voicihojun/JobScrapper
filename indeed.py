import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://ca.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find("div", {"class":"pagination"})
  links = pagination.find_all("a")
  
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  last_page = pages[-1]
  
  return last_page

def extract_job(html):
  title = html.find("h2",{"class":"jobTitle"}).find_all("span")[-1]["title"]
  
  name = html.find("span", {"class": "companyName"}).string
  location = html.find("div", {"class": "companyLocation"}).string
  job_id = html["data-jk"]
  
  # print({"title": title, "company": name, "location": location, "link": f"https://ca.indeed.com/viewjob?jk={job_id}"})
  return {"title": title, "company": name, "location": location, "link": f"https://ca.indeed.com/viewjob?jk={job_id}"}

  


def get_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Indeed Scrapping page : {page}")
    # print(f"{URL}&start={page*LIMIT}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("a", {"class":"result"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
    
  return jobs


def get_indeed_jobs():
  last_page = get_last_page()
  jobs = get_jobs(last_page)
  return jobs