import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app(testing=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
    
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def add_two_planets():
    planet_one = Planet(
        name="Saturn",
        description="Rings",
        order_from_sun="6th from sun"
    )
    planet_two = Planet(
        name="Mars",
        description="Hot red",
        order_from_sun="4th from sun"
    )
    db.session.add_all([planet_one, planet_two])
    db.session.commit()
