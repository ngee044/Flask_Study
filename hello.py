from flask import Flask
from v1 import app as v1_app
from v2 import app as v2_app

app = Flask(__name__)
app.register_blueprint(v1_app)
app.register_blueprint(v2_app)




@app.route('/v1/users')
def v1_users():
    return 'v1'

@app.route('/v2/users')
def v2_users():
    return 'v2'

