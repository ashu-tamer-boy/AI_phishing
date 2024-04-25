import requests
from bs4 import BeautifulSoup

def get_page_stats(url):
    try:
        # Fetch the HTML content of the webpage
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract text from the webpage
        text = soup.get_text()

        # Count the number of words
        word_count = len(text.split())

        # Extract images from the webpage
        images = soup.find_all('img')

        # Count the number of images
        image_count = len(images)

        # Extract links from the webpage
        links = soup.find_all('a')

        # Count the number of links
        link_count = len(links)

        # Return the statistics
        return {
            "url": url,
            "word_count": word_count,
            "image_count": image_count,
            "link_count": link_count
        }
    except Exception as e:
        # print("Error:", e)
        return None

# Example usage

def status(url):
      # Replace with the URL of the webpage you want to analyze
     stats = get_page_stats(url)
     if(stats == None):
           return -1
     if(stats['word_count'] < 100 and stats['image_count'] < 10 and  stats['link_count'] >20 ):
        return -1
     else:
        return 1
    
    # print("Statistics for", stats["url"])
    # print("Word count:", stats["word_count"])
    # print("Image count:", stats["image_count"])
    # print("Link count:", stats["link_count"])
# print(status("https://epicor.com" ))