from order_service import create_order
from database import SessionLocal, Base, engine
from user_repository import JsonPlaceholderUserRepository

Base.metadata.create_all(bind=engine)

class DummyLogger:
    def log(self, msg):
        pass

class NullNotifier:
    def send(self, to, message):
        pass


def test_create_order_with_real_api():
    db = SessionLocal()
    order = create_order(1, 100, NullNotifier(), DummyLogger(), db, JsonPlaceholderUserRepository())
    assert order.status == 'CREATED'
    db.close()
