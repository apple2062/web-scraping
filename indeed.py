#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:22:21 2020

@author: iyeonju
"""

 
import requests
from bs4 import BeautifulSoup # 데이터 추출하는 애

LIMIT =  50
#URL = "https://www.indeed.com/jobs?q=python&limit=50"
URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python"

#제일 마지막 페이지 번호 수 알아내기
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,'html.parser')
    pagination = soup.find("div",{"class":"pagination"})  # 맨 하단 페이지 버튼 번호

    links = pagination.find_all('a') #버튼 마다 있는 anchor찾기
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string)) #anchor태그 안의 span 태그만 찾아서 '내용 가져오기'(.string)   
 
    max_page = pages[-1] #가장 큰 페이지 번호 가져오기
    return max_page

#extract_jobs를 통해 html인자(=request한 결과를 담은 result)를 받고 직업:회사 반
def extract_job(html):
        #result는 일자리 목록이고,거기서 div 를 찾았는데 class명이 title이어야 했다.그리고 그 안에 anchor을 찾아서 그 attribute인 title 가져오기
        title = html.find("h2",{"class":"title"}).find("a")["title"] #["title"]은 a 태그 안의 title이라는 속성을 가져온것 
        company = html.find("span",{"class":"company"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = (str(company_anchor.string))
        else:
            company = (str(company.string)) 
        location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
        job_id = html["data-jk"] #esults = soup.find_all("div",{"class":"jobsearch-SerpJobCard"}) < 이놈들마다 id를 불러오
        return {'title':title,'company':company[1:],'location':location,'link':f"https://kr.indeed.com/viewjob?jk={job_id}"}

    
#indeed page를 입력받아서 그 만큼의 Request를 만들기 위한 함수
def extract_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        result = requests.get(f"{URL}&start={0*LIMIT}") #https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}&start={)*LIMIT}
        soup = BeautifulSoup(result.text,'html.parser')
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs 

def get_jobs():
    last_page = get_last_page()
    jobs =extract_jobs(last_page)
    return jobs