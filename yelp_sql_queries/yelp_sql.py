# Final SQL queries integrated with Django
'''
Cuisines search:
- Get top cities for a cuisine

City search:
- top cuisines for a city
- average reviews per restaurant for each star category
- average ratings and avg reviews/restaurant per price bracket
- all cuisines in a city
- cuisines ranked by # restaurants
'''

import sqlite3
import csv
import string
import math
import statistics as stat

def get_top_cities(query, database = "yelp_adjusted.db"):
    '''
    Returns top cities for a cuisine, normalized by avg city ratings so that
    reviews across cities are comparable

    Required: cuisine
    Optional: limit of # cities returned (default 10)

    Inputs:
        - query (dict): maps city name to all available cuisines
            example query:
            query = {"cuisine": "Mexican",
                     "limit": 20}

    Output:
        - list of lists
          [0]: city name
          [1]: average rating
          [2]: number of restaurants of that cuisine in the city
    '''

    connection = sqlite3.connect(database)
    c = connection.cursor()
    
    search_string = '''SELECT city, AVG(rating) as avg_rating, 
    COUNT(*) as num_restaurants 
    FROM restaurant
    JOIN cuisines
    ON restaurant.id = cuisines.id
    WHERE cuisines.cuisine = ?
    COLLATE NOCASE
    GROUP BY city
    '''
    
    params = []
    cuisine = query["cuisine"]
    params.append(cuisine)

    results = c.execute(search_string, params)
    result_table = results.fetchall()

    connection.commit()
    c.connection.close()

    result_table.sort(key = lambda x: x[1], reverse = True)

    if "limit" in query:
        limit = query["limit"]
    else:
        limit = 10
    
    result_table = result_table[:limit]
    result_list = []
    for result in result_table:
        result = list(result)
        result[1] = round(result[1], 2)
        result[0] = result[0].title()
        result_list.append(result)

    return result_list
        
    
def get_top_cuisines(query, database = "yelp_raw.db"):
    '''
    Get top cuisines for a city (or worst if "worse" is specified), 
    restricts to restaurants with >= 5 reviews and cuisines with >= 10 restaurants
    
    Required: city name, price ceiling, limit of # cuisines returned (default 10), 
        worst (boolean specifying best or worst cuisines)

    Inputs:
        - query (dict): maps possible queries (city, price) to list of user inputs
          example_query = {"city": "chicago",
                           "price": "$$$",
                           "limit": 10,
                           "worst": True}

    Ouput:
        - list of lists, each entry is one cuisine type
    '''

    connection = sqlite3.connect(database)
    c = connection.cursor()

    search_string = '''SELECT cuisine, AVG(price) as avg_price, AVG(rating) as avg_rating, 
    COUNT(*) as num_restaurants, SUM(reviews) as num_reviews
    FROM restaurant
    JOIN cuisines
    ON restaurant.id = cuisines.id
    WHERE city = ?
    COLLATE NOCASE
    '''
    
    params = []
    city = query["city"].lower()
    params.append(city)

    # If user specified price ceiling, adjusts table to return cuisines
    # below this average price
    if "price" in query:
        search_string += '''AND price <= ?'''
        price_length = len(query["price"])
        params.append(price_length)

    search_string += '''
    GROUP BY cuisine;
    '''
    
    results = c.execute(search_string, params)
    result_table = results.fetchall()

    connection.commit()
    c.connection.close()

    if query["worst"]:
        result_table.sort(key = lambda x: x[2])
    else:
        result_table.sort(key = lambda x: x[2], reverse = True)

    if "limit" in query:
        limit = query["limit"]
    else:
        limit = 10

    result_list = format_cuisine_table(limit, result_table)

    return result_list


def format_cuisine_table(limit, result_table):
    '''
    Formats prices and ensures cuisines have > 10 restaurants
    '''

    format_price_table = []
    count = 0
    
    for entry in result_table:
        # Turns prices from floats (rounded up since they will always be capped by 
        # price ceiling) to dollar sign characters
        entry = list(entry)
        entry[1] = math.ceil(entry[1]) * "$"
        entry[2] = round(entry[2], 2)
        entry[0] = entry[0].title()

        # Restricts to cuisines with > 10 restaurants
        if entry[3] > 10 and count < limit:
            format_price_table.append(entry)
            count += 1

    return format_price_table


