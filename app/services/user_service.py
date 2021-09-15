import uuid
import datetime
from ..shared.messages.errors import UserErrors
from app import db
from app.models.user import UserModel
from .base_service import BaseService


class UserService(BaseService):

    model = UserModel

    def add_new_user(self, data, auto_commit=True):
        if self.check_if_user_already_exist(data['email']):
            return {'success': False,
                    'errors': [UserErrors.USER_ALREADY_EXIST.value],
                    'message': UserErrors.USER_ALREADY_EXIST.value
                    }
        updated_data = UserModel(email=data['email'], name=data['name'], password=data['password'])
        self.save_changes(updated_data, auto_commit)
        return {'success': True,
                'errors': [],
                'data': [],
                'message': UserErrors.USER_SUCCESSFULLY_CREATED.value
                }

    def check_if_user_already_exist(self, email):
        return self.model.query.filter_by(email= email).first()

