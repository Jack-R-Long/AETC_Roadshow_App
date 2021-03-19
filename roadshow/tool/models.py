from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    rank = models.CharField(max_length=5)


class Plan_of_insntruction(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.IntegerField(default=0)
