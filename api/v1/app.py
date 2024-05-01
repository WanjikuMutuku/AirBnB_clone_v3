#!/usr/bin/python3
"""app file of v1"""

import flask from Flask, jsonify
from storage import models
from app_views import api.v1.views

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix= '/api/v1')

@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

@app.errorhandler(404)
def handle_not_found_error(error):
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
