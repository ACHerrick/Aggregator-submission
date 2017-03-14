# Scrapes Tripadvisor restaurant page for data

'''
Code in this file scrapes all of the desired information (name, rating, price, address,
city, state, zipcode, country, phone #) on Tripadvisor. We did not use this in our final 
implementation because of difficulties building a crawler, and thus this code was discontinued.
'''

import requests
import re
import bs4

def go():
    '''
    Return restaurant info
    '''
    url = "https://www.tripadvisor.com/Restaurant_Review-g35805-d7200288-Reviews-Shake_Shack-Chicago_Illinois.html"
    soup = cook_soup(url)
    restaurant_info = get_info(soup)
    return restaurant_info


def cook_soup(url):
    '''
    Create Beautiful Soup object from url
    '''
    request = requests.get(url)
    encoding = request.encoding
    html = request.text.encode(encoding)
    soup = bs4.BeautifulSoup(html, "html5lib")

    return soup


def get_info(soup):
    '''
    Pulls name, rating, price, cuisine tags, address, city, state, country, zipcode,
    and phone number from page. Return in form of dictionary.
    '''
    name_tag = soup.find_all('h1', property = "name")
    name = name_tag[0].text
    name = name.replace("\n", "")

    rating_tag = soup.find_all('img', property = "ratingValue")
    rating = rating_tag[0]["content"]

    price_tag = soup.find_all('div', class_ = "detail first price_rating separator")
    price = price_tag[0].text
    price = price.replace("\n", "")

    cuisine_all = soup.find_all('div', class_ = "detail separator")
    cuisine_tags = cuisine_all[0].find_all('a')
    cuisine = []
    for cuisine_tag in cuisine_tags:
        cuisine.append(cuisine_tag.text)

    address_tag = soup.find_all('span', property = "streetAddress")
    address = address_tag[0].text

    city_tag = soup.find_all('span', property = "addressLocality")
    city = city_tag[0].text

    state_tag = soup.find_all('span', property = "addressRegion")
    state = state_tag[0].text

    country_tag = soup.find_all('span', property = "addressCountry")
    country = country_tag[0]["content"]

    zipcode_tag = soup.find_all('span', property = "postalCode")
    zipcode = zipcode_tag[0].text

    phone_tag = soup.find_all('div', class_ = "fl phoneNumber")
    phone = phone_tag[0].text
    phone = re.findall("[0-9-]{12}", phone)
    phone = phone[0].replace("-", "")
    # returns in form 3126671701

    restaurant_info = {
    "name": name,
    "rating": rating,
    "price": price
    "cuisine": cuisine
    "address": address, 
    "city": city,
    "state": state, 
    "zipcode": zipcode,
    "country": country,
    "phone": phone
    }

    return restaurant_info