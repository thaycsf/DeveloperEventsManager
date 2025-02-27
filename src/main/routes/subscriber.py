from flask import Blueprint, jsonify, request

subscriber_route_bp = Blueprint('subscriber_route', __name__)

from src.validators.subscriber_creation_validator import subscriber_creation_validator

from src.http_types.http_request import HttpRequest

from src.model.repositories.inscritos_repository import InscritosRepository

from src.controllers.subscribers.subscriber_creation import SubscriberCreation
from src.controllers.subscribers.subscriber_manager import SubscriberManager

@subscriber_route_bp.route('/subscriber', methods=['POST'])
def create_new_subscriber():
    subscriber_creation_validator(request)
    
    http_request = HttpRequest(body=request.json)
    
    subs_repo = InscritosRepository()
    subscriber_creation = SubscriberCreation(subs_repo)
    
    http_response = subscriber_creation.create(http_request)
    
    return jsonify(http_response.body), http_response.status_code

@subscriber_route_bp.route('/subscriber/link/<link>/event/<event_id>', methods=['GET'])
def subscribers_by_link(link, event_id):       
    subs_repo = InscritosRepository()
    subscriber_manager = SubscriberManager(subs_repo)
    
    http_request = HttpRequest(param={"link": link, "event_id": event_id})
    
    http_response = subscriber_manager.get_subscribers_by_link(http_request)
    
    return jsonify(http_response.body), http_response.status_code

@subscriber_route_bp.route('/subscriber/ranking/event/<event_id>', methods=['GET'])
def ranking_link(event_id):       
    subs_repo = InscritosRepository()
    subscriber_manager = SubscriberManager(subs_repo)
    
    http_request = HttpRequest(param={"event_id": event_id})
    
    http_response = subscriber_manager.get_event_ranking(http_request)
    
    return jsonify(http_response.body), http_response.status_code