from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Tag(models.Model):
#     value = models.CharField(max_length=100,unique=True)

#     def __str__(self):
#         return self.value

class Task(models.Model):

    STATUS_CHOICES=(
        ('OPEN','Open'),
        ('WORKING','Working'),
        ('DONE','Done'),
        ('OVERDUE','Overdue'),
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    # tags = models.ManyToManyField(Tag, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['timestamp']