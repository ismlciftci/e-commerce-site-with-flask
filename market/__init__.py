from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from  flask_login import LoginManager
app = Flask(__name__)
if __name__ =="__main__":
    app.debug = True
    app.run()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
app.config['SECRET_KEY'] = '7c6541cc452541625a3e3b9a'
db = SQLAlchemy(app)
bcrypt =Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category="info"
from market import routes

