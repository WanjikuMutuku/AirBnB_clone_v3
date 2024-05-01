#!/usr/bin/python3
"""api index"""

from api.v1.views import app_views
from flask import jsonify
import models
from models import storage
from models.base_model import BaseModel


@app_views.route('/status', strict_slashes=False)
def get_stats():
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
