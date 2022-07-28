from admin import AuthorsAdmin, CategoriesAdmin, PostsAdmin, StatusAdmin
from extensions import db,admin
from datetime import datetime
from flask_admin.contrib.sqla import ModelView

class Status(db.Model):
     __tablename__ = "Status"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(250), nullable = False)
     def __repr__(self):
        return f'{self.name}'

     def __init__(self, name):
        self.name = name 

     def save(self):
        db.session.add(self)
        db.session.commit()
class Authors(db.Model):
     __tablename__ = "Authors"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(250), nullable = False)
     def __repr__(self):
        return f'{self.name}'

     def __init__(self, name):
        self.name = name 

     def save(self):
        db.session.add(self)
        db.session.commit()

class Categories(db.Model):
     __tablename__ = "Categories"
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(250), nullable = False)
     def __repr__(self):
        return f'{self.name}'

     def __init__(self, name):
        self.name = name 

     def save(self):
        db.session.add(self)
        db.session.commit()
class Posts(db.Model):
    __tablename__ = "Posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable = False)
    author=db.Column(db.Integer,db.ForeignKey('Authors.id'),nullable=False)
    author_desc=db.Column(db.String(255),nullable=False)
    img= db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    status=db.Column(db.Integer,db.ForeignKey('Status.id'),nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey('Categories.id'),nullable=False)
    posted_at=db.Column(db.DateTime,nullable=False)


    def __repr__(self):
        return f'{self.title}'

    def __init__(self, title,author,author_desc,img,description,status,category_id,posted_at):
        self.title = title 
        self.author=author
        self.author_desc=author_desc
        self.img=img
        self.description = description
        self.status=status
        self.category_id=category_id
        self.posted_at=posted_at

    def save(self):
        db.session.add(self)
        db.session.commit()

admin.add_view(AuthorsAdmin(Authors, db.session))
admin.add_view(CategoriesAdmin(Categories, db.session))
admin.add_view(PostsAdmin(Posts, db.session))
admin.add_view(StatusAdmin(Status, db.session))