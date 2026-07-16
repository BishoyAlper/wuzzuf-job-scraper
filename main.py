import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

job_titles, job_company, job_link, job_posted_time, job_location, job_requirements, job_salary, job_description = [], [], [], [], [], [], [], []
raw = ['Job title', 'Job company', "job salary",'posted', 'Job_location', "Job link", "Job requirements", "job description"]

#driver setup
def driver_setup():
    options = Options()
    options.add_argument('--headless=new')
    return webdriver.Chrome(options=options)

# Extract data from website
def extract_data(link):
    try:
        page = requests.get(link)
        # Adding data to beautiful soup
        soup = BeautifulSoup(page.content, 'lxml')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error in extracting link {link} : {e}")

# Extracting details
def extracting_job_details(jobs):
    for job in jobs:
        # Extracting titles
        title = job.find('h2').get_text(strip=True)
        job_titles.append(title)

        # Job company
        company = job.find('a', class_= "css-ipsyv7").get_text(strip=True)
        company = company.replace("-", "")
        job_company.append(company)

        # Job location
        location = job.find('span', class_ = "css-16x61xq").text.strip()
        job_location.append(location)

        # Job links
        link = job.find('a', class_='css-ipsyv7').get('href')
        job_link.append(link)

        # Job posted
        post = job.find("div", class_="css-1k5ee52").find_all("div")[-1].get_text(strip=True)

        job_posted_time.append(post)

        # Job requirements
        reqs = job.find('div', class_ ='css-1rhj4yg')

        for req in reqs.find_all("a"):
            job_requirements.append(req.text.strip().replace("·", "").strip())

#extracting salary and description
def extract_salary_description(link, driver):
    try:
        driver.get(link)

        # extract salary
        salary = "Not preview"
        try:
            job_details = driver.find_element(By.CLASS_NAME, 'css-3kx5e2')
            salary = job_details.find_element(By.XPATH, "//span[text()='Salary:']/following-sibling::span").text.strip()
        except Exception as e:
            print(f"Error in extracting salary in {link} : {e}")

        # extracting description
        description = "Not provided"
        try:
            description = driver.find_element(
                By.XPATH,
                "//h2[text()='Job Description']/following-sibling::div"
            ).text.strip()
        except Exception as e:
            print(f"Error in extracting description {link} : {e}")
        return salary, description
    except Exception as e:
        print(f"Error in extracting salary and description in {link} : {e}")
        return "Not preview", "Not preview"

# Add details to CSV file
def add_to_csv(all_data):
    with open('/Users/bishoy.alper.aziz/PycharmProjects/wuzzuf_web_scrapping/wuzzuf.csv', 'w') as file:
        wr = csv.writer(file)
        wr.writerow(raw)
        wr.writerows(all_data)

# Get job offers count
def job_offer_count(position):
    soup = extract_data(f"https://wuzzuf.net/search/jobs/?a=navbl&q={position}&start=0")
    count = int(soup.find('p', class_="css-17yjama").find('strong').text.strip())
    return count

def main():
    driver = driver_setup()
    posision = input("Please enter your Career : ")

    #count page num
    job_offers_count = job_offer_count(posision)
    job_pages_count = job_offers_count // 15

    print(f"We reached {job_offers_count} job")
    for i in range(job_pages_count + 1):
        soup = extract_data(f"https://wuzzuf.net/search/jobs/?a=navbl&q={posision}&start={i}")
        jobs = soup.find_all("div", class_="css-ghe2tq e1v1l3u10")
        extracting_job_details(jobs)
        print(f"Congrates page {i + 1} finshed")

    for link in job_link:
        salary, description = extract_salary_description(link, driver)
        job_salary.append(salary)
        job_description.append(description)
        print(f"Congrates finshed extract data in {link}")

    # ['Job title', 'Job company', 'posted', 'Job_location', "Job link", "Job requirements"]
    all_data = list(zip(
        job_titles,
        job_company,
        job_salary,
        job_posted_time,
        job_location,
        job_link,
        job_requirements,
        job_description
    ))

    add_to_csv(all_data)

main()
