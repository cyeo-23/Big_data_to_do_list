
from models.user import User
from services.user_services import UserServices


user = User(firstname='moussa', lastname='YEO', pseudo='dan', password='azerty')
service = UserServices()
print(service.collection)
user = service.add_user(user)
print(user)
