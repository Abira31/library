from graphene import Field,Mutation,String
from django.contrib.auth.models import User
from .types import UserType

class UserCreate(Mutation):
    user = Field(UserType)

    class Arguments:
        username = String(required=True)
        password = String(required=True)
        email = String(required=True)

    def mutate(self,info,username,password,email):
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        return UserCreate(user=user)
