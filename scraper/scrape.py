import scrape_kantipur
import scrape_nagarik
import scraper_onlinekhabar
import scrape_annapurnapost
import csv
import os
online = []
kantipur = []
nagarik = []

os.system("rm *.txt")
scrape_kantipur.scrape()
scrape_nagarik.scrape()
scraper_onlinekhabar.scrape()
scrape_annapurnapost.scrape()

f = open("../ServerSide/NewsData.txt",'a')
f.write("news title,url,domain\n")
online_khabar = open("online_khabar.txt",'r')
f.write(online_khabar.read()+'\n')
online_khabar.close()
nagarik_news = open("nagarik_news.txt",'r')
f.write(nagarik_news.read())
nagarik_news.close()
kantipur_daily = open("kantipur_daily.txt",'r')
f.write(kantipur_daily.read())
kantipur_daily.close()
annapurna_post = open("annapurna_post.txt",'r')
f.write(annapurna_post.read())
annapurna_post.close()
f.close()

