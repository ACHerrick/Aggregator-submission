"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
'''
This file was originally generated by the Django framework. Url routes have been created for subpages, namely:
	- admin: an admin page for easy access of apps. For access, username is emilyding and password is cs122
	- about: an about page containing an introduction of the site and biographical information
	- overview: an "all cities" overview that is statically generated, containing facts and graphs from aggregated data across all cities.
        - topcuisines: a ranked list of cuisines.
	- form: a form to specify city, price range, etc. for aggregation. 
	- results: follows form submission, gives a snapshot with facts and graphs of specified city.
	- compare: a form to all comparison of two cities.
	- cresults: follws compare submission, gives graph and facts comparing two cities.
	- cuisine: allows lookup of a cuisine to find top cities for cuisine
        - cuiresults: follows submissions of cuisine page, gives graphs of top cities for cuisine.	
'''

from django.conf.urls import include, url
from django.contrib import admin
from myapp import views as v

urlpatterns = [
    url(r'^$', v.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', v.about),
    url(r'^overview/', v.overview),
    url(r'^topcuisines/',v.top_cuisines, name="Top Cuisines"),
    url(r'^form/', v.form, name="City Aggregator"),
    url(r'^results/',v.results, name="Results"),
    url(r'^compare/', v.compare),
    url(r'^cresults/',v.cresults, name="City Compare Results"),
    url(r'^cuisine/', v.cuisine),
    url(r'^cuiresults/',v.cuiresults, name="Cuisine Results"),  
]
