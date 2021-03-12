from django.db import models
# Create your models here.


class Url(models.Model):
    shortened = models.CharField(max_length=5)
    url_link = models.URLField(max_length=50)

    def __str__(self):
        return f"My short is {self.shortened}, my link is {self.url_link}"