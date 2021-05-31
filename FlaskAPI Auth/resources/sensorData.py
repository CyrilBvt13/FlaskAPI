#~/FlaskAPI/resources/sensorData.py

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import SensorData, User
from database.db import db, query
import uuid

class SensorDatasAPI(Resource):
    def get(self):
        return db.all()

    @jwt_required()
    def put(self):
        id = uuid.uuid4().hex
        userId = get_jwt_identity()
        args = SensorData.sensorData_args.parse_args()
        args['id'] = id
        args['user'] = userId
        db.insert(args)
        return {'id': str(args['id'])}, 201

class SensorDataAPI(Resource):
    @jwt_required()
    def get(self, uid):
        return db.search(query.id == uid)

    @jwt_required()
    def patch(self, uid):
        args = sensorData_args.parse_args()
        db.update(args, query.id == uid)
        return db.search(query.id == uid), 201

    @jwt_required()
    def delete(self, uid):
        db.remove(query.id == uid)
        return '', 204
