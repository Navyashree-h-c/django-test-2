import graphene
from user.schema.user.user_schema import User, UserModel, CreateUser, UpdateUser, DeleteUser
from user.model.user.user_management_model import UserManagement

class Query(graphene.ObjectType):

    users = graphene.List(   
        User,
        size=graphene.Int(required=True),
        page=graphene.Int(required=True)
    )

    user = graphene.Field(
        User,
        id = graphene.Int(required=True)
    )	    

    def resolve_users(self, info, size, page):
        '''
        resolve_users: return list of users

        Args:
            size: integer size
            page: integer page
        '''

        # blogs =  BlogModel.objects.all()
        # skip = size * (page-1)
        # blogs = blogs[skip:]
        # blogs = blogs[:size]

        # print(BlogModel.objects.filter(id=4))

        # return blogs

        # temp_array = [9,8,7,6,5,4,3,2,1]
        # temp_array = temp_array[3:]
        # temp_array = temp_array[:2]

        # print(temp_array)
        
        return UserManagement.get_list_of_users()


    def resolve_user(self, info, id):
        '''
        resolve_user: return user by id

        Args:
            id (Integer): unique for users
        '''
        return UserManagement.get_user_by_id(id)
        

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()