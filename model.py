import json
from transformers import pipeline
import requests
from bs4 import BeautifulSoup
summrize = pipeline("summarization", model="facebook/bart-large-cnn")


count = 0

data_list = [
    {"url": "https://techcrunch.com/",  #tech
     "uppertag": "header",
     "upperkey": "class",
     "uppervalue": "post-block__header",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "article-content",
     "imgtag": "article",
     "imgkey": "class",
     "imgvalue": "article-container article--post",
     "imgname": "src",
     "credit_name":"techcrunch",
     "domain":"Technology"},
    {"url": "https://www.indiatvnews.com/technology",  #tech
     "uppertag": "h3",
     "upperkey": "class",
     "uppervalue": "titel",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "content",
     "imgtag": "figure",
     "imgkey": "class",
     "imgvalue": "artbigimg row",
     "imgname": "data-original",
     "credit_name":"indiatvnews",
     "domain":"Technology"},
    {"url": "https://techcrunch.com/category/artificial-intelligence/",  #tech
     "uppertag": "h2",
     "upperkey": "class",
     "uppervalue": "post-block__title",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "article-content",
     "imgtag": "article",
     "imgkey": "class",
     "imgvalue": "article-container article--post",
     "imgname": "src",
     "credit_name":"techcrunch",
     "domain":"Technology"},
    {"url": "https://www.techradar.com/",  #tech
     "uppertag": "div",
     "upperkey": "class",
     "uppervalue": "wcl-item-right p-u-1-2 p-u-sm-1 p-u-md-1-2 p-u-lg-1-2",
     "lowertag": "div",
     "lowerkey": "class",
     "lowervalue": "text-copy bodyCopy auto",
     "imgtag": "div",
     "imgkey": "class",
     "imgvalue": "hero-image-padding",
     "imgname": "src",
     "credit_name":"techradar",
     "domain":"Technology"},
    # # {"url": "https://www.news18.com/sports/",  #sports
    # #  "uppertag": "div",
    # #  "upperkey": "class",
    # #  "uppervalue": "slick-slide",
    # #  "lowertag": "div",
    # #  "lowerkey": "class",
    # #  "lowervalue": "jsx-926f17af57ac97dc",
    # #  "imgtag": "figure",
    # #  "imgkey": "class",
    # #  "imgvalue": "jsx-926f17af57ac97dc",
    # #  "imgname": "src",
    # #  "credit_name":"news18",
    # #  "domain":"Sports"},

    # {"url": "https://www.moneycontrol.com/news/tags/sports.html",  #sports
    #  "uppertag": "li",
    #  "upperkey": "class",
    #  "uppervalue": "clearfix",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "content_wrapper arti-flow",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "article_image",
    #  "imgname": "data-src",
    #  "credit_name":"moneycontrol",
    #  "domain":"sports"},
    # {"url": "https://sports.ndtv.com/",  #sports
    #  "uppertag": "h3",
    #  "upperkey": "class",
    #  "uppervalue": "crd_ttl",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "story__content",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "ins_instory_dv_cont",
    #  "imgname": "src",
    #  "credit_name":"ndtv",
    #  "domain":"Sports"},
    # {"url": "https://www.nbcnews.com/sports",  #sports
    #  "uppertag": "h2",
    #  "upperkey": "class",
    #  "uppervalue": "styles_headline__ice3t",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "article-body__content",
    #  "imgtag": "picture",
    #  "imgkey": "class",
    #  "imgvalue": "article-hero__main-image",
    #  "imgname": "src",
    #  "credit_name":"nbcnews",
    #  "domain":"Sports"},
    # {"url": "https://www.marca.com/en/",     #sports
    #  "uppertag": "div",
    #  "upperkey": "class",
    #  "uppervalue": "ue-c-cover-content__main",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "ue-c-article__body",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "ue-c-article__media-img-container ue-l-article--expand-edge-right-until-tablet ue-l-article--expand-edge-left-until-tablet",
    #  "imgname": "src",
    #  "credit_name":"marca",
    #  "domain":"Sports"},
    # {"url": "https://www.ndtv.com/elections#pfrom=home-ndtv_mainnavgation",  #election
    #  "uppertag": "div",
    #  "upperkey": "class",
    #  "uppervalue": "HmCr_li",
    #  "lowertag": "div",
    #  "lowerkey": "itemprop",
    #  "lowervalue": "articleBody",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "ins_instory_dv_cont",
    #  "imgname": "src",
    #  "credit_name":"ndtv",
    #  "domain":"Election"},
    # {"url": "https://indianexpress.com/section/political-pulse/",  #election
    #  "uppertag": "h2",
    #  "upperkey": "class",
    #  "uppervalue": "title",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "ev-meter-content ie-premium-content-block",
    #  "imgtag": "span",
    #  "imgkey": "class",
    #  "imgvalue": "custom-caption",
    #  "imgname": "src",
    #  "credit_name":"indianexpress",
    #  "domain":"Election"},
    # {"url": "https://www.indiatvnews.com/topic/lok-sabha-elections-2024",  #election
    #  "uppertag": "h3",
    #  "upperkey": "class",
    #  "uppervalue": "title",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "content",
    #  "imgtag": "figure",
    #  "imgkey": "class",
    #  "imgvalue": "artbigimg row",
    #  "imgname": "data-original",
    #  "credit_name":"indiatvnews",
    #  "domain":"Election"},
    # {"url": "https://www.nbcnews.com/news/europe",     #internationl
    #  "uppertag": "h2",
    #  "upperkey": "class",
    #  "uppervalue": "styles_headline__ice3t",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "article-body__content",
    #  "imgtag": "figure",
    #  "imgkey": "class",
    #  "imgvalue": "article-hero__main",
    #  "imgname": "src",
    #  "credit_name":"nbcnews",
    #  "domain":"International"},
    # {"url": "https://www.thehindu.com/news/international/",    #internationl
    #  "uppertag": "h3",
    #  "upperkey": "class",
    #  "uppervalue": "title big",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "articlebodycontent col-xl-9 col-lg-12 col-md-12 col-sm-12 col-12",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "picture verticle",
    #  "imgname": "srcset",
    #  "credit_name":"The hindu",
    #  "domain":"International"},
    # {"url": "https://www.indiatvnews.com/world",    #internationl
    #  "uppertag": "h3",
    #  "upperkey": "class",
    #  "uppervalue": "titel",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "content",
    #  "imgtag": "figure",
    #  "imgkey": "class",
    #  "imgvalue": "artbigimg row",
    #  "imgname": "data-original",
    #  "credit_name":"indiatvnews",
    #  "domain":"International"},
    # {"url": "https://www.india.com/entertainment/",     #entertainment
    #  "uppertag": "article",
    #  "upperkey": "class",
    #  "uppervalue": "repeat-box",
    #  "lowertag": "section",
    #  "lowerkey": "class",
    #  "lowervalue": "lhs-col article-details",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "lazy-image",
    #  "imgname": "data-src",
    #  "credit_name":"india",
    #  "domain":"Entertainment"},
    # {"url": "https://globalnews.ca/entertainment/",     #entertainment
    #  "uppertag": "li",
    #  "upperkey": "class",
    #  "uppervalue": "c-posts__item c-posts__loadmore",
    #  "lowertag": "article",
    #  "lowerkey": "class",
    #  "lowervalue": "l-article__text js-story-text",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "c-figure__inner",
    #  "imgname": "src",
    #  "credit_name":"globalnews",
    #  "domain":"Entertainment"},
    # {"url": "https://www.moneycontrol.com/news/trends/entertainment/",  #entertainment
    #  "uppertag": "li",
    #  "upperkey": "class",
    #  "uppervalue": "clearfix",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "content_wrapper arti-flow",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "article_image",
    #  "imgname": "data-src",
    #  "credit_name":"moneycontrol",
    #  "domain":"Entertainment"
    #  },
    # {"url": "https://indianexpress.com/section/entertainment/",     #entertainment
    #  "uppertag": "div",
    #  "upperkey": "class",
    #  "uppervalue": "title",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "ev-meter-content ie-premium-content-block",
    #  "imgtag": "span",
    #  "imgkey": "class",
    #  "imgvalue": "custom-caption",
    #  "imgname": "src",
    #  "credit_name":"indianexpress",
    #  "domain":"Entertainment"},
    # {"url": "https://www.moneycontrol.com/news/business/economy/",  #economy
    #  "uppertag": "li",
    #  "upperkey": "class",
    #  "uppervalue": "clearfix",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "content_wrapper arti-flow",
    #  "imgtag": "div",
    #  "imgkey": "class",
    #  "imgvalue": "article_image",
    #  "imgname": "data-src",
    #  "credit_name":"moneycontrol",
    #  "domain":"Finance"},
    # {"url": "https://www.livemint.com/market",
    #  "uppertag": "h3",
    #  "upperkey": "class",
    #  "uppervalue": "market-new-common-collection_imgStory__hLGEJ imgStory fl",
    #  "lowertag": "div",
    #  "lowerkey": "class",
    #  "lowervalue": "paywall",
    #  "imgtag": "figure",
    #  "imgkey": "",
    #  "imgvalue": "",
    #  "imgname": "src",
    #  "credit_name":"livemint",
    #  "domain":"Finance"},
]


