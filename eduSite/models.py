from datetime import datetime
from eduSite import db, login_manager 
from flask_login import UserMixin

#http://flask-sqlalchemy.pocoo.org/2.3/models/

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User(db.Model, UserMixin):                           #class User is inheriting from superclass
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post', backref='user',lazy=True)
    #role = db.Column()

    def __repr__(self):                                                                                                     #https://www.codecademy.com/en/forum_questions/52405de880ff33e27c002c9a
        return f"User('{self.username}', '{self.email}')"     #remember to add role

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #nature = db.Column()
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"   #remember to add nature i.e course or review/doubt