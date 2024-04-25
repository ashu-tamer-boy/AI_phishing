import requests
import re
from bs4 import BeautifulSoup

def get_links(url):
    # try:
    #     # Fetch the HTML content of the page
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         # Parse the HTML content
    #         soup = BeautifulSoup(response.content, 'html.parser')
    #         # Find all anchor tags (links)
    #         links = soup.find_all('a', href=True)
    #         # Extract the URLs from the anchor tags
    #         links_list = [link['href'] for link in links if link.get('href')]
    #         if(len(links_list) <= 2):
    #             return 0
    #         elif(len(links_list) == 0):
    #             return 1
    #     else: 
    #         return 0
    # except Exception as e:
    #     return -1
    try:    
            response = requests.get(url)
            number_of_links = len(re.findall(r"<a href=", response.text))
            if number_of_links == 0:
                return 1
            elif number_of_links <= 2:
                return 0
            else:
                return -1
    except:
            return -1

# Example usage:
# url = "https://epicor.com"
# links = get_links(url)
# if links:
#     print(f"Links pointing to {links}:")
   
# else:
#     print(f"Failed to retrieve links for {url}.")