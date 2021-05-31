#~/FlaskAPI/resources/routes.py

from .sensorData import SensorDataAPI, SensorDatasAPI
from .auth import SignupAPI, LoginAPI

def initialize_routes(api):
    api.add_resource(SensorDatasAPI, "/flaskAPI/sensordata/")
    api.add_resource(SensorDataAPI, "/flaskAPI/sensordata/<uid>")

    api.add_resource(SignupAPI, "/flaskAPI/auth/signup/")
    api.add_resource(LoginAPI, "/flaskAPI/auth/login/")