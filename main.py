#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://kr.indeed.com/jobs?q=python&radius=25&start=0
from indeed import get_jobs as get_indeed_jobs

indeed_jobs = get_indeed_jobs()
print(indeed_jobs)

#최대 페이지 숫자(=max_page) 를 알았으니 max_page 개의 request를 만들어보자.

