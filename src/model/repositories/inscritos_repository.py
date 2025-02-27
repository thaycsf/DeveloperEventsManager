from sqlalchemy import func, desc
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.inscritos_repository_interface import InscritosRepositoryInterface

class InscritosRepository(InscritosRepositoryInterface):
    def insert(self, subscriber: dict) -> None:
      with DBConnectionHandler() as db:
          try:
            new_subscriber = Inscritos(
              nome=subscriber.get("nome"), 
              email=subscriber.get("email"), 
              link=subscriber.get("link"), 
              evento_id=subscriber.get("evento_id")
              )
            db.session.add(new_subscriber)
            db.session.commit()
          except Exception as exception:
            db.session.rollback()
            raise exception
          
    def select_subscriber(self, **subscriber_filters) -> Inscritos:
      with DBConnectionHandler() as db:
        query = db.session.query(Inscritos)
        
        for attribute, value in subscriber_filters.items():
          if hasattr(Inscritos, attribute):
            query = query.filter(getattr(Inscritos, attribute) == value)
        
        data = query.one_or_none()
        return data
      
    def select_subscriber_by_link(self, subscriber_link:str, event_id: int) -> list:
      with DBConnectionHandler() as db:
        data = (
          db.session.query(Inscritos)
          .filter
          (
            Inscritos.link == subscriber_link,
            Inscritos.evento_id == event_id
          )
          .all()
        )
        
        return data
      
    def get_ranking(self, event_id: int) -> list:
      with DBConnectionHandler() as db:
        result = (
          db.session.query(
            Inscritos.link,
            func.count(Inscritos.id).label("total")
          )
          .filter(
            Inscritos.evento_id == event_id,
            Inscritos.link.isnot(None)
          )
          .group_by(Inscritos.link)
          .order_by(desc("total"))
          .all()
        )
        
        return result
