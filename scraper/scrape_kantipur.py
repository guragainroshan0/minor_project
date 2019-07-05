import json
import bs4 as bs
import requests
import csv
from datetime import datetime,timedelta
def scrape():
        i=0
        day = datetime.today()
        for _ in range(150):         
                url = "https://www.kantipurdaily.com/news/"+str(day)[:10].replace('-','/')+"?json=true"
                #print(url)
                day = day - timedelta(days=1)
                r = requests.get(url)
                # print(r.text)
                p = bs.BeautifulSoup(json.loads(r.text)["html"],"lxml")
                posts = p.find_all("h2")
                for title in posts:
                        data = title.find("a")
                        with open("kantipur_daily.txt",'a') as csv_file:
                                csv_write = csv.writer(csv_file,delimiter=',')
                                csv_write.writerow([data.text,data["href"],'KantipurDaily'])
                                #print(data["href"])
                                print(data.text)
                                i = i+1
        print(i)

if __name__=="__main__":
        scrape()
