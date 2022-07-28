from flask import render_template
from app import app
from models import Authors, Categories, Posts, Status
@app.route("/")
def home():
    status=Status.query.all()
    posts=Posts.query.all()
    categories=Categories.query.all()
    authors=Authors.query.all()
    return render_template("home.html",posts=posts,authors=authors,categories=categories,status=status)

@app.route("/categories")
def categories():
    status=Status.query.all()
    posts=Posts.query.all()
    categories=Categories.query.all()
    authors=Authors.query.all()
    return render_template("categories.html",posts=posts,authors=authors,categories=categories,status=status)

@app.route('/blog/<int:id>',methods=["GET","POST"])
def blog(id):
    status=Status.query.all()
    posts=Posts.query.all()
    categories=Categories.query.all()
    authors=Authors.query.all()
    return render_template("blog.html",post=posts[id-1],authors=authors,categories=categories,status=status)

@app.route('/category/<int:id>',methods=["GET","POST"])
def category(id):
    status=Status.query.all()
    posts=Posts.query.all()
    categories=Categories.query.all()
    authors=Authors.query.all()
    return render_template("category.html",category=categories[id-1],posts=posts,authors=authors,categories=categories,status=status)
