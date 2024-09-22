import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time

time.sleep(2)  # Sleep for 2 seconds between requests


url = "https://csoonline.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

soup = BeautifulSoup(response.content, "html.parser")

# You can now view the parsed HTML content
print(soup.prettify())  # To see the structured HTML in a readable format

# Extract all links
links = soup.find_all('a')

# Print all links with their href attribute
links = soup.find_all('a', href=True)

link_data = []
for link in links:
    link_text = link.text.strip()  # Strip whitespace
    href = link.get('href')        # Get the href attribute
    
    # Only include links with meaningful text and non-empty href attributes
    if link_text and href:
        link_data.append([link_text, href])

# Step 7: Create a pandas DataFrame
df = pd.DataFrame(link_data, columns=["Link Text", "URL"])

# Step 8: Print the DataFrame in a well-formatted table
print(df.to_string(index=False))

# Extracting specific elements by class
# title = soup.find('h1', class_='title-class')  # Replace with the actual class name
title = soup.find('h1')  # Example tag
if title is not None:
    print(title.text)
else:
    print("Title not found")

print(title.text)  # Extract the text inside the h1 tag

for page in range(1, 6):  # Scraping 5 pages as an example
    url = f"https://csoonline.com/page/{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # Extract data as before

data = {"links": []}

for link in links:
    href = link.get('href')
    data["links"].append(href)

with open("scraped_data.json", "w") as json_file:
    json.dump(data, json_file)



