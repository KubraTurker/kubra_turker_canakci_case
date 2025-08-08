# Insider QA Case
This repository contains automated tests for verifying the functionality for Insider website using Python + Pytest + Allure.
## What is Tested?

### 1. Home and Careers Page 
1. Verify that the Insider homepage (https://useinsider.com/) opens successfully. 
2. From the top navigation, open Company -> Careers and check that:
   - [x] Locations block is visible 
   - [x] Teams block is visible 
   - [x] Life at Insider block is visible

### 2. Job Listings Page
1. Go to https://useinsider.com/careers/quality-assurance/, click See all QA jobs, and in Open Positions:
   - [x] Filter by Location: Istanbul, Turkey
   - [x] Filter by Department: Quality Assurance 
   - [x] Verify that the jobs list is displayed
2. For each job in the list, verify:
   - [x] Position contains “Quality Assurance”
   - [x] Department is “Quality Assurance”
   - [x] Location is “Istanbul, Turkey”
3. Click View Role and check that it redirects to the Lever Application Form page (jobs.lever.co).

## Technologies Used

The following technologies and libraries are used in this project:

- Python 3.9+ -> Used for writing tests
- Pytest -> Used as the test framework

## Setup and Execution

1. Install Dependencies

```commandline
pip install -r requirements.txt
brew install allure 
```
2. Run Tests

To execute the tests:
```commandline
pytest
```
or if you want to use Allure Reports
```commandline
python -m pytest --alluredir allure-results
```

To view Allure Reports
```commandline
allure serve allure-results
```

