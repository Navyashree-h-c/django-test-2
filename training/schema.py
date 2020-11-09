import graphene
import blog.schema.blog.schema as Blog
import user.schema.user.schema as User

class Query(Blog.Query,User.Query,graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class Mutations(Blog.Mutations,User.Mutations,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutations)