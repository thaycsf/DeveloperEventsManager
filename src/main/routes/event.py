from flask import Blueprint, jsonify, request

event_route_bp = Blueprint('event_route', __name__)

from src.validators.event_creation_validator import event_creation_validator

from src.http_types.http_request import HttpRequest

from src.controllers.events.event_creation import EventCreation
from src.model.repositories.eventos_repository import EventosRepository

@event_route_bp.route('/event', methods=['POST'])
def create_new_event():
    event_creation_validator(request)
    http_request = HttpRequest(body=request.json)
    
    eventos_repo = EventosRepository()
    event_creation = EventCreation(eventos_repo)
    
    http_response = event_creation.create(http_request)
    
    return jsonify(http_response.body), http_response.status_code