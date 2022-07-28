from flask import Flask, request,render_template

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/Blogs'
app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
app.config['SECRET_KEY'] = "my_project"

from extensions import *
from models import *
from controllers import *


if __name__ == "__main__":
    app.run(port=5000,debug=True)
