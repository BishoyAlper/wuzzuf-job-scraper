## Project Overview

Wuzzuf Job Scraper is a Python automation project that extracts job listings from Wuzzuf using a hybrid web scraping approach.

The scraper begins by accepting a job keyword from the user, then searches Wuzzuf and calculates the total number of available jobs. It automatically navigates through every search result page, extracts static information using BeautifulSoup, and visits each job details page with Selenium to retrieve dynamically loaded content.

The application collects structured job information, including titles, companies, locations, posting dates, requirements, salaries, descriptions, and direct job links. Once the scraping process is complete, all data is exported into a CSV file for further analysis or reporting.

## User Input

The user enters a job title or keyword.

---

## Search Wuzzuf

The application sends an HTTP request to the Wuzzuf search page using the provided keyword.

*Technology:* Requests


---

## Step 4: Handle Pagination

The scraper determines the total number of available jobs and iterates through every search result page until all jobs are processed.


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

