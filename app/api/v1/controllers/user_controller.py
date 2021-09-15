from flask import request
from flask_restplus import Resource
from app.models.dto import UserDTO
from app.services.user_service import UserService
from app.utils.generic_response import generic_response
from app.shared.status_code import HttpStatusCode
api = UserDTO.api


@api.route('/')
class UserList(Resource):

    @api.doc('list_of_registered_users')
    @api.marshal_list_with(UserDTO.user)
    def get(self):
        """List all registered users"""
        return UserService.get_details()

    @api.doc('create a new user')
    @api.expect(UserDTO.user, validate=True)
    @api.marshal_with(UserDTO.user)
    def post(self):
        """Creates a new User """
        data = request.json
        userService = UserService()
        response = userService.add_new_user(data=data)
        STATUS_CODE = HttpStatusCode.CREATED.value if response.get('success') else HttpStatusCode.BAD_REQUEST.value
        return response, STATUS_CODE

# @api.route('/<public_id>')
# @api.param('public_id', 'The User identifier')
# @api.response(404, 'User not found.')
# class User(Resource):
#     @api.doc('get a user')
#     @api.marshal_with(_user)
#     def get(self, public_id):
#         """get a user given its identifier"""
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             return user
