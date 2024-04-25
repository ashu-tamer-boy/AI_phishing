import requests
from bs4 import BeautifulSoup
import networkx as nx

def get_page_rank(url):
    # Fetch the HTML content of the webpage
    try:
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract all links (href attributes) from the webpage
        links = [a.get('href') for a in soup.find_all('a', href=True)]

        # Remove None values and non-HTTP links
        links = [link for link in links if link is not None and link.startswith('http')]

        # Create a directed graph
        G = nx.DiGraph()

        # Add nodes (webpages) and edges (links) to the graph
        for link in links:
            G.add_edge(url, link)

        # Calculate PageRank
        page_rank = nx.pagerank(G)

        # Return the PageRank of the specified URL
        x = page_rank[url] if url in page_rank else 0
        if x < 0.1:
            return 1
        else:
            return -1
    except:
        return -1
# url = "https://epicor.com"  # Replace with the URL you want to get the PageRank for
# print("PageRank of URL", url, ":", get_page_rank(url))
