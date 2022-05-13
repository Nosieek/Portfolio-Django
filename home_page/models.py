from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.FilePathField(path="/img")