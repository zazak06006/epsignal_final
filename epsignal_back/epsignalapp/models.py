from django.db import models

class Info(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Problem(models.Model):
    PROBLEM_TYPES = [
        ('technique', 'Problème Technique'),
        ('moral', ' Problèm"e morale'),
        ('autre','Autre problème'),
    ]

    problem_type = models.CharField(max_length=50, choices=PROBLEM_TYPES)
    email = models.EmailField()
    description = models.TextField()

class Newsletter(models.Model):
    email = models.CharField(max_length=50)