from flask import *
from pafy import new
from pywhatkit import playonyt


web = Flask(__name__)
song = None


@web.route("/link")
def home():
    return render_template("link.html")


@web.route("/you")
def you():
    global song
    args = request.args
    try:
        frm = args["from"].strip()
        to = args["to"].strip()
        song = args["song"].strip()
        
    except:
        return "<error>code=100<br>Invalid Data</error>"
        
    return render_template("you.html",frm=frm,to=to,tlen=len(to))


@web.route("/iloveu")
def love():
    url = None
    if song!=None:
        url = new(playonyt(song.replace("%"," "),open_video=False).split("\\")[0]).getbestaudio().url

    return render_template("love.html",url=url)


web.run(host="192.168.225.137",port=5000,debug=True)