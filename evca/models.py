from django.db import models
from django.utils import timezone


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name + " " + self.surname



class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('event date', default=timezone.now())

    def __str__(self) -> str:
        return self.name
    

class Expenses(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )
    debt = models.FloatField(default=0)
    due = models.FloatField(default=0)

    def __str__(self) -> str:
        result = str(self.member) + " " + str(self.event) + " " + str(self.debt) + " " + str(self.due)
        return result