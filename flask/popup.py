import requests
from bs4 import BeautifulSoup


from googlesearch import search

import re

def extract_domain(url):
  # Define a regular expression pattern for extracting the domain
  pattern = r"(https?://)?(www\d?\.)?(?P<domain>[\w\.-]+\.\w+)(/\S*)?"
  # Use re.match to search for the pattern at the beginning of the URL
  match = re.match(pattern, url)
  # Check if a match is found
  if match:
  # Extract the domain from the named group "domain"
    domain = match.group("domain")
    return domain
  else:
    return None

# Example usage
# domain1 = extract_domain("https://www.example.com/path/to/page")
# domain2 = extract_domain("http://sub.example.co.uk/some-page")
# print(f"Domain 1: {domain1}")
# print(f"Domain 2: {domain2}")
def check_for_popups(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        if response.status_code == 200:
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            # Look for JavaScript code that might trigger pop-ups
            script_tags = soup.find_all('script')
            for script_tag in script_tags:
                if "window.open" in script_tag.text:
                    return 1
            return -1
        else:
            # print("Failed to fetch URL:", response.status_code)
            return -1
    except Exception as e:
        # print("An error occurred:", e)
        return -1

# Example usage:
# url = "https://example.com"
# has_popups = check_for_popups(url)
# if has_popups is not None:
#     if has_popups:
#         return 1;
#     else:
#         print("The URL does not have pop-ups.")
def get_page_rankk(url):

    query =  extract_domain(url).split('.')
# initilazing index=0
    index = 0
    flag = False
# search will return an object containing
# all url from google search results
# here, tid is top level domain, 
# stop means how many search results you want
# stop=100 means we will get top 100 results from google
    for i in search(query[0],        # The query you want to run  
                      # The top level domain  
                    lang = 'en'  # The language  
                   # num = 10,     # Number of results per page  
                    #start = 0,    # First result to retrieve  
                    #stop = 100,  # Last result to retrieve  
                    #pause = 2.0,  # Lapse between HTTP requests  
                ):  
    
        if url in i:
            # printing index of website and url
            flag = True
             
        
    if(flag):
        return 1
    else:
        return -1
    
# print(get_page_rank("https://erpcustomer.epicor.com/lms/catalog/browse"))
#print(check_for_popups("https://erpcustomer.epicor.com/lms/catalog/browse"))