def star_reviews(query, database = "yelp_raw.db"):
    '''
    Gets avg reviews per restaurant for each star category for a city

    Inputs:
        - query (dict): contains desired city name
            example query:
            query = {"city": "chicago"}
        - database

    Output:
        - list of lists: 
          [0]: rating
          [1]: # restaurants
          [2]: avg # reviews / restaurant]
    '''

    connection = sqlite3.connect(database)
    c = connection.cursor()
    
    search_string = '''SELECT rating, COUNT(*) as num_restaurants, SUM(reviews) as num_reviews
    FROM restaurant
    WHERE city = ?
    COLLATE NOCASE
    AND reviews > 10
    GROUP BY rating
    '''
    
    params = []
    city = query["city"]
    params.append(city)

    results = c.execute(search_string, params)
    result_table = results.fetchall()

    connection.commit()
    c.connection.close()

    # Gets average # reviews per restaurant
    for index, result in enumerate(result_table):
        avg_num_reviews = result[2] / result[1]
        avg_num_reviews = round(avg_num_reviews, 2)
        result_table[index] = [result[0], result[1], avg_num_reviews]

    return result_table


def price_ratings(query, database = "yelp_raw.db"):
    '''
    Gets avg ratings for each price category for a city

    Inputs:
        - query (dict): contains desired city name
            example query:
            query = {"city": "chicago"}
        - database

    Output:
        - list of lists
          [0]: price
          [1]: avg rating
          [2]: # restaurants
          [3]: avg # reviews / restaurant]
        '''

    connection = sqlite3.connect(database)
    c = connection.cursor()
    
    search_string = '''SELECT price, AVG(rating) as avg_rating, 
    COUNT(*) as num_restaurants, SUM(reviews) as num_reviews
    FROM restaurant
    WHERE city = ?
    COLLATE NOCASE
    AND reviews > 10
    GROUP BY price
    '''
    
    params = []
    city = query["city"]
    params.append(city)

    results = c.execute(search_string, params)
    result_table = results.fetchall()

    format_price_table = []

    for entry in result_table:
        if entry[0]:
            # Turns price from float to $
            price = math.ceil(float(entry[0])) * "$"
            format_price_table.append([price, entry[1], entry[2], entry[3] / entry[2]])

    connection.commit()
    c.connection.close()

    return format_price_table


def all_cuisines(query, database = "yelp_adjusted.db"):
    '''
    Get all cuisine types with >= 10 restaurants for a city from database

    Inputs:
        - query (dict): maps city name to all available cuisines
            example query:
            query = {"city": "chicago"}
        - database

    Output:
        - alphabetized list of cuisines
    '''

    connection = sqlite3.connect(database)
    c = connection.cursor()
    
    search_string = '''SELECT DISTINCT cuisine, COUNT(*) as num_restaurants
    FROM cuisines
    JOIN restaurant
    ON restaurant.id = cuisines.id
    WHERE city = ?
    COLLATE NOCASE
    GROUP BY cuisine
    '''
    
    params = []
    city = query["city"]
    params.append(city)

    results = c.execute(search_string, params)
    result_table = results.fetchall()
    cuisine_table = []

    # Take out of form [("cuisine",)] to form ['cuisine']
    for result in result_table:
        print(result)
        if result[1] >= 10:
            cuisine_table.append(result[0])

    connection.commit()
    c.connection.close()

    return sorted(cuisine_table)


def common_cuisines(query, database = "yelp_adjusted.db"):
    '''
    Returns most common cuisines with ratings

    Inputs:
        - query (dict): maps city name to all available cuisines
            example query:
            query = {"city": "Los Angeles"}

    Output:
        - list of lists of sorted most common cuisines
    '''

    connection = sqlite3.connect(database)
    c = connection.cursor()
    
    search_string = '''SELECT cuisine, AVG(rating) as avg_rating, 
    COUNT(*) as num_restaurants 
    FROM restaurant
    JOIN cuisines
    ON restaurant.id = cuisines.id
    WHERE city = ?
    COLLATE NOCASE
    GROUP BY cuisine
    '''
    
    params = []
    city = query["city"].lower()
    params.append(city)

    results = c.execute(search_string, params)
    result_table = results.fetchall()

    connection.commit()
    c.connection.close()
    
    full_result_list = []
    result_list = []

    for result in result_table:
        result = list(result)
        result[1] = round(result[1], 2)
        full_result_list.append(result)
        result_list.append(result[1:])
    full_result_list.sort(key = lambda x: x[2], reverse = True)
    result_list.sort(key = lambda x: x[1], reverse = True)

    return full_result_list[:5], result_list[:10]