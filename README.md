# task_web_automation_scraping
Web scraping of amazon products(1000 URLS) parameters(fields) using selenium and requests libs -- python3

## TASK:
1. Scrap minimum hundred urls of thousand url list.
2. Using Selenium following details to be scraped:
Product Title, Product Image Url, Price of the Product, Product details.
3. Total time taken to complete hundred urls.
4. Output to be in the list of dictionaries, finally represented in JSON.
5. Upload code file, resultant JSON file and a proper readme.

## Approach:
1. Made a list of Urls.
2. Made a code for checking the status of Urls.
3. Xpath was made for functional urls.
4. Details for the urls was imported from csv file.
5. Code was modified according to the details needed and format of the output required.

## Issue Faced:
1. Some Urls were showing Error 503, and were not available.
2. Some web elements text were not retuning even after the element already present.
3. URL from list ending with 'X' were accesible, others not

## Timer Introduced:
1. timer logic introduced in the code for returing time difference for each set of 100 url parsed.

## Testing: 
1. Manually done for all selected countries (4)
2. All 94 URL collected and tested/scraping with Asin param ending with 'X'.(89 passing: result Json attached)
3. All of the 1000 URL list being tested

## Solution:
```bash
pip install -r requirements.txt
```

```bash
python az.py
```
1. *az.py* python file for running the webscriping logic, getting url data from the csv file(provided: attched)
2. ChromeDriver
3. JSON file
4. CSV file (downloaded from the task spreadsheet)
