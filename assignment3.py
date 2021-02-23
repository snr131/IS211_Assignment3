"""
IS 211 Assignment 3 in Python 3.8.6
Sarah May
Start program by entering python assignment3.py into the command line
You will then be prompted to enter a url
Output will contain the percent of image requests, the most popular browser, and the number of hits per hours
"""

"""Import modules"""
import urllib
from urllib import request
import csv
import re
import datetime
import argparse


"""Test program with this url"""
#url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'


"""Download the data using the download_data function"""
def download_data(url):
    """Open the URL"""
    response = urllib.request.urlopen(url)

    """Read the response and convert it to string characters if it was in binary"""
    file_content = response.read().decode('utf-8')
    return file_content


"""Save the results of the download_data function to the variable downloadedData"""
#downloaded_data = download_data(url)


"""I am storing the data I need in lists"""
#paths_to_files = []
#useragents = []
#timestamps = []


def process_data(downloaded_data):
    """Feeds downloadedData into csv.reader for processing"""
    myreader = csv.reader(downloaded_data.splitlines())

    """Row by row, append data to their respective lists"""
    for row in myreader:
        timestamps.append(row[1])
        paths_to_files.append(row[0])
        useragents.append(row[2])
        #print(row[0],row[2]) 
    return paths_to_files
    return useragents
    return timestamps


"""Test the processData function using the downloadedData, and save the results to the processed_data variable"""
#processed_data = process_data(downloaded_data)


def percent_image_files(processed_data):
    """The paths_to_files list holds all file paths in the processed_data"""
    string = ''.join(paths_to_files)

    """Compile a list called match that contains each of the extensions in the re expression below"""
    match = re.findall(r".jpg|.JPG|.gif|.GIF|.png|.PNG", string)

    """Calculate the percentage of image files"""
    image_request_percentage = (len(match) / len(paths_to_files)) * 100
    image_requests = 'Image requests account for {}% of all requests'.format(image_request_percentage)
    print(image_requests)


def browser_count(useragents):
    """Match the user agents to the pattern to identify the browser"""
    userAgentPattern = re.compile("(MSIE|Trident|(?!Gecko.+)Firefox|(?!AppleWebKit.+Chrome.+)Safari(?!.+Edge)|(?!AppleWebKit.+)Chrome(?!.+Edge)|(?!AppleWebKit.+Chrome.+Safari.+)Edge|AppleWebKit(?!.+Chrome|.+Safari)|Gecko(?!.+Firefox))(?: |\/)([\d\.apre]+)")
    
    """Count the number of hits per browser, store in a dictionary"""
    browser_count_dict = {'Firefox': 0, 'Chrome': 0, 'MSIE': 0, 'Safari': 0}
    for i in range(0, len(useragents)):
        useragenttuple = re.search(userAgentPattern, useragents[i]).groups()
        if useragenttuple[0] == 'Firefox':
            browser_count_dict['Firefox'] += 1
        elif useragenttuple[0] == 'Chrome':
            browser_count_dict['Chrome'] += 1
        elif useragenttuple[0] == 'MSIE':
            browser_count_dict['MSIE'] += 1
        elif useragenttuple[0] == 'Safari':
            browser_count_dict['Safari'] += 1
    return browser_count_dict


"""Store the results of the browser_count function to the browser_count_tally variable"""
#browser_count_tally = browser_count(useragents)


def most_pop_browser(browser_count_tally):
    """Calculate and print the percentage of the total of the most popular browser"""
    most_popular_browser_percent = ((max([i for i in browser_count_tally.values()])) / len(useragents)) * 100
    most_popular_browser = max(browser_count_tally, key=browser_count_tally.get) 
    print('In this dataset, {} was the most popular browser with {}% of hits'.format(most_popular_browser, most_popular_browser_percent)) 


#coverted_timestamps = [datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') for timestamp in timestamps] 


#hours = [timestamp.hour for timestamp in coverted_timestamps]


def hits_per_hour(hours): 
    """Create an empty dictionary to store hours and hits"""
    hours_dict = {} 
    for item in hours: 
        if (item in hours_dict):
            hours_dict[item] += 1
        else:
            hours_dict[item] = 1
    for key, value in hours_dict.items(): 
        print("Hour {} has {} hits".format(key, value))



def main(url):
    print(f"Running main with URL = {url}...")
    return url


if __name__ == "__main__":
    # main entry point
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str)
    args = parser.parse_args()
    args.url = str(input('Enter the url\n'))
    main(args.url)
    downloaded_data = download_data(args.url)
    paths_to_files = []
    useragents = []
    timestamps = []
    processed_data = process_data(downloaded_data)
    percent_image_files(processed_data)
    browser_count_tally = browser_count(useragents)
    most_pop_browser(browser_count_tally)
    coverted_timestamps = [datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') for timestamp in timestamps] 
    hours = [timestamp.hour for timestamp in coverted_timestamps]
    hits_per_hour(hours)