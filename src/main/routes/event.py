from flask import Blueprint, jsonify, request

event_route_bp = Blueprint('event_route', __name__)

from src.validators.event_creation_validator import event_creation_validator

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

@event_route_bp.route('/event', methods=['POST'])
def create_new_event():
    event_creation_validator(request)
    #http_request = HttpRequest(body=request.json)
    
    http_response = HttpResponse(body={"message": "Event created"}, status_code=201)
    
    return jsonify(http_response.body), http_response.status_code