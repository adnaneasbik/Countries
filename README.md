Country Scraper

This Python script uses the BeautifulSoup library to scrape country data from a website. It allows you to extract country names, capitals, populations, and areas from the country pages on the target website and export it to a CSV file.

Installation

To use this script, you'll need to have Python 3 installed on your computer, as well as the BeautifulSoup and Requests libraries. You can install these libraries using pip:

pip install beautifulsoup4 requests

Usage
To use the script, simply run the country_scraper.py file from the command line:

python country_scraper.py

The script will prompt you to enter the URL of the website you want to scrape. It will then scrape data from the website's country pages, and save the data to a CSV file named country_data.csv in the same directory as the script.

Output

The script will output the scraped data to a CSV file named country_data.csv. The file will have the following columns:

Name: The name of the country.

Capital: The capital of the country.

Population: The population of the country.

Area: The area of the country in square kilometers.

Disclaimer

Scraping data from websites may violate their terms of service, and can potentially lead to legal issues. It's important to ensure that you have the necessary permissions and rights before scraping any website. This script is provided for educational purposes only, and should be used at your own risk.

