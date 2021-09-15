from ..shared.messages.errors import UserErrors
from app import db
from app.models.users.user_tokens import UserTokensModel
from .base_service import BaseService


class UserTokenService(BaseService):

    model = UserTokensModel

    def add_user_token(self, user_token_model):
        self.save_changes(user_token_model)
