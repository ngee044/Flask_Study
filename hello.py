from flask import Flask, request

app = Flask(__name__)

#solution 1
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

#solution 2
@app.route('/login', methods=['GET'])
def login_page():
    return show_the_login_form()

@app.route('/login', methods=['POST'])
def login():
    return do_the_login()

def show_the_login_form():
    pass

def do_the_login():
    pass
