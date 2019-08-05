package com.roguragain.myapplication;
public class news {

    String news, link , source;

    @Override
    public String toString() {
        return "news{" +
                "news='" + news + '\'' +
                ", link='" + link + '\'' +
                ", source='" + source + '\'' +
                '}';
    }

    public news(String news, String link , String source) {
        this.news = news;
        this.link = link;
        this.source =source;
    }


}