#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://kr.indeed.com/jobs?q=python&radius=25&start=0
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file

#indeed_jobs = get_indeed_jobs()


so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = so_jobs + indeed_jobs


save_to_file(jobs)
