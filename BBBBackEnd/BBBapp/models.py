from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


# Model for a blog post
class BBBCatalog(models.Model):
# Need to know the specifications for each class. 
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # name = models.CharField(max_length=512)
    # description = models.TextField(max_length=4096)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # overriding toString() for more user friendly output 
    def __str__(self):
        return self.title
