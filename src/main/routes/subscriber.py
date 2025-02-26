from flask import Blueprint, jsonify, request

subscriber_route_bp = Blueprint('subscriber_route', __name__)

from src.validators.subscriber_creation_validator import subscriber_creation_validator

from src.http_types.http_request import HttpRequest

from src.controllers.subscribers.subscriber_creation import SubscriberCreation

from src.model.repositories.inscritos_repository import InscritosRepository

@subscriber_route_bp.route('/subscriber', methods=['POST'])
def create_new_subscriber():
    subscriber_creation_validator(request)
    
    http_request = HttpRequest(body=request.json)
    
    subs_repo = InscritosRepository()
    subscriber_creation = SubscriberCreation(subs_repo)
    
    http_response = subscriber_creation.create(http_request)
    
    return jsonify(http_response.body), http_response.status_code