import graphene
from graphene_django.types import DjangoObjectType
from blog.model.blog.blog_model import BlogModel
from django.utils import timezone

class Blog(DjangoObjectType):

    # user_blogs = graphene.List(BlogModel)

    class Meta:
        model = BlogModel

    # def resolve_user_blogs(self, info):
    #     '''
    #     resolve_user_blogs: return BlogModel objects
    #     '''
    #     return BlogModel.objects.all()

#Mutation Insertion
class CreateBlog(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)
        description = graphene.String()
        posted_by = graphene.String()

    # The class attributes define the response of the mutation
    blog = graphene.Field(Blog)

    def mutate(self, info, name, description, posted_by):
        '''
        mutate: returns creates blog info

        Args:
            name: name
            description: description
            posted_by: posted_by
        '''
        new_blog = BlogModel(
            name = name,
            description = description,
            posted_by = posted_by,
            posted_on = timezone.now(),
        )

        new_blog.save()
        # Notice we return an instance of this mutation
        return CreateBlog(blog=new_blog)

#Updating
class UpdateBlog(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        description = graphene.String()
        posted_by = graphene.String()
        id = graphene.Int()

    # The class attributes define the response of the mutation
    message = graphene.String()

    def mutate(self, info, id, description, posted_by):
        '''
        mutate: returns updated blog info

        Args:
            id: integer id
            description: description
            posted_by: posted_by
        '''
        old_blog = BlogModel.objects.get(pk=id)
        old_blog.description = description
        old_blog.posted_by = posted_by
        old_blog.posted_on = timezone.now()

        old_blog.save()
        # Notice we return an instance of this mutation
        return UpdateBlog(message="Blog info updated")

#Deleting
class DeleteBlog(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.Int()

    # The class attributes define the response of the mutation
    message = graphene.String()

    def mutate(self, info, id):
        '''
        mutate: deletes blog

        Args:
            id: integer id
        '''
        old_blog = BlogModel.objects.get(pk=id)
        old_blog.delete()
        # Notice we return an instance of this mutation
        return DeleteBlog(message="Blog Deleted")