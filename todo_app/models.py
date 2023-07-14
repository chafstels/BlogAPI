from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='to_do', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title[:50]} -> {self.owner}"
