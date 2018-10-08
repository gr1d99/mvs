from app.authentication.models import Role
import faker

FAKER = faker.Faker()


def create_role(user_id):
    role = Role(name=FAKER.name(), description=FAKER.text(), user_id=None)
    role.user_id = user_id
    role.create()
    return role


def delete_role(role_id):
    role = Role.query.get(role_id)
    role.delete()
