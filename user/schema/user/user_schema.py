import graphene
from graphene_django.types import DjangoObjectType
from user.model.user.user_model import UserModel
from django.utils import timezone

class User(DjangoObjectType):

    class Meta:
        model = UserModel


#Mutation Insertion
class CreateUser(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        description = graphene.String()
        email = graphene.String()
        mobile = graphene.String()
        posted_by = graphene.String()

    # The class attributes define the response of the mutation
    user = graphene.Field(User)

    def mutate(self, info, name, description, email, mobile, posted_by):
        '''
        mutate: returns creates user info

        Args:
            name (String): name
            description (String): description
            email (String): email
            mobile (String): mobile no
            posted_by (String): posted_by
        '''
        new_user = UserModel(
            name = name,
            description = description,
            email = email,
            mobile = mobile,
            posted_by = posted_by,
            posted_on = timezone.now(),
        )

        new_user.save()
        # Notice we return an instance of this mutation
        return CreateUser(user=new_user)

#Updating
class UpdateUser(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        description = graphene.String()
        posted_by = graphene.String()
        id = graphene.Int()

    # The class attributes define the response of the mutation
    message = graphene.String()

    def mutate(self, info, id, description, posted_by):
        '''
        mutate: returns updated user info

        Args:
            id (Integer): integer id
            description (String): description
            posted_by (String): posted_by
        '''
        old_user = UserModel.objects.get(pk=id)
        old_user.description = description
        old_user.posted_by = posted_by
        old_user.posted_on = timezone.now()

        old_user.save()
        # Notice we return an instance of this mutation
        return UpdateUser(message="User info updated")

#Deleting
class DeleteUser(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.Int()

    # The class attributes define the response of the mutation
    message = graphene.String()

    def mutate(self, info, id):
        '''
        mutate: deletes user

        Args:
            id (Integer): integer id
        '''
        old_user = UserModel.objects.get(pk=id)
        old_user.delete()
        # Notice we return an instance of this mutation
        return DeleteUser(message="User Deleted")