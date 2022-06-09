from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    massage=models.TextField()

class Home(models.Model):
    main_title = models.CharField(max_length=10000)

    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)

    sub_title = models.TextField(max_length=20000)
    def __str__(self):
        return self.main_title