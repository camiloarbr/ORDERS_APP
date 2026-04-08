from order_service import create_order

class StubUserRepository:
    def get_user_email(self, user_id):
        return "stub.user@fake.local"


class StubDB:
    def __init__(self):
        self.added = None
        self.committed = False

    def add(self, order):
        self.added = order

    def commit(self):
        self.committed = True

class DummyLogger:
    def __init__(self):
        self.messages = []

    def log(self, msg):
        self.messages.append(msg)

class NullNotifier:
    def __init__(self):
        self.notifications = []

    def send(self, to, message):
        self.notifications.append((to, message))

def test_create_order_with_stub():
    db = StubDB()
    logger = DummyLogger()
    notifier = NullNotifier()

    order = create_order(10, 200, notifier, logger, db, StubUserRepository())

    assert order.status == 'CREATED'
    assert order.user_email == "stub.user@fake.local"
    assert db.added is order
    assert db.committed is True
    assert logger.messages == ["Creating order for stub.user@fake.local"]
    assert notifier.notifications == [
        ("stub.user@fake.local", "Order created")
    ]