def generateModel(list_headline, list_newsdes, list_link):
    global count
    summary_headline =  summrize(list_headline)
    summary_des = summrize(list_newsdes[:1024])
    url = 'https://yashkassa.pythonanywhere.com/news/addsummary'
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    data = {"link": list_link, "summary_headline": summary_headline[0]['summary_text'], "summary_des":summary_des[0]['summary_text']}
    response = requests.post(url, json=json.dumps(data), headers=headers)
    print(response.text)
    count +=1
    

def postdata(list_link, list_headline, list_newsdes, list_img, list_credit, list_domain):
    url = 'https://yashkassa.pythonanywhere.com/news/singlepostnewsDomainwise'
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    data = {"links": list_link, "headlines": list_headline, "description":list_newsdes, "images":list_img, "credits":list_credit, "domains":list_domain}
    response = requests.post(url, json=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        print('Response:', response.text)
        data = json.loads(response.text)
        if(data['status']  == 'success'):
            generateModel(list_headline, list_newsdes, list_link)
    else:
        print(f'POST request failed with status code {response.status_code}')
        print('Error message:', response.text)

def scrape_news_data():
    for item in data_list:
        url = item["url"]
        uppertag = item["uppertag"]
        upperkey = item["upperkey"]
        uppervalue = item["uppervalue"]
        lowertag = item["lowertag"]
        lowerkey = item["lowerkey"]
        lowervalue = item["lowervalue"]
        imgtag = item["imgtag"]
        imgkey = item["imgkey"]
        imgvalue = item["imgvalue"]
        imgname = item["imgname"]
        credit_name = item["credit_name"]
        domain = item["domain"]

        try:
            r = requests.get(url)
        except:
            print(f'Faild {url}')
            
        soup = BeautifulSoup(r.content, 'lxml')
        all_articles = soup.find_all(uppertag, {upperkey: uppervalue})
        all_articles = all_articles[:5]

        for article in all_articles:
            link = article.find('a')['href']
            headline = article.text.strip()
            page = requests.get(link)
            bsobj = BeautifulSoup(page.content, 'lxml')
            news_content = bsobj.find(lowertag, {lowerkey: lowervalue})
            image = bsobj.find(imgtag, {imgkey: imgvalue})
            img = None
            if image:
                try:
                    if credit_name == "The hindu":
                        img = image.find('source').get(imgname, None)
                    else:
                        img_tag = image.find('img')
                        img = img_tag.get(imgname, None) if img_tag else None
                except:
                    print(f'image error {url}')

            if news_content:
                newsdes = news_content.text.strip()
                postdata(link, headline, newsdes, img, credit_name, domain)
    
    

scrape_news_data()  

print(count)
