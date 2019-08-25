
# Dependencies 
import os
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd
import requests
import pymongo

def init_browser():
        # @NOTE: Replace the path with your actual path to the chromedriver
        executable_path = {"executable_path": "C:/Users/Nader/OneDrive/Education/SMU Data Science/Web Scrapper/Web_Scrapper_HW/chromedriver"}
        return Browser("chrome", **executable_path, headless=False)

def scrape_info():

        
        browser = init_browser()
        url_mars = 'https://mars.nasa.gov/news/'
        browser.visit(url_mars)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        #Save data in object
        news = soup.find("div", class_="list_text")
        news_headline = news.find("div", class_="content_title").text
        news_body = news.find("div", class_="article_teaser_body").text
        news_date = news.find("div", class_="list_date").text

        print(f"News Headline: {news_headline}")
        print(f"Context: {news_body}")
        print(f"Date release: {news_date}")

        url_JPL = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url_JPL)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        mars_image = soup.find("article", class_="carousel_item")
        mars_image

        url_weather = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(url_weather)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        weather_tweet = soup.find("p", class_= "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
        print(f"Latest Tweet: {weather_tweet}")

        url = 'https://space-facts.com/mars/'
        tables = pd.read_html(url)

        df = tables[0]
        del df['Earth']
        df.columns = ['Parameters', 'Mars']
        df

        html_table = df.to_html()
        html_table

        url_image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'

        url_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url_hemispheres)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        hemispheres = soup.find_all("div", class_="item")

        hemi_titles = []
        hemi_url = ['https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
            'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
            'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
            'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',
           ]
        hemisphere_image_urls = {}

        for title in hemispheres:
                try:
                        hemispheres_title = title.find("h3").text
                        if(hemispheres_title):
                                hemi_titles.append(hemispheres_title)
                except AttributeError as e:
                        print(e)

        hemisphere_image_urls["title"] = hemi_titles
        hemisphere_image_urls["img_url"] = hemi_url
        hemisphere_image_urls

        hemisphere_image_urls = {"title": hemi_titles,"img_url": hemi_url}

        return hemisphere_image_urls