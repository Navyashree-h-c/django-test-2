from django.db import models

class BlogModel(models.Model):
    name = models.TextField()
    description = models.TextField()
    posted_by = models.TextField()
    posted_on = models.DateTimeField()

    # @staticmethod
    # def get_list_of_blogs():
    #     return BlogModel.objects.all()

    # def get_blog_by_id(id):
    #     return BlogModel.objects.get(pk=id)