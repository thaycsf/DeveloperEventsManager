from ...model.repositories.eventos_link_repository import EventosLinkRepository
import pytest

@pytest.mark.skip("Insert in DB")
def test_insert_evento_link():
  event_id = 7
  subscriber_id = 3
  event_link_repository = EventosLinkRepository()
  
  event_link_repository.insert(event_id, subscriber_id)
  
@pytest.mark.skip("Select in DB")
def test_select_event():
  event_id = 12
  subscriber_id = 18
  event_link_repository = EventosLinkRepository()
  
  event_link = event_link_repository.select_event_link(event_id, subscriber_id)
  print(event_link.link)