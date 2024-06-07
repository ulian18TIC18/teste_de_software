import pytest
from unittest.mock import Mock

class EmailService:
    def send_email(self, recipient, subject, body):
        pass

class EventHandler:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def handle_event(self, event):
        self.email_service.send_email('test@example.com', 'Event Occurred', str(event))

def teste_handle_event_valido():
    email_service_mock = Mock()
    event_handler = EventHandler(email_service_mock)
    event = {'type': 'test_event'}

    event_handler.handle_event(event)

    email_service_mock.send_email.assert_called_once_with('test@example.com', 'Event Occurred', str(event))

def teste_handle_event_invalido():
    email_service_mock = Mock()
    event_handler = EventHandler(email_service_mock)
    event = 'invalid_event'

    with pytest.raises(ValueError):
        event_handler.handle_event(event)


