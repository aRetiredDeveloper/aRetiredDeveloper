import enum


class GenericError(enum.Enum):
    OOPS_SOMETHING_WENT_WRONG = 'Oops, something went wrong and unable to process your request!'


class UserErrors(enum.Enum):
    USER_ALREADY_EXIST = 'User already exist. Please login in your account or choose another email'
    USER_SUCCESSFULLY_CREATED = 'User has been successfully added. Please login now!'


class AuthErrors(enum.Enum):
    INVALID_USERNAME_PASSWORD = 'Invalid Username or Password. Please check and login again'
    MISSING_AUTH_TOKEN = 'Authorization is missing'
    AUTH_TOKEN_NOT_VALID = 'Authorization is invalid. Make sure you are logged in!'
    MAILFORMED_TOKEN = 'Token is not correct. It is mailformed token. Please login again or check your token'

