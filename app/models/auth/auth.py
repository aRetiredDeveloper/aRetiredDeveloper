import sys
import traceback
from app.models.user import UserModel
from app.models.users.user_tokens import UserTokensModel
from app.services.user_token import UserTokenService
from app.shared.status_code import HttpStatusCode
from app.shared.messages.errors import GenericError, AuthErrors
from app.shared.messages.success import UserMessage
from app import db
from app.services.base_service import BaseService


class AuthModel(BaseService):
    model = UserModel

    @staticmethod
    def login_user(data):
        try:
            user_model = UserModel()
            user = UserModel.query.filter_by(email=data['email']).first()
            if user and user.check_password(data.get('password')):
                auth_token = user_model.encode_auth_token(user.id)
                user_token = UserTokensModel(user_id= user.id, auth_token=auth_token, source_origin=1)
                UserTokenService.save_changes(user_token)
                if auth_token:
                    response_object = {
                        'success': True,
                        'message': UserMessage.LOGIN_SUCCESSFULLY.value,
                        'Authorization': auth_token,
                        'errors': []
                    }
                    return response_object, HttpStatusCode.SUCCESS.value
            else:
                response_object = {
                    'success': False,
                    'message': AuthErrors.INVALID_USERNAME_PASSWORD.value,
                    'errors': [
                        {
                            'error_code': HttpStatusCode.FORBIDDEN.value,
                            'error_message': AuthErrors.INVALID_USERNAME_PASSWORD.value}]
                }
                return response_object, HttpStatusCode.BAD_REQUEST.value
        except Exception as e:
            UserTokenService.rollback()
            response_object = {
                'success': False,
                'message': GenericError.OOPS_SOMETHING_WENT_WRONG.value,
                'errors': [{'error_code': HttpStatusCode.INTERNAL_SERVER_ERROR.value, 'error_message': e}]
            }
            return response_object, HttpStatusCode.INTERNAL_SERVER_ERROR.value

    @staticmethod
    def logout(auth_token):
        if auth_token:
            auth_token = auth_token.split(" ")[1]
            user_token = UserTokenService.get_details(auth_token=auth_token)
            if not user_token:
                return {'success': False, 'message': AuthErrors.AUTH_TOKEN_NOT_VALID.value,
                        'errors': [{'error_code': HttpStatusCode.BAD_REQUEST.value,
                                    'error_message': AuthErrors.AUTH_TOKEN_NOT_VALID.value}]}
            response = AuthModel.delete_user_token(user_token)
            return response
        else:
            return {'success': False, 'message': AuthErrors.MISSING_AUTH_TOKEN.value,
                    'errors': [{'error_code': HttpStatusCode.BAD_REQUEST.value,
                                'error_message': AuthErrors.MISSING_AUTH_TOKEN.value}]
                    }, HttpStatusCode.FORBIDDEN.value

    @staticmethod
    def delete_user_token(user_token):
        try:
           AuthModel.delete(user_token)
           return {'success': True, 'message': UserMessage.LOGOUT_SUCCESSFULLY.value, 'errors': []},\
                  HttpStatusCode.SUCCESS.value
        except Exception as e:
            AuthModel.rollback()
            ex_type, ex_value, ex_traceback = sys.exc_info()
            return {'success': False, 'message': str(ex_value),
                    'errors': [{'error_code': HttpStatusCode.INTERNAL_SERVER_ERROR.value, 'error_message': str(ex_value)}]}, HttpStatusCode.INTERNAL_SERVER_ERROR.value
