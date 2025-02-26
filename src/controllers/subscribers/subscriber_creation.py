from src.model.repositories.interfaces.inscritos_repository_interface import InscritosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscriberCreation:
    def __init__(self, subs_repo: InscritosRepositoryInterface):
        self.__subs_repo = subs_repo
        
    def create(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body["data"]
        subscriber_email = subscriber_info["email"]
        event_id = subscriber_info["evento_id"]
        
        self.__check_subscriber(subscriber_email, event_id)
        self.__insert_subscriber(subscriber_info)
        
        return self.__format_response(subscriber_info)
        
    def __check_subscriber(self, subscriber_email: str, event_id: int) -> None:
        response = self.__subs_repo.select_subscriber(email=subscriber_email, evento_id=event_id)
        if response:
            raise Exception("Subscriber already exists")
        
    def __insert_subscriber(self, subscriber_info: dict) -> None:
        self.__subs_repo.insert(subscriber_info)
        
    def __format_response(self, subscriber_info: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": 1,
                    "attributes": subscriber_info
                }
            },
            status_code=201
        )