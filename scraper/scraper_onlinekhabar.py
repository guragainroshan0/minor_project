import bs4 as bs
import requests
import csv

def scrape():
    #page = input('Page number each page contains 21 post')
    page = 150
   
    for page_number in range(0,int(page)): 
        sauce = requests.get('https://www.onlinekhabar.com/content/news/page'+str(page_number))
        soup = bs.BeautifulSoup(sauce.text,'lxml')
        posts = soup.find_all("div",class_="relative list__post show_grid--view")
        for post in posts:
            wrapper = post.find_all("div",class_="item")
            tag = wrapper[-1].find('a')
            title = tag.text
            link = tag['href']
            print(title)
            source = link.split('/')[2]
            with open('online_khabar.txt','a') as csv_file:
               csv_writer = csv.writer(csv_file,delimiter=',')
               csv_writer.writerow([title,link,"OnlineKhabar"])
        print(page_number)

if __name__=="__main__":
        scrape()
