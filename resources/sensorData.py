#~/FlaskAPI/resources/sensorData.py

from flask_restful import Resource
from flask_jwt_extended import jwt_required
from database.models import SensorData
from database.db import db, query
import uuid

class SensorDatasAPI(Resource):
    def get(self):
        return db.all()

    @jwt_required
    def put(self):
        id = uuid.uuid4().hex
        args = SensorData.sensorData_args.parse_args()
        args['id'] = id
        print(args)
        db.insert(args)
        return {'id': str(args['id'])}, 201

class SensorDataAPI(Resource):
    def get(self, uid):
        return db.search(query.id == uid)

    @jwt_required
    def patch(self, uid):
        args = sensorData_args.parse_args()
        db.update(args, query.id == uid)
        return db.search(query.id == uid), 201

    @jwt_required
    def delete(self, uid):
        db.remove(query.id == uid)
        return '', 204