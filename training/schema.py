import graphene
import blog.schema.blog.schema as Blog

class Query(Blog.Query,graphene.ObjectType):
    pass

class Mutations(Blog.Mutations,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutations)