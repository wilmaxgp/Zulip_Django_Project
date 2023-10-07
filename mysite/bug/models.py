from django.db import models

# Create your models here.

class Bug(models.Model):
    description = models.TextField()
    bug_type = models.CharField(max_length=100)
    report_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('TO DO', 'To Do'),
        ('IN PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
        ])
