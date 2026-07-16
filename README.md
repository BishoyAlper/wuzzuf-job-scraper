## Project Overview

Wuzzuf Job Scraper is a Python automation project that extracts job listings from Wuzzuf using a hybrid web scraping approach.

The scraper begins by accepting a job keyword from the user, then searches Wuzzuf and calculates the total number of available jobs. It automatically navigates through every search result page, extracts static information using BeautifulSoup, and visits each job details page with Selenium to retrieve dynamically loaded content.

The application collects structured job information, including titles, companies, locations, posting dates, requirements, salaries, descriptions, and direct job links. Once the scraping process is complete, all data is exported into a CSV file for further analysis or reporting.

## User Input

The user enters a job title or keyword.

<img width="954" height="55" alt="Screenshot 2026-07-16 at 7 26 06 PM" src="https://github.com/user-attachments/assets/6170ddb8-32a3-405c-bc12-e2f507e87e0d" />

---

## Search Wuzzuf

The application sends an HTTP request to the Wuzzuf search page using the provided keyword.

*Technology:* Requests

📷 Screenshot:

<img width="619" height="36" alt="Screenshot 2026-07-16 at 7 27 47 PM" src="https://github.com/user-attachments/assets/45b50948-7092-4df5-b802-da125e8a579b" />

---

## Step 4: Handle Pagination

The scraper determines the total number of available jobs and iterates through every search result page until all jobs are processed.

📷 Screenshot:


<img width="430" height="867" alt="Screenshot 2026-07-16 at 7 31 03 PM" src="https://github.com/user-attachments/assets/4ddad85a-c3af-4697-82e5-651a83610155" />

---

## Export Data

Finally, all collected information is exported into a CSV file.

Exported Columns:

- Job Title
- Company
- Salary
- Posted Date
- Location
- Job Link
- Requirements
- Job Description

📷 Screenshot:

<img width="1511" height="861" alt="Screenshot 2026-07-16 at 7 35 12 PM" src="https://github.com/user-attachments/assets/d62537a6-402c-4d6c-ae56-bd6dd27d3558" />
