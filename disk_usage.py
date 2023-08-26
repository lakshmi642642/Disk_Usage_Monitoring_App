import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    drive = psutil.disk_usage('/')
    total = drive.total
    total = total / 1000000000
    used = drive.used
    used = used / 1000000000
    free = drive.free
    free = free / 1000000000
    percent = drive.percent
    #return f"Total : {total} Used : {used} Free : {free} Percent : {percent}"
    return render_template("index.html",total=total,used=used,free=free)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')