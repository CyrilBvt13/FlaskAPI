#~/FlaskAPI/database/models.py

from flask_restful import reqparse
from flask_bcrypt import generate_password_hash, check_password_hash

class SensorData:
    sensorData_args = reqparse.RequestParser()
    sensorData_args.add_argument("id", type=str)
    sensorData_args.add_argument("user", type=str)
    sensorData_args.add_argument("timestamp", type=str, help="Timestamp is missing", required=True)
    sensorData_args.add_argument("temperature", type=float, help="Temperature is missing", required=True)
    sensorData_args.add_argument("pressure", type=float, help="Pressure is missing", required=True)
    sensorData_args.add_argument("humidity", type=float, help="Humidity is missing", required=True)

class User:
    user_args = reqparse.RequestParser()
    user_args.add_argument("id", type=str)
    user_args.add_argument("email", type=str, help="email is missing", required=True)
    user_args.add_argument("password", type=str, help="password is missing", required=True)
    
    def hash_password(password):
        hashedPassword = generate_password_hash(password).decode('utf8')
        return hashedPassword
 
    def check_password(hashedPassword, password):
        return check_password_hash(hashedPassword, password)