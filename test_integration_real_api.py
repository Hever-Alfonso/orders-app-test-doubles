from order_service import create_order
from database import SessionLocal, Base, engine
from user_repository import JsonPlaceholderUserRepository

Base.metadata.create_all(bind=engine)

class DummyLogger:
    def log(self, msg):
        pass  # no hace nada, solo cumple el parametro obligatorio

class NullNotifier:
    def send(self, to, message):
        pass  # no hace nada, solo cumple el parametro obligatorio

def test_create_order_integration_real_api():
    db = SessionLocal()
    order = create_order(1, 50, NullNotifier(), DummyLogger(), db, JsonPlaceholderUserRepository())
    assert order.status == 'CREATED'
    db.close()
