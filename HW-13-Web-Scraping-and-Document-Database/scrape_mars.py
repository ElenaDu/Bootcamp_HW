import requests
from bs4 import BeautifulSoup
from splinter import Browser
import time
import pandas as pd




def scrape():
    
    '''executes scraping data and return one Python dictionary containing all of the scraped data.'''
    mars_data={}

     # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text

    url1="https://mars.nasa.gov/news/" 
    response=requests.get(url1)
     # Create BeautifulSoup object; parse with 'lxml'
    soup=BeautifulSoup(response.text, 'lxml')
     #collect the latest News Title and Paragraph Text
    news_title=soup.find('div', class_='content_title').a.text
    mars_data['news_title']=news_title
    news_p=soup.find('div', class_='rollover_description_inner') .text               
    mars_data['news_par']=news_p

    #Use splinter to navigate www.jpl.nasa.gov and find the image url for the current Featured Mars Image.
    url2="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url2)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    # Parse HTML with Beautiful Soup
    html=browser.html
    soup=BeautifulSoup(html,'lxml')
    #Use Beautiful Soup's find() method to navigate and retrieve attribute
    img_link=soup.find('img', class_="main_image")['src']
    #save a complete url string for this image
    featured_image_url="https://www.jpl.nasa.gov"+img_link
    mars_data['featured_image_url']=featured_image_url

    #Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page.
    #Retrieve page with the requests module
    url3='https://twitter.com/marswxreport?lang=en'
    response=requests.get(url3)
    #Create BeautifulSoup object; parse with 'lxml'
    soup=BeautifulSoup(response.text, 'lxml')
    #find all tweets on the page
    mars_tweets=soup.find_all('p', class_='js-tweet-text')
    #since this page contains other tweets related to Mars weather, try to find the first tweet with 'Sol ' substring.
    for tweet in mars_tweets:
        try:
            p_tweet=tweet.text
            if p_tweet.find('Sol ')!=-1:
                mars_weather=p_tweet
                mars_data['mars_weather']=mars_weather
                break
        except AttributeError as e:
            print(e)

    #Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet.
    url4='https://space-facts.com/mars/'
    # We can use the read_html function in Pandas to automatically scrape any tabular data from a page.
    tables=pd.read_html(url4)
    df=tables[0]
    df.set_index(0, inplace=True)
    #use to_html method to generate HTML tables from DataFrames.
    html_table=df.to_html(header=False)
    mars_data['html_table']=html_table

    #Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
    url5='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    html=browser.html
    # Create BeautifulSoup object; parse with 'lxml'
    soup=BeautifulSoup(html,'lxml')
    #find the text content related to hemispheres links
    div_l=soup.find_all('div', class_='description')
    h3_list=[]
    for d in div_l:
        text_h3=d.find('h3').text
        h3_list.append(text_h3)

    #click each of the links using '.click_link_by_partial_text' method to the hemispheres 
    #in order to find the image url to the full resolution image.
    hemisphere_image_urls =[]
    for h3 in h3_list:
        browser.click_link_by_partial_text(h3)
        time.sleep(2)
        #Save both the image url string for the full resolution hemisphere image, 
        #and the Hemisphere title containing the hemisphere name.
        link=browser.find_link_by_text('Sample').first
        url=link['href']
        h2=browser.find_by_css('h2').first.value

       #Use Python dictionary to store the data using the keys img_url and title
    
        if (url and h2):
            i_url={}
            i_url['title']=h2
            i_url['img_url']=url
              
            #Append the dictionary with the image url string and the hemisphere title to a list.
            #This list contains one dictionary for each hemisphere
            hemisphere_image_urls.append(i_url)   
        
        browser.back()
    mars_data['hemisphere_image_urls']=hemisphere_image_urls
    
    browser.quit()
    
    return mars_data
    