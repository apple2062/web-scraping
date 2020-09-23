from flask import Flask, render_template,request
'''@:데코레이터  -> 데코레이터는 바로 아래에 있는 "함수"만을 보는데 그 함수를 decorate 해주는 역할을 한다.
 때문에 파이썬이 이 코드를 본 순간 아~ /contact로 접속 요쳥이 들어오면 potato를 실행하면 되는구나 라고 생각 '''
app = Flask("FlaskScrapper")

@app.route("/") #home
def home():
    return render_template("home.html")
    
'''
@app.route("/<username>")
def potato(username):
    return f"Contact your name is {username}"
'''
@app.route("/report")
def report():
    word = request.args.get('word')
    word = word.lower()
    return render_template("report.html",searching = word) #여기 내가 선언한 searching 변수를 html 파일의 {{}} 안의 변수 안에 넣어주면 플라스크가 여기 값을 담아 사용자한테 보여줌 

app.run(host = "0.0.0.0") 