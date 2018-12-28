import os
import subprocess
import psutil

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return ""

@app.route("/cpu", methods = ['GET', 'POST'])
def get_cpu():
    if request.method == 'GET':
        return str(psutil.cpu_percent())
    if request.method == 'POST':
        cpu_quota = request.get_json(force=True)['cpu_quota']
        id_containers = os.popen("sudo docker container ls | grep stress | awk '{print $1;}'").readlines()
        
        for id_container in id_containers:
            id_container = id_container.split('\n')[0]
            os.system("sudo docker update " + id_container + " --cpu-period 100000 --cpu-quota " + cpu_quota)

        return ""

if __name__ == "__main__":
    app.run(debug=True)