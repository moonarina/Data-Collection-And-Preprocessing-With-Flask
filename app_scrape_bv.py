import pandas as pd
from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify

app = Flask(__name__)

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
    # Show dataframe
    return df

@app.route('/scraped_data')

def scrape_data_endpoint():
    
    #Bali Vacation Rentals
    
    # Retrieve title data
    df_beachfront_title = scrape_data('https://www.bukitvista.com/property-type/beachfront/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    beachfront_title_data = df_beachfront_title['Title'].tolist()
    print("Success scraped beachfront title data")
    # Retrieve address data
    df_beachfront_address = scrape_data('https://www.bukitvista.com/property-type/beachfront/page', '', 'd-flex align-items-center h-100', 'Address', 'address', {'class': 'item-address'}, 1, 10)
    beachfront_address_data = df_beachfront_address['Address'].tolist()
    print("Success scraped beachfront address data")
    # Retrieve price data
    df_beachfront_price = scrape_data('https://www.bukitvista.com/property-type/beachfront/page', '', 'd-flex align-items-center h-100', 'Price', 'li', {'class': 'item-price item-price-text'}, 1, 10)
    beachfront_price_data = df_beachfront_price['Price'].tolist()
    print("Success scraped beachfront price data")
    # Retrieve bedroom data
    df_beachfront_bedroom = scrape_data('https://www.bukitvista.com/property-type/beachfront/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    beachfront_bedroom_data = df_beachfront_bedroom['Bedroom'].tolist()
    print("Success scraped beachfront bedroom data")
    # Retrieve bathroom data
    df_beachfront_bathroom = scrape_data('https://www.bukitvista.com/property-type/beachfront/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    beachfront_bathroom_data = df_beachfront_bathroom['Bathroom'].tolist()
    print("Success scraped beachfront bathroom data")
    
    # Retrieve title data
    df_island_life_title = scrape_data('https://www.bukitvista.com/property-type/island-life/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    island_life_title_data = df_island_life_title['Title'].tolist()
    print("Success scraped island life title data")
    # Retrieve address data
    df_island_life_address = scrape_data('https://www.bukitvista.com/property-type/island-life/page', '', 'd-flex align-items-center h-100', 'Address', 'address', {'class': 'item-address'}, 1, 10)
    island_life_address_data = df_island_life_address['Address'].tolist()
    print("Success scraped island life address data")
    # Retrieve price data
    df_island_life_price = scrape_data('https://www.bukitvista.com/property-type/island-life/page', '', 'd-flex align-items-center h-100', 'Price', 'li', {'class': 'item-price item-price-text'}, 1, 10)
    island_life_price_data = df_island_life_price['Price'].tolist()
    print("Success scraped island life price data")
    # Retrieve bedroom data
    df_island_life_bedroom = scrape_data('https://www.bukitvista.com/property-type/island-life/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    island_life_bedroom_data = df_island_life_bedroom['Bedroom'].tolist()
    print("Success scraped island life bedroom data")
    # Retrieve bathroom data
    df_island_life_bathroom = scrape_data('https://www.bukitvista.com/property-type/island-life/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    island_life_bathroom_data = df_island_life_bathroom['Bathroom'].tolist()
    print("Success scraped island life bathroom data")
    
    # Retrieve title data
    df_jungle_view_title = scrape_data('https://www.bukitvista.com/property-type/jungle-view/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    jungle_view_title_data = df_jungle_view_title['Title'].tolist()
    print("Success scraped jungle view title data")
    # Retrieve address data
    df_jungle_view_address = scrape_data('https://www.bukitvista.com/property-type/jungle-view/page', '', 'd-flex align-items-center h-100', 'Address', 'address', {'class': 'item-address'}, 1, 10)
    jungle_view_address_data = df_jungle_view_address['Address'].tolist()
    print("Success scraped jungle view address data")
    # Retrieve price data
    df_jungle_view_price = scrape_data('https://www.bukitvista.com/property-type/jungle-view/page', '', 'd-flex align-items-center h-100', 'Price', 'li', {'class': 'item-price item-price-text'}, 1, 10)
    jungle_view_price_data = df_jungle_view_price['Price'].tolist()
    print("Success scraped jungle view price data")
    # Retrieve bedroom data
    df_jungle_view_bedroom = scrape_data('https://www.bukitvista.com/property-type/jungle-view/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    jungle_view_bedroom_data = df_jungle_view_bedroom['Bedroom'].tolist()
    print("Success scraped jungle view bedroom data")
    # Retrieve bathroom data
    df_jungle_view_bathroom = scrape_data('https://www.bukitvista.com/property-type/jungle-view/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    jungle_view_bathroom_data = df_jungle_view_bathroom['Bathroom'].tolist()
    print("Success scraped jungle view bathroom data")
    
    # Retrieve title data
    df_ocean_view_title = scrape_data('https://www.bukitvista.com/property-type/ocean-view/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    ocean_view_title_data = df_ocean_view_title['Title'].tolist()
    print("Success scraped ocean view title data")
    # Retrieve address data
    df_ocean_view_address = scrape_data('https://www.bukitvista.com/property-type/ocean-view/page', '', 'd-flex align-items-center h-100', 'Address', 'address', {'class': 'item-address'}, 1, 10)
    ocean_view_address_data = df_ocean_view_address['Address'].tolist()
    print("Success scraped ocean view address data")
    # Retrieve price data
    df_ocean_view_price = scrape_data('https://www.bukitvista.com/property-type/ocean-view/page', '', 'd-flex align-items-center h-100', 'Price', 'li', {'class': 'item-price item-price-text'}, 1, 10)
    ocean_view_price_data = df_ocean_view_price['Price'].tolist()
    print("Success scraped ocean view price data")
    # Retrieve bedroom data
    df_ocean_view_bedroom = scrape_data('https://www.bukitvista.com/property-type/ocean-view/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    ocean_view_bedroom_data = df_ocean_view_bedroom['Bedroom'].tolist()
    print("Success scraped ocean view bedroom data")
    # Retrieve bathroom data
    df_ocean_view_bathroom = scrape_data('https://www.bukitvista.com/property-type/ocean-view/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    ocean_view_bathroom_data = df_ocean_view_bathroom['Bathroom'].tolist()
    print("Success scraped ocean view bathroom data")
    
    # Retrieve title data
    df_residential_title = scrape_data('https://www.bukitvista.com/property-type/residential/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    residential_title_data = df_residential_title['Title'].tolist()
    print("Success scraped residential title data")
    # Retrieve address data
    df_residential_address = scrape_data('https://www.bukitvista.com/property-type/residential/page', '', 'd-flex align-items-center h-100', 'Address', 'address', {'class': 'item-address'}, 1, 10)
    residential_address_data = df_residential_address['Address'].tolist()
    print("Success scraped residential address data")
    # Retrieve price data
    df_residential_price = scrape_data('https://www.bukitvista.com/property-type/residential/page', '', 'd-flex align-items-center h-100', 'Price', 'li', {'class': 'item-price item-price-text'}, 1, 10)
    residential_price_data = df_residential_price['Price'].tolist()
    print("Success scraped residential price data")
    # Retrieve bedroom data
    df_residential_bedroom = scrape_data('https://www.bukitvista.com/property-type/residential/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    residential_bedroom_data = df_residential_bedroom['Bedroom'].tolist()
    print("Success scraped residential bedroom data")
    # Retrieve bathroom data
    df_residential_bathroom = scrape_data('https://www.bukitvista.com/property-type/residential/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    residential_bathroom_data = df_residential_bathroom['Bathroom'].tolist()
    print("Success scraped residential bathroom data")
    
    # Retrieve title data
    df_rice_paddy_view_title = scrape_data('https://www.bukitvista.com/property-type/rice-paddy-view/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    rice_paddy_view_title_data = df_rice_paddy_view_title['Title'].tolist()
    print("Success scraped rice paddy view title data")
    # Retrieve address data
    df_rice_paddy_view_address = scrape_data('https://www.bukitvista.com/property-type/rice-paddy-view/page', '', 'd-flex align-items-center h-100', 'Address', 'address', {'class': 'item-address'}, 1, 10)
    rice_paddy_view_address_data = df_rice_paddy_view_address['Address'].tolist()
    print("Success scraped rice paddy view address data")
    # Retrieve price data
    df_rice_paddy_view_price = scrape_data('https://www.bukitvista.com/property-type/rice-paddy-view/page', '', 'd-flex align-items-center h-100', 'Price', 'li', {'class': 'item-price item-price-text'}, 1, 10)
    rice_paddy_view_price_data = df_rice_paddy_view_price['Price'].tolist()
    print("Success scraped rice paddy view price data")
    # Retrieve bedroom data
    df_rice_paddy_view_bedroom = scrape_data('https://www.bukitvista.com/property-type/rice-paddy-view/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    rice_paddy_view_bedroom_data = df_rice_paddy_view_bedroom['Bedroom'].tolist()
    print("Success scraped rice paddy view bedroom data")
    # Retrieve bathroom data
    df_rice_paddy_view_bathroom = scrape_data('https://www.bukitvista.com/property-type/rice-paddy-view/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    rice_paddy_view_bathroom_data = df_rice_paddy_view_bathroom['Bathroom'].tolist()
    print("Success scraped rice paddy view bathroom data")
    
    # Yogyakarta Vacation Rentals
    
    # Retrieve title data
    df_yogyakarta_title = scrape_data('https://www.bukitvista.com/villa-jogja/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    yogyakarta_title_data = df_yogyakarta_title['Title'].tolist()
    print("Success scraped yogyakarta title data")
    # Retrieve address data
    df_yogyakarta_address = scrape_data('https://www.bukitvista.com/villa-jogja/page', 'https://www.bukitvista.com/property/', 'd-flex align-items-center h-100', 'Address', 'h2', {'class': 'item-title'}, 1, 10)
    yogyakarta_address_data = df_yogyakarta_address['Address'].tolist()
    print("Success scraped yogyakarta address data")
    # Retrieve price data
    df_yogyakarta_price = scrape_data('https://www.bukitvista.com/villa-jogja/page', '', 'd-flex align-items-center h-100', 'Price', 'span', {'class': 'item-price-text'}, 1, 10)
    yogyakarta_price_data = df_yogyakarta_price['Price'].tolist()
    print("Success scraped yogyakarta price data")
    # Retrieve bedroom data
    df_yogyakarta_bedroom = scrape_data('https://www.bukitvista.com/villa-jogja/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    yogyakarta_bedroom_data = df_yogyakarta_bedroom['Bedroom'].tolist()
    print("Success scraped yogyakarta bedroom data")
    # Retrieve bathroom data
    df_yogyakarta_bathroom = scrape_data('https://www.bukitvista.com/villa-jogja/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    yogyakarta_bathroom_data = df_yogyakarta_bathroom['Bathroom'].tolist()
    print("Success scraped yogyakarta bathroom data")
    
    # Nusa Penida Vacation Rentals
    
    # Retrieve title data
    df_nusa_penida_title = scrape_data('https://www.bukitvista.com/nusa-penida-vacation-rentals/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    nusa_penida_title_data = df_nusa_penida_title['Title'].tolist()
    print("Success scraped nusa penida title data")
    # Retrieve address data
    df_nusa_penida_address = scrape_data('https://www.bukitvista.com/nusa-penida-vacation-rentals/page', 'https://www.bukitvista.com/property/', 'd-flex align-items-center h-100', 'Address', 'h2', {'class': 'item-title'}, 1, 10)
    nusa_penida_address_data = df_nusa_penida_address['Address'].tolist()
    print("Success scraped nusa penida address data")
    # Retrieve price data
    df_nusa_penida_price = scrape_data('https://www.bukitvista.com/nusa-penida-vacation-rentals/page', '', 'd-flex align-items-center h-100', 'Price', 'span', {'class': 'item-price-text'}, 1, 10)
    nusa_penida_price_data = df_nusa_penida_price['Price'].tolist()
    print("Success scraped nusa penida price data")
    # Retrieve bedroom data
    df_nusa_penida_bedroom = scrape_data('https://www.bukitvista.com/nusa-penida-vacation-rentals/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    nusa_penida_bedroom_data = df_nusa_penida_bedroom['Bedroom'].tolist()
    print("Success scraped nusa penida bedroom data")
    # Retrieve bathroom data
    df_nusa_penida_bathroom = scrape_data('https://www.bukitvista.com/nusa-penida-vacation-rentals/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    nusa_penida_bathroom_data = df_nusa_penida_bathroom['Bathroom'].tolist()
    print("Success scraped nusa penida bathroom data")
    
    # Bali Long Term Rentals
    
    # Retrieve title data
    df_bali_long_term_title = scrape_data('https://www.bukitvista.com/bali-long-term-rentals/page', '', 'd-flex align-items-center h-100', 'Title', 'h2', {'class': 'item-title'}, 1, 10)
    bali_long_term_title_data = df_bali_long_term_title['Title'].tolist()
    print("Success scraped bali long term title data")
    # Retrieve address data
    df_bali_long_term_address = scrape_data('https://www.bukitvista.com/bali-long-term-rentals/page', 'https://www.bukitvista.com/property', 'd-flex align-items-center h-100', 'Address', 'h2', {'class': 'item-title'}, 1, 10)
    bali_long_term_address_data = df_bali_long_term_address['Address'].tolist()
    print("Success scraped bali long term address data")
    # Retrieve price data
    df_bali_long_term_price = scrape_data('https://www.bukitvista.com/bali-long-term-rentals/page', '', 'd-flex align-items-center h-100', 'Price', 'li', {'class': 'item-price'}, 1, 10)
    bali_long_term_price_data = df_bali_long_term_price['Price'].tolist()
    print("Success scraped bali long term price data")
    # Retrieve bedroom data
    df_bali_long_term_bedroom = scrape_data('https://www.bukitvista.com/bali-long-term-rentals/page', '', 'd-flex align-items-center h-100', 'Bedroom', 'span', {'class': 'hz-figure'}, 1, 10)
    bali_long_term_bedroom_data = df_bali_long_term_bedroom['Bedroom'].tolist()
    print("Success scraped bali long term bedroom data")
    # Retrieve bathroom data
    df_bali_long_term_bathroom = scrape_data('https://www.bukitvista.com/bali-long-term-rentals/page', '', 'd-flex align-items-center h-100', 'Bathroom', 'span', {'class': 'hz-figure'}, 1, 10)
    bali_long_term_bathroom_data = df_bali_long_term_bathroom['Bathroom'].tolist()
    print("Success scraped bali long term bathroom data")
    
    
    # Combine data into a single response
    response = {
        'Title': beachfront_title_data + island_life_title_data + jungle_view_title_data + ocean_view_title_data + residential_title_data + rice_paddy_view_title_data + yogyakarta_title_data + nusa_penida_title_data + bali_long_term_title_data,
        'Address': beachfront_address_data + island_life_address_data + jungle_view_address_data + ocean_view_address_data + residential_address_data + rice_paddy_view_address_data + yogyakarta_address_data + nusa_penida_address_data + bali_long_term_address_data,
        'Price': beachfront_price_data + island_life_price_data + jungle_view_price_data + ocean_view_price_data + residential_price_data + rice_paddy_view_price_data + yogyakarta_price_data + nusa_penida_price_data + bali_long_term_price_data,
        'Bedroom': beachfront_bedroom_data + island_life_bedroom_data + jungle_view_bedroom_data + ocean_view_bedroom_data + residential_bedroom_data + rice_paddy_view_bedroom_data + yogyakarta_bedroom_data + nusa_penida_bedroom_data + bali_long_term_bedroom_data,
        'Bathroom': beachfront_bathroom_data + island_life_bathroom_data + jungle_view_bathroom_data + ocean_view_bathroom_data + residential_bathroom_data + rice_paddy_view_bathroom_data + yogyakarta_bathroom_data + nusa_penida_bathroom_data + bali_long_term_bathroom_data
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
