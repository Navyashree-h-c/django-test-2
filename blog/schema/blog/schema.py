import graphene
from blog.schema.blog.blog_schema import Blog, BlogModel, CreateBlog, UpdateBlog, DeleteBlog
from blog.model.blog.blog_management_model import BlogManagement

class Query(graphene.ObjectType):

    blogs = graphene.List(   
        Blog,
        size=graphene.Int(required=True),
        page=graphene.Int(required=True)
    )

    blog = graphene.Field(
        Blog,
        id = graphene.Int(required=True)
    )	    

    def resolve_blogs(self, info, size, page):
        '''
        resolve_blogs: return list of blogs

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
        
        return BlogManagement.get_list_of_blogs()


    def resolve_blog(self, info, id):
        '''
        resolve_blog: return blog by id

        Args:
            id (Integer): unique for blogs
        '''
        return BlogManagement.get_blog_by_id(id)
        

class Mutations(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    update_blog = UpdateBlog.Field()
    delete_blog = DeleteBlog.Field()