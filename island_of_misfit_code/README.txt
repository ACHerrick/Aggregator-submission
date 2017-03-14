\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\##############################\
\### Island of Misift Code ####\
\##############################\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Files in this folder represent code that was attempted at various points in
time but was ultimately abandoned as being ineffective (or was never intended
for final use) 

.py files:
distance_finder_but_the_one_that_doesnt_work.py
fake_data_generation.py
fake_sql_calling.py
fake_sql_generation.py
tripadvisor_scrape.py
yelp_sql_graph.py

distance_finder_but_the_one_that_doesnt_work.py: This file contains an initial
attempt to design an effective algorithm for computing Starbucks distances in
better than n^2 time.

The 3 fake_[word]_[word].py files were used for testing purposes before real
data was obtained and were never intended to be part of the final product. These
files generate fake data, create a SQL database from it, and run some simple calls

tripadvisor_scrape.py: Code in this file scrapes all of the desired information from 
a restaurant page on Tripadvisor. We did not use this because of difficulties building
a crawler, and thus this code was discontinued.

yelp_sql_graph.py: Code in this file contains all functions that are in our website, 
and generates graphs for the functions using matplotlib. We did not use this because 
of difficulties dynamically generating graphs to be displayed on Django, so we created 
graphs using Google. However, this code can be used to generate graphs using MATPLOTLIB.
