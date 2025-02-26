from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos

class InscritosRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber: dict) -> None: pass
    
    @abstractmethod    
    def select_subscriber(self, **subscriber_filters) -> Inscritos: pass
    
    @abstractmethod
    def select_subscriber_by_link(self, subscriber_link:str, event_id: int) -> list: pass
    
    @abstractmethod
    def get_ranking(self, event_id: int) -> list: pass