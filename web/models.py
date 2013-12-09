from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Action(models.Model):
    name = models.CharField(max_length=200, null=False)
    command = models.CharField(max_length=1000, null=False)
    user = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return self.name

class Execution(models.Model):
    action = models.ForeignKey(Action, null=False)
    user = models.ForeignKey(User, null=False)
    output = models.TextField(null=False)
    error = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)