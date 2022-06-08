from django.db import models

# Create your models here.
class Blog (models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()

    def  _str_(self):
        return self.title