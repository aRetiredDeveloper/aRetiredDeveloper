from functools import wraps
from flask import request
from app.services.user_token import UserTokenService
from app.shared.status_code import HttpStatusCode
from app.shared.messages.errors import AuthErrors, UserErrors, GenericError
from flask import Flask, g


def check_token_exist(auth_token):
    if not auth_token:
        return {'success': False, 'message': AuthErrors.MISSING_AUTH_TOKEN.value,
                'errors': [{'error_code': HttpStatusCode.FORBIDDEN.value,
                            'error_message': AuthErrors.MISSING_AUTH_TOKEN.value}]
                }
    token = auth_token.split(" ")
    if len(token) < 2 or len(token) > 2:
        return {'success': False, 'message': AuthErrors.MAILFORMED_TOKEN.value,
                'errors': [
                    {'error_code': HttpStatusCode.FORBIDDEN.value, 'error_message': AuthErrors.MAILFORMED_TOKEN.value}]
                }
    return {'success': True}


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        auth_token_exist = check_token_exist(auth_token)
        if auth_token_exist and not auth_token_exist.get('success'):
            return auth_token_exist, HttpStatusCode.FORBIDDEN.value
        auth_token = auth_token.split(" ")[1]
        token_exist = UserTokenService.get_details(auth_token=auth_token)
        if not token_exist:
            return {
                       'success': False,
                       'message': AuthErrors.AUTH_TOKEN_NOT_VALID.value,
                       'errors': [{'error_code': HttpStatusCode.FORBIDDEN.value,
                                   'error_message': AuthErrors.AUTH_TOKEN_NOT_VALID.value}]
                   }, HttpStatusCode.FORBIDDEN.value
        g.user_id = token_exist.id
        return f(*args, **kwargs)

    return decorated
