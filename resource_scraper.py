import requests
from bs4 import BeautifulSoup
import os
import time

# URL to scrape
url = "https://mindremakeproject.org/2020/01/13/free-printable-pdf-workbooks-manuals-and-toolkits-for-providers-who-work-with-children-adolescents-families/"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div with class "entry-content"
entry_content = soup.find('div', class_='entry-content')

if entry_content:
    # Find all links within the entry-content div
    links = entry_content.find_all('a')
    
    # Create a 'pdfs' folder if it doesn't exist
    if not os.path.exists('pdfs'):
        os.makedirs('pdfs')
    
    # Extract and download PDF links
    pdf_counter = 0
    total_links = 0
    skipped = 0
    errors = 0
    
    for link in links:
        href = link.get('href')
        text = link.text.strip()
        if href:
            total_links += 1
            if '.pdf' in href.lower():
                try:
                    filename = os.path.join('pdfs', href.split('/')[-1])
                    if os.path.exists(filename):
                        print(f"Skipping: {filename} (already exists)")
                        skipped += 1
                        continue
                    
                    pdf_response = requests.get(href)
                    if pdf_response.status_code == 200:
                        with open(filename, 'wb') as file:
                            file.write(pdf_response.content)
                        pdf_counter += 1
                        print(f"Downloaded: {filename}")
                    
                except Exception as e:
                    errors += 1
                    print (f"ERROR:{pdf_response.status_code} - Unable to download {text}: {str(e)}")                
    
    print(f"\nTotal links found: {total_links}")
    print(f"Total PDFs downloaded: {pdf_counter}")
    print(f"Total PDFs skipped: {skipped}")
    print(f"Total PDF errors: {errors}")
else:
    print("Could not find the entry-content class.")