from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.inscritos_repository_interface import InscritosRepositoryInterface

class SubscriberManager:
    def __init__(self, subscribers_repository: InscritosRepositoryInterface):
        self.__subscribers_repository = subscribers_repository
        
    def get_subscribers_by_link(self, request: HttpRequest) -> HttpResponse:
        link = request.param["link"]
        event_id = request.param["event_id"]
        subscribers = self.__subscribers_repository.select_subscriber_by_link(link, event_id)
        return self.__format_subscribers_by_link(subscribers)
    
    def get_event_ranking(self, request: HttpRequest) -> HttpResponse:
        event_id = request.param["event_id"]
        event_ranking = self.__subscribers_repository.get_ranking(event_id)
        return self.__format_event_ranking(event_ranking)
        
    def __format_subscribers_by_link(self, subscribers: list) -> HttpResponse:
        formatted_subscriber = []
        
        for subscriber in subscribers:
            formatted_subscriber.append(
                {
                    "nome": subscriber.name,
                    "email": subscriber.email,
                }
            )
            
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscribers",
                    "count": len(formatted_subscriber),
                    "subscribers": formatted_subscriber
                }
            },
            status_code=200
        )
        
    def __format_event_ranking(self, ranking: list) -> HttpResponse:
        formatted_ranking = []
        
        for position in ranking:
            formatted_ranking.append(
                {
                    "link": position.link,
                    "total_subscribers": position.total,
                }
            )
            
        return HttpResponse(
            body={
                "data": {
                    "Type": "Ranking",
                    "count": len(formatted_ranking),
                    "subscribers": formatted_ranking
                }
            },
            status_code=200
        )