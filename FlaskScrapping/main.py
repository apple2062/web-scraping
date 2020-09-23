from flask import Flask, render_template,request,redirect
from scrapper import get_jobs
'''
@:데코레이터  -> 데코레이터는 바로 아래에 있는 "함수"만을 보는데 그 함수를 decorate 해주는 역할을 한다.
 때문에 파이썬이 이 코드를 본 순간 아~ /contact로 접속 요쳥이 들어오면 potato를 실행하면 되는구나 라고 생각 
'''

app = Flask("FlaskScrapper")

'''
매번 실행할때마다 stackoverflow 에 존재하는 150 페이지의 word job을 scraping하는 걸 기다릴 순 없다.
그래서 fake DB 마냥 저장소가 필요. fake DB 는 route 외부인, 바깥쪽으로 나와있어야 한다.
'''
db = {}

@app.route("/") #home
def home():
    return render_template("home.html")
    

@app.route("/<username>")
def potato(username):
    return f"Contact your name is {username}"

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        fromdb = db.get(word)  #내가 검색요청한 직업을 db 에서 찾는다
        if fromdb:  #fromdb에 직업이 존재한다면,
            jobs = fromdb  #스크래퍼가 동작하지 않아도됨.
        else:
            jobs = get_jobs(word)
            db[word] = jobs #직업이 존재하지 않으므로, 스크래퍼 동작 가동하고 db 에 저장
    else:
        return redirect("/")
        
    return render_template("report.html",searching = word,resultsNumber= len(jobs)) #여기 내가 선언한 searching 변수를 html 파일의 {{}} 안의 변수 안에 넣어주면 플라스크가 여기 값을 담아 사용자한테 보여줌 

app.run(host = "0.0.0.0") 