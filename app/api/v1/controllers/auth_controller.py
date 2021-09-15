from flask import request, g
from flask_restplus import Resource
#from app.main.service.auth_helper import Auth
from app.models.dto import AuthDto
from app.models.auth.auth import AuthModel
from app.utils.decorator import token_required
api = AuthDto.api
user_auth = AuthDto.user_auth
auth_response = AuthDto()

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    @api.marshal_with(auth_response.user_response)
    def post(self):
        # get the post data
        post_data = request.json
        auth_data = AuthModel.login_user(data=post_data)
        return auth_data


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    @token_required
    def post(self):
        # get auth token
        print('user id-->', g.user_id)
        auth_header = request.headers.get('Authorization')
        return AuthModel.logout(auth_token=auth_header)