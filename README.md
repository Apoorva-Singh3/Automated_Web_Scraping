# task_web_automation_scraping
Web scraping of amazon products(1000 URLS) parameters(fields) using selenium and requests libs -- python3

## TASK:
1. Scrap minimum hundred Urls of thousand url list.
2. Using Selenium following details to be scraped:
Product Title, Product Image Url, Price of the Product, Product details.
3. Total time taken to complete hundred Urls.
4. Output to be in the list of dictionaries, finally represented in JSON.
5. Upload code file, resultant JSON file and a proper readme.

## Approach:
1. Made a list of Urls.
2. Made a code for checking the status of Urls.
3. Xpath was made for functional Urls.
4. Details for the Urls was imported from csv file.
5. Code was modified according to the details needed and format of the output required.

## Issue Faced:
1. Some Urls were showing Error 503, and were not available.
2. Some web elements text were not returning even when the element was already present.
3. Urls from list ending with 'X' were accesible

## Timer Introduced:
1. Timer logic introduced in the code for returing time difference for each set of 100 Url parsed.

## Testing: 
1. Manually done for all selected countries (4)
2. All 94 Urls collected and tested/scraping with 'Asin' parameter ending with 'X'.(89 passing: resultant Json attached).
3. All of the 1000 Urls list being tested.

## Solution:
```bash
pip install -r requirements.txt
```

```bash
python az.py
```
1. *az.py* python file for running the webscripting logic, getting url data from the csv file(provided)
2. ChromeDriver
3. *my_json* JSON file
4. CSV file (downloaded from the task spreadsheet)
