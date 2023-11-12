# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar 
"""


from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_mars():
    return "Visitor to Mars, Welcome \n"


@app.route("/test")
def test():
    return "Testinng, emergency service running)"


@app.route("/describe")
def describe():
    from datetime import datetime

    description = (
        f"description\n Date and time: {datetime.now()}\n"
        "system running: emergency module\n"
        "larvis status: down\n"
        "larvis emergency: Docker container\tresponding: True\n"
        """"Minikube status: cluster:\n"
                   "extensions:\n"
                   "- extension\n:"
                  " last-update: Sat, 11 Nov 2023 22:41:12 GMT\n"
                   "provider: minikube.sigs.k8s.io\n"
                   "version: v1.32.0\n"
                   "name: cluster_info\n"
                   "server: https://127.0.0.1:57234\n"
                   "name: minikube"""
    )
    return description


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="5000")
