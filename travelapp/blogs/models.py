from django.db import models


# class Tag(models.Model):
#     name = models.CharField(max_length=256)

#     def __str__(self):
#         return self.name
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add= True)
    updatedAt = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title