import bs4 as bs
import requests
import csv

def scrape():
    #page = input('Page number each page contains 21 post')
    page = 150
    for page_number in range(0,int(page)): 
        sauce = requests.get('https://nagariknews.nagariknetwork.com/category/21?page='+str(page_number))
        soup = bs.BeautifulSoup(sauce.text,'lxml')
        if page_number == 1:
            data = soup.find_all("div",class_="col-sm-3 part-ent")
            for d in data:
                with open('nagarik_news.txt','a') as csv_file:
                    title = d.find('a').text
                    link = "https://nagariknews.nagariknetwork.com" +d.find('a')['href']
                    print(title+'\n'+link)
                    csv_writer = csv.writer(csv_file,delimiter=',')
                    csv_writer.writerow([title,link,"https://nagariknews.nagariknetwork.com"])
        else:
            posts = soup.find_all('div',class_="col-sm-9 detail-on")
            for data in posts:
                with open('nagarik_news.txt','a') as csv_file:
                    title = data.find('a').text
                    #link = data.find('a')['href']
                    link = "https://nagariknews.nagariknetwork.com" +data.find('a')['href']
                    print(title+'\n'+link)
                    csv_writer = csv.writer(csv_file,delimiter=',')
                    csv_writer.writerow([title,link,"NagarikDaily"])


if __name__=="__main__":
    scrape()
