from django.db import models

class UserModel(models.Model):
    name = models.TextField()
    description = models.TextField()
    email = models.EmailField()
    mobile = models.TextField()
    posted_by = models.TextField()
    posted_on = models.DateTimeField()

    @staticmethod
    def get_list_of_users():
        return UserModel.objects.all()

    def get_user_by_id(id):
        return UserModel.objects.get(pk=id)