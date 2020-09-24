import csv

def save_to_file(jobs):
    file = open("jobs.csv",mode = "w")
    writer = csv.writer(file)
    writer.writerow(["title","company","location","link"])
    for job in jobs:
        #jobs 에 있는 각 job 을 가지고 row 를 작성할건데 job 이 가진 값의 리스트를 row 로 가져올 것임 
        writer.writerow(list(job.values()))
    return 