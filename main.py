#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://kr.indeed.com/jobs?q=python&radius=25&start=0
from indeed import extract_indeed_pages, extract_indeed_jobs

#최대 페이지 숫자(=max_page) 를 알았으니 max_page 개의 request를 만들어보자.
last_indeed_page = extract_indeed_pages()
print(last_indeed_page)

indeed_jobs = extract_indeed_jobs(last_indeed_page)
