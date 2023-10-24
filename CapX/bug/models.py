from django.db import models

class Bug(models.Model):
    PRIORITY_CHOICES = [
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low'),
    ]

    description = models.TextField()
    bug_type = models.CharField(max_length=100, choices=[
        ('error', 'Error'),
        ('new_feature', 'New Feature'),
        ('other', 'Other'),
    ])
    report_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('TO DO', 'To Do'),
        ('IN PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ])
    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
