import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    drive = psutil.disk_usage('/')
    total = drive.total
    used = drive.used
    free = drive.free
    percent = drive.percent
    return f"Total : {total} Used : {used} Free : {free} Percent : {percent}"

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')