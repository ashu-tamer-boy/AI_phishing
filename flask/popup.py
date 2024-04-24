import requests
from bs4 import BeautifulSoup


from googlesearch import search

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
                    return True
            return 1
        else:
            print("Failed to fetch URL:", response.status_code)
            return -1
    except Exception as e:
        print("An error occurred:", e)
        return -1

# Example usage:
# url = "https://example.com"
# has_popups = check_for_popups(url)
# if has_popups is not None:
#     if has_popups:
#         return 1;
#     else:
#         print("The URL does not have pop-ups.")
def get_page_rank(url):

    query = input('get me' + url)
# initilazing index=0
    index = 0
    flag = False
# search will return an object containing
# all url from google search results
# here, tid is top level domain, 
# stop means how many search results you want
# stop=100 means we will get top 100 results from google
    for i in search(query,        # The query you want to run  
                    tld = None,  # The top level domain  
                    lang = 'en',  # The language  
                    num = 10,     # Number of results per page  
                    start = 0,    # First result to retrieve  
                    stop = None,  # Last result to retrieve  
                    pause = 2.0,  # Lapse between HTTP requests  
                ):  
    
        if url in i:
            # printing index of website and url
            flag = True
             
        index += 1
    if(flag):
        return 1
    else:
        return -1
    
print(get_page_rank("https://erpcustomer.epicor.com/lms/catalog/browse"))
#print(check_for_popups("https://erpcustomer.epicor.com/lms/catalog/browse"))