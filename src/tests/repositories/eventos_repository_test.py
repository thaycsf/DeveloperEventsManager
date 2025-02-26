from ...model.repositories.eventos_repository import EventosRepository
import pytest

@pytest.mark.skip("Insert in DB")
def test_insert_eventos():
  event_name = "Test Event 2"
  event_repository = EventosRepository()
  
  event_repository.insert(event_name)
  
@pytest.mark.skip("Select in DB")
def test_select_event():
  event_name = "Test Event 2"
  event_repository = EventosRepository()
  
  event = event_repository.select_event(event_name)
  print(event)
  print(event.nome)
  print(event.id)