\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\###############################\
\### ACE Cuisine Aggregator ####\
\###############################\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Welcome the ACE Cuisine Aggregator! 

If you have ever wondered how food in Boston compares to food in New York (New 
York is better), or what the best city is for Chinese food (Kansas City), wonder 
no longer! This ReadMe will help you navigate through our code folders as conveniently
as possible, so that you can stop puzzling over documents and start learning about
cuisines as easily as possible. 

Firstly, this project contains 5 folders, each containing a different section of 
code.

django_code: This folder contains the code necessary to run the website itself,
and execute the code which produces our dynamic graphs. Some code is copied from
other parts of our project as necessary in order to ensure smooth functionality.

island_of_misfit_code: This folder contains scraps of code that were not used in
the final product, either because they were made obselete or because they did not
effectively accomplish their original goal.

yelp_data_collection: This folder contains the code used to gather city-level data
from Yelp using an API, aggregate that data into a single large spreadsheet, and
load the data into two SQL databases (one mean-adjusted and one unweighted). Code 
is also included to scrape information on Starbucks and compute the median min
distance index for cities.

yelp_sql_queries: This folder contains the code used to query the SQL databases
and extract the data necessary to produce the graphs seen on the website. Some of
these functions contain code to make graphs as well through matplotlib, but the
displayed graphs are instead created with JavaScript through Google Charts. 

zagat_linkage: This folder contains the code used to scrape zagat code for Chicago
and link restaurants from there with Chicago Yelp data in order to test for
discrepencies in their average ratings. 

Running the server, and viewing interesting aggregated data, requires use of the
django_code folder primarily (further instructions provided inside). To easily answer
questions not explicitly shown through the website, use the yelp_sql_queries folder, as
code there can more easily be modified to answer new questions. 

To add cities to the databases, or to begin with a new dataset, use the yelp_data_collection
folder. Instructions in that folder's ReadMe explain how to do this easily.
(Appending new data, however, will require unzipping the existing city files)


API Keys for Yelp:
app_id = 'rVkxCbS3vszyTTHgSdPRJA'
app_secret = 'xB5UJmXyLKyYTO4uKUl1TluKTGiiCnYnaCjCiv2dyvSc6Jfuh0s1xm4g27NbNZRA'

API Keys for Zagat: (Choose one, though they might sometimes be banned)
API = "AIzaSyCP58u53oJ_brOYoNkF0ktaCE2EyZaJIyA"
API = "AIzaSyDW15a3LCSe7J1YDRvUMWR1IsVlMxqQtRU"
API = "AIzaSyB28WD_QVBYhUlO3fr22uMNr2zemUA7ZyQ"
API = "AIzaSyCkSm8tFiiEFSoXc9ixXNLlMD0N3O52sno"
API = "AIzaSyDLWHjPZycWPeYui9yg2AM0own1IaVHIFc"


Note: Outside of necessary Django packages, the only neccesary import installation
(beyond Python defaults) is sklearn, which requires scipy as a prerequisite. This is
used for data gathering (i.e, not required to run the website) to compute Starbucks 
distances efficiently.