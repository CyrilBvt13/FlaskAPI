
from .sensorDatas import SensorDataAPI, SensorDatasAPI

def initialize_routes(api):
    api.add_resource(SensorDatasAPI, "/flaskAPI/sensordata/")
    api.add_resource(SensorDataAPI, "/flaskAPI/sensordata/<uid>")