from flask_restful import reqparse

class SensorData:
    pigarden_args = reqparse.RequestParser()
    pigarden_args.add_argument("id", type=str, help="ID is missing", required=True)
    pigarden_args.add_argument("timestamp", type=str, help="Timestamp is missing", required=True)
    pigarden_args.add_argument("temperature", type=float, help="Temperature is missing", required=True)
    pigarden_args.add_argument("pressure", type=float, help="Pressure is missing", required=True)
    pigarden_args.add_argument("humidity", type=float, help="Humidity is missing", required=True)