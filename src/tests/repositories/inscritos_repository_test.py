from ...model.repositories.inscritos_repository import InscritosRepository
import pytest
import json

@pytest.mark.skip("Insert in DB")
def test_insert_inscrito():
      subscriber = {
            "nome": "Jane Doe", 
            "email": "jane.doe@example.com",
            "evento_id": 2
      }
      subscriber_repository = InscritosRepository()
      
      subscriber_repository.insert(subscriber)
  
@pytest.mark.skip("Select in DB")
def test_select_inscrito():
      query = 2
      subscriber_repository = InscritosRepository()
      
      subscriber = subscriber_repository.select_subscriber(query)
      subscriber_dict = {
            "nome": subscriber.nome,
            "email": subscriber.email,
            "evento_id": subscriber.evento_id
      }
      print(json.dumps(subscriber_dict, default=str, indent=4))
      
@pytest.mark.skip("Select in DB")
def test_ranking():
      event_id = 3
      subscriber_repository = InscritosRepository()
      
      ranking = subscriber_repository.get_ranking(event_id)
      
      for element in ranking:
            print(f"Link: {element.link} - Total de inscritos: {element.total}")