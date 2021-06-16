# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo
import time
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {"executable_path":ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

    # mars news site url
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)
    
    time.sleep(1)

    html = browser.html
    news_soup = bs(html, "html.parser")
    
    news_title = news_soup.find('div', class_='content_title').text
    
    news_p = news_soup.find('div', class_='article_teaser_body').text
    
    
    
    # mars space image site
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    image_html = browser.html
    image_soup = bs(image_html, "html.parser")
        
    relative_image_path = image_soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = image_url + relative_image_path
              
    
    # mars facts site
    facts_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(facts_url)[0]
    
    tables.columns = ['Category','Measurement', 'Measurement']
    tables.set_index('Category', inplace=True)
    html_table = tables.to_html()
    html_table.replace('n', '')
    
    # # high res site
    
    # Mars hemisphere name and image to be scraped
    hemispheres_url = "https://marshemispheres.com/"
    browser.visit(hemispheres_url)
    hemispheres_html = browser.html
    hemispheres_soup = bs(hemispheres_html, 'html.parser')
    # Mars hemispheres products data
    all_mars_hemispheres = hemispheres_soup.find('div', class_='collapsible results')
    mars_hemispheres = all_mars_hemispheres.find_all('div', class_='item')
    hemisphere_image_urls = []
    # Iterate through each hemisphere data
    for i in mars_hemispheres:
        # Collect Title
        hemisphere = i.find('div', class_="description")
        title = hemisphere.h3.text        
        # Collect image link by browsing to hemisphere page
        hemisphere_link = hemisphere.a["href"]    
        browser.visit(hemispheres_url + hemisphere_link)        
        image_html = browser.html
        image_soup = bs(image_html, 'html.parser')        
        image_link = image_soup.find('div', class_='downloads')
        image_url = image_link.find('li').a['href']
        # Create Dictionary to store title and url info
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = hemispheres_url+image_url        
        hemisphere_image_urls.append(image_dict)
        # Mars 
    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "fact_table": str(html_table),
        "hemisphere_images": hemisphere_image_urls
    }

    return mars_dict