from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=150)
    describtion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.task
    
    