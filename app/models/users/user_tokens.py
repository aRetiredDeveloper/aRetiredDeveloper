from app import db, flask_bcrypt
import datetime
from ..base_model import BaseModel
from app.configurations import key
from app.shared.constants import CONSTANT


class UserTokensModel(BaseModel):

    __tablename__ = 'user_tokens'

    id = db.Column(db.Integer(), primary_key=True, unique=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    auth_token = db.Column(db.Text())
    source_origin = db.Column(db.Integer())
    expiration_time = db.Column(db.DateTime())

    def __init__(self, user_id, auth_token, source_origin=1):
        print(user_id, auth_token, source_origin)
        self.user_id = user_id
        self.auth_token = auth_token
        self.source_origin = source_origin
        self.expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=CONSTANT.TOKEN_EXPIRATION_DATE)


    def __repr__(self):
        return "<UserToken '{}'--> {}>".format(self.user_id, self.auth_token)
