from flask import Flask, render_template, request
import api

app = Flask(__name__)


@app.route('/',methods=["GET"])
def hello():
    p = request.args.get("p")
    if p == None or p =="":
        res = "אין מה לראות כאן. עדיין!"
        p = "הכנס בסיס"
    else:
        try:
            res = api.get_par(p)
        except:
            res = "קרתה בעיה. נסה שוב בבקשה"
    return render_template("webpage.html",res=res,p=p)
