import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import *


def extract_links_and_forms(url):
    """
    Function that requests the base URL specified, parses the HTML code from the response,
    and gives all the pages and forms available via the HTML page.
    """
    try:
        data = {}
        response = requests.get(url, verify=False)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting links
        GET_url = {}
        for link in soup.find_all('a', href=True):
            # Building full URLs
            full_url = urljoin(url, link['href'])
            GET_url[full_url] = {}  # Fixed: Use append to add to the list

        data["GET"] = GET_url

        # Extracting forms if they exist
        for form in soup.find_all('form'):
            form_details = {
                'action': urljoin(url, form.get('action', '')),
                'method': form.get('method', 'GET').upper()
            }
            if form_details['method'] in data:
                data[form_details['method']].append(form_details['action'])
            else:
                data[form_details['method']] = [form_details['action']]

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to reach {url}\nDetails: {e}")
        return {}


def map_website(url, dont_crawl_that, visited=None):
    """
    Function to recursively map a website starting from the base URL.
    Calls `extract_links_and_forms` for each page and processes the results.
    """
    if visited is None:
        visited = set()  # Initialize the set of visited URLs

    for domain_name in dont_crawl_that:
        print("dont crawl that", dont_crawl_that)
        print("url : ", url)
        print("domain : ", domain_name)
        print(url in domain_name)
        if url.find(domain_name) != -1:
            print(f"not visiting {url}")
            return {}

    # Stop if the URL has already been visited
    if url in visited:
        return {}

    print(f"Visiting: {url}")
    visited.add(url)  # Mark the current URL as visited

    # Call the given function to extract links and forms
    data = extract_links_and_forms(url)

    # Initialize the result structure
    site_map = data

    # Recursively visit all GET links
    for link in data.get('GET', []):
        if link not in visited:
            child_map = map_website(link, dont_crawl_that, visited)
            site_map['GET'][link] = child_map  # Add the child map to the current site map

    return site_map
    
    
