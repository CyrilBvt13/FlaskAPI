from flask_restful import Resource
from database.models import SensorData
from database.db import db, query
import uuid

class SensorDatasAPI(Resource):
    def get(self):
        return db.all()

    def put(self):
        id = uuid.uuid4().hex
        args = SensorData.sensorData_args.parse_args()
        args['id'] = id
        print(args)
        db.insert(args)
        return args, 201

class SensorDataAPI(Resource):
    def get(self, uid):
        return db.search(query.id == uid)

    def patch(self, uid):
        args = sensorData_args.parse_args()
        db.update(args, query.id == uid)
        return db.search(query.id == uid), 201

    def delete(self, uid):
        db.remove(query.id == uid)
        return '', 204