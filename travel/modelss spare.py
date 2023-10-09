from . import db
from datetime import datetime

#week 9 work
class User(db.Model):
    #change the bracktes to db.Model
    __tablename__ = 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False) #no column can be empty
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user') # backreg is going back to user
#week 9 work


class Destination:
    def __init__(self, name, description, image, currency):
        self.name = name
        self.description = description
        self.image = image
        self.currency = currency
        self.comments = list()

    def set_comments(self, comment):
        self.comments.append(comment)

    def __repr__(self):
        str = f"Name: {self.name}, Currency: {self.currency}"
        return str

class Comment:
    def __init__(self,user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at


#optional
    def __repr__(self):
        str = f"User {self.user}, \n Text {self.text}"
        return str