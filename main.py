from flask import Flask

from utils import *

req = Utils() # создание экземпляра класса для работы функций
FILENAME = "candidates.json"
req.load_candidates(FILENAME)
DATA = req.get_all()

app = Flask(__name__)

@app.route('/')
def index():
    str="<pre>"
    for item in DATA:
        str += f"{item.name}\n"
        str += f"{item.position}\n"
        str += f"{item.skills}\n"
        str += "<br>"
    str += "</pre>"
    return str


@app.route('/candidates/<int:pk>')
def get_user(pk):
    user = req.get_by_pk(pk)
    if user:
        str = "<pre>"
        str += f"<img src='(user.picture)'>\n"
        str += f"{user.name}\n"
        str += f"{user.position}\n"
        str += f"{user.skills}\n"
        str += "</pre>"
    else:
        str = "NOT FOUND"
    return str


@app.route('/skills/<x>')
def get_user_skill(x):
    users = req.get_by_skill(x)
    if users:
        str = "<pre>"
        for user in users:
            str += f"<img src='(user.picture)'>\n"
            str += f"{user.name}\n"
            str += f"{user.position}\n"
            str += f"{user.skills}\n"
            str += "<br>"
        str += "</pre>"
    else:
        str = "NOT FOUND"
    return str


if __name__ == '__main__':
    app.run(port=5000, debug=False)