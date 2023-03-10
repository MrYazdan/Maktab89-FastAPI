from auth.schemas import UserPrivateSchema


users_db: list[UserPrivateSchema] = [
    UserPrivateSchema(**{"id": "1", "username": 'yazdan', "password": '1234', "full_name": "Yazdan yazdani", "age": '23'}),
    UserPrivateSchema(**{"id": "2", "username": 'ali', "password": '654321', "full_name": "Ali Amiri", "age": '43'}),
    UserPrivateSchema(**{"id": "3", "username": 'fatemeh', "password": 'milad', "full_name": "Fatemeh akbari", "age": '12'}),
    UserPrivateSchema(**{"id": "4", "username": 'heydar', "password": 'tehran', "full_name": "heydar mehrabi", "age": '56'}),
    UserPrivateSchema(**{"id": "5", "username": 'arian', "password": 'qwerty', "full_name": "arian rezaii", "age": '32'}),
]
