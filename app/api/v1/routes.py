# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from app.api.v1.controllers.user_controller import api as user_ns
from app.api.v1.controllers.auth_controller import api as auth_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service',
          ordered= False
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')