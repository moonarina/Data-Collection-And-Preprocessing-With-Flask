import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape_data(url, url2, container_name, column_name, element, attrs, start, end):
    data = []  # List to store data

    for page in range(start, end):  # Iterate from start to end page
        full_url = f'{url}/{page}'  # Full URL with page number
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_containers = soup.findAll('div', attrs={'class': container_name})

        for container in div_containers:
            review = container.find(element, attrs=attrs)
            if review:
                # Get the URL for each title
                if url2:
                    relative_url = review.find('a')['href']
                    absolute_url = f'{url2}/{relative_url}'
                    # Visit the URL to get the address
                    response = requests.get(absolute_url)
                    soup_inner = BeautifulSoup(response.text, 'html.parser')
                    address_element = soup_inner.find('address', class_='item-address')
                    if address_element:
                        address = address_element.text.strip()
                        data.append((address))
                else:
                    data.append(review.text.strip())
            else:
                item = container.find(element, attrs=attrs)
                if item:
                    data.append(item.text.strip())

    # Create a dataframe from a list of data
    df = pd.DataFrame({column_name: data})
    print('Total properties acquired:', len(df))
    print('Success scraped the data')
    # Show dataframe
    return df