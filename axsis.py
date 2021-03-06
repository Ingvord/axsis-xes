# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:32:08 2020

@author: ingvord
"""


from flask import Flask, request
from flask_restful import Api
from picontroller import PiController, PiControllerServoMode, PiControllerReference, PiControllerPosition, PiControllerStop
from pi_device import create_pi_device as internal_create_pi_device


app = Flask(__name__)
api = Api(app)

api.add_resource(PiController, '/axsis/controllers/<int:id>')
api.add_resource(PiControllerServoMode, '/axsis/controllers/<int:id>/servo')
api.add_resource(PiControllerReference, '/axsis/controllers/<int:id>/reference')
api.add_resource(PiControllerPosition, '/axsis/controllers/<int:id>/position')
api.add_resource(PiControllerStop, '/axsis/controllers/<int:id>/stop')


@app.before_request
def create_pi_device():
    host = request.args.get('ip')
    port = request.args.get('port', default=50000)

    request.pi_device = internal_create_pi_device(host, port)


@app.teardown_request
def destroy_pi_device(response):
    request.pi_device.CloseConnection()
    return response

