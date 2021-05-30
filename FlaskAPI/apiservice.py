#~/FlaskAPI/apiservice.py

from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.routes import initialize_routes


project = "flaskAPI"

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

initialize_routes(api)

if __name__ == "__main__":
#   app.run(host='0.0.0.0', debug=False)
    app.run(debug=True)