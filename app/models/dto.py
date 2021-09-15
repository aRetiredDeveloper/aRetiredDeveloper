from flask_restplus import Namespace, fields


class ErrorResponse(object):
    api = Namespace('error', description='Error Format')

    @staticmethod
    def error_format():
        return ErrorResponse.api.model('errors', {
            'error_code': fields.String(description='Error Code'),
            'error_message': fields.String(description='Error Message')
        })


class GenericResponse(object):
    api = Namespace('response', description='User related operations')

    @staticmethod
    def api_response():
        return GenericResponse.api.model('response', {
            'success': fields.Boolean(),
            'message': fields.String(description='message'),
            'errors': fields.List(fields.Nested(ErrorResponse.error_format()))
        })


class UserDTO(GenericResponse):
    api = Namespace('user', description='User related operations')
    # user = api.model('user', {**GenericResponse.response, **{
    #     'data': fields.List(fields.String())
    # }})
    user = api.model('user', {
        'data': fields.List(fields.String())
    })


class AuthDto(GenericResponse):
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

    user_response = api.model('login_response', {
        **GenericResponse.api_response(),
        "Authorization": fields.String()
    })
