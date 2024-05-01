#!/usr/bin/python3
"""
API endpoints for State objects.
"""

from models import storage
from models.state import State
from flask import jsonify, request, abort
from api.v1.views import app_views


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def states():
    """
    Retrieves the list of all State objects or creates a new State.
    """
    if request.method == 'GET':
        states = storage.all(State).values()
        return jsonify([state.to_dict() for state in states])

    if request.method == 'POST':
        if not request.get_json():
            abort(400, 'Not a JSON')
        if 'name' not in request.get_json():
            abort(400, 'Missing name')
        data = request.get_json()
        state = State(**data)
        state.save()
        return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'], strict_slashes=False)
def state(state_id):
    """
    Retrieves a State object, updates it, or deletes it.
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(state.to_dict())

    if request.method == 'PUT':
        if not request.get_json():
            abort(400, 'Not a JSON')
        ignored_keys = ['id', 'created_at', 'updated_at']
        data = request.get_json()
        for key, value in data.items():
            if key not in ignored_keys:
                setattr(state, key, value)
        state.save()
        return jsonify(state.to_dict()), 200

    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
