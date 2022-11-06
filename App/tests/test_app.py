import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User, Notification
from App.models import Recommendation
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
    get_user,
    get_user_by_username,
    update_user,
    create_recommendation_cli,
    get_all_recommendation_json,
    create_notification_cli,
    get_all_notification_json
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''

class RecommendationUnitTests(unittest.TestCase):

    def test_new_recommendation(self):
        recommendation = Recommendation("1", "This is a recommendation for bob", "2")
        assert recommendation.id == "1"
        assert recommendation.letter == "This is a recommendation for bob"
        assert recommendation.recipient_id == "2"
        
    def test_recommendation_toJSON(self):
        recommendation = Recommendation("1", "This is a recommendation for bob", "2")
        recommendation_json = recommendation.toJSON()
        self.assertDictEqual(recommendation_json, {"ID": "1", "Letter": "This is a recommendation for bob", "recipient_id": "2", "sender": None  })


class NotificationUnitTests(unittest.TestCase):

    def test_new_notification(self):
        notification = Notification("1", "This is a request for a recommendation from ms jade", "2")
        assert notification.id == "1"
        assert notification.message == "This is a request for a recommendation from ms jade"
        assert notification.recipient_id == "2"

    def test_notification_toJSON(self):
        notification = Notification("1", "This is a request for a recommendation from ms jade", "2")
        notification_json = notification.toJSON()
        self.assertDictEqual(notification_json, {"ID": "1", "message": "This is a request for a recommendation from ms jade", "recipient_id": "2", "sender": None  })


class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bob@mail.com", "bobpass", "teacher")
        assert user.username == "bob"
        assert user.role == "teacher"
        assert user.email == "bob@mail.com"
        assert user.password != "bobpass"

    # pure function no side effects or integrations called
    def test_toJSON(self):
        user = User("bob", "bob@mail.com", "bobpass", "teacher")
        user_json = user.toJSON()
        print(user_json)
        self.assertDictEqual(user_json, {"id":None, "username":"bob", "role": "teacher", "email": "bob@mail.com"})
    
    def test_hashed_password(self):
        password = "bobpass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", "bob@mail.com", "bobpass", "teacher")
        assert user.password != password

    def test_check_password(self):
        password = "bobpass"
        user = User("bob", "bob@mail.com", "bobpass", "teacher")
        assert user.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


def test_authenticate():
    user = create_user("bob", "bob@mail.com", "bobpass", "teacher")
    assert authenticate("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "rob@mail.com", "robpass", "teacher")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        print(users_json)
        self.assertListEqual([{"id": 1, "username": "bob", "role": "teacher", "email": "bob@mail.com"}, {"id": 2, "username": "rick", "role": "teacher", "email": "rob@mail.com"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "rob")
        user = get_user(1)
        assert user.username == "rob"

class RecommendationIntegrationTests(unittest.TestCase):

    def test_create_recommendation(self):
        recommendation = create_recommendation_cli( "This is a recommendation for bob", "2", "1")
        assert recommendation.id == 1
        assert recommendation.letter == "This is a recommendation for bob"
        assert recommendation.recipient_id ==  2

    def test_get_all_reccommendation_json(self):
        recommendation_json = get_all_recommendation_json()
        self.assertListEqual([{"ID": 1, "Letter": "This is a recommendation for bob", "recipient_id": 2, "sender": None}], recommendation_json)


class NotificationIntegrationTests(unittest.TestCase):

    def test_create_notification(self):
        notification = create_notification_cli( "This is a request for a recommendation from ms jade", "2", "1")
        assert notification.id == 1
        assert notification.message == "This is a request for a recommendation from ms jade"
        assert notification.recipient_id ==  2

    def test_get_all_notification_json(self):
        notification_json = get_all_notification_json()
        self.assertListEqual([{"ID":1, "message": "This is a request for a recommendation from ms jade", "recipient_id": 2, "sender": None}], notification_json)