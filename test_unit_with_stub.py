from order_service import create_order
from database import SessionLocal
from models import Order

class StubUserRepository:
    def get_user_email(self, user_id):
        # siempre devuelve el mismo email fijo, sin importar el user_id
        return "stub@test.com"

class DummyLogger:
    def log(self, msg):
        pass

class NullNotifier:
    def send(self, to, message):
        pass

def test_create_order_with_stub():
    db = SessionLocal()
    order = create_order(10, 200, NullNotifier(), DummyLogger(), db, StubUserRepository())
    # el estado y el email deben coincidir con lo que devuelve el stub
    assert order.status == 'CREATED'
    assert order.user_email == "stub@test.com"
    
    db.query(Order).delete()
    db.commit()
    db.close()
