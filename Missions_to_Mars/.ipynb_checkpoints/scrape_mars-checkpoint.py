from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_mars_news():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # mars news site url
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)
    
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")
    
    news_title = soup.find('div', class_='content_title').text
    
    news_p = soup.find('div', class_='article_teaser_body').text
    
    browser.quit()
    
    # mars space image site
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)
    
    relative_image_path = soup.find_all('img')[1]['src']
    featured_image_url = image_url + relative_image_path
              
    browser.quit() 
    # # mars facts site
    # facts_url = 'https://galaxyfacts-mars.com/'
    # browser.visit(facts_url)
    
    # tables = pd.read_html(facts_url)
    
    # facts_df = tables[0]
    # facts_df.columns = ['Category','Measurement', 'Measurement']
    # html_table = facts_df.to_html()
    # cleaned_html_table = html_table.replace('\n', '')
    
    # # high res site
    
    # high_res_url = 'https://marshemispheres.com/'
    # browser.visit(high_res_url)
    
    # high_res_html = browser.html
    # soup = bs(high_res_html, "html.parser")
    
    # nextpage_urls = []
    # imgtitles = []
    # base_url = 'https://marshemispheres.com/'

    # # HTML object
    # html = browser.html
    # # Parse HTML with Beautiful Soup
    # soup = bs(html, 'html.parser')
    # # Retrieve all elements that contain hemisphere photo info
    # divs = soup.find_all('div', class_='description')

    # # Iterate through each div to pull titles and make list of hrefs to iterate through
    # counter = 0
    # for div in divs:
    #     # Use Beautiful Soup's find() method to navigate and retrieve attributes
    #     link = div.find('a')
    #     href=link['href']
    #     img_title = div.a.find('h3')
    #     img_title = img_title.text
    #     imgtitles.append(img_title)
    #     next_page = base_url + href
    #     nextpage_urls.append(next_page)
    #     counter = counter+1
    #     if (counter == 4):
    #         break
    
    # my_images=[]
    # for nextpage_url in nextpage_urls:
    #     url = nextpage_url
    #     browser.visit(url)
    #     html = browser.html
    #     soup = bs(html, 'html.parser')
    #     link2 = soup.find('img', class_="wide-image")
    #     forfinal = link2['src']
    #     full_img = base_url + forfinal
    #     my_images.append(full_img)
    #     nextpage_urls = []
            
    
    # hemisphere_image_urls = []

    # cerberus = {'title':imgtitles[0], 'img_url': my_images[0]}
    # schiaparelli = {'title':imgtitles[1], 'img_url': my_images[1]}
    # syrtis = {'title':imgtitles[2], 'img_url': my_images[2]}
    # valles = {'title':imgtitles[3], 'img_url': my_images[3]}

    # hemisphere_image_urls = [cerberus, schiaparelli, syrtis, valles]
    
    mars_data = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url,
        # 'cleaned_html_table': cleaned_html_table,
        # 'hemisphere_image_urls': hemisphere_image_urls      
       }
    
    browser.quit()
    
    return mars_data
    
    