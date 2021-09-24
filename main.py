from indeed import get_indeed_jobs
from stackoverflow import get_last_page, get_so_jobs
from save import save_to_file


# TODO : I scrape only 4/16 pages of indeed because of 'next'.
# So, todo is scrapping all 16 pages from indeed website.
# and now, i only search 'python'. I want to search bar to put what i want to search. 

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = indeed_jobs + so_jobs

file = save_to_file(jobs)

