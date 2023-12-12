from django.db import models

# Create your models here.
class Case(models.Model):
    typeChoice = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
        ('type3', 'Type 3'),
        # Add more choices as needed
    ]
        
    Name = models.TextField(max_length=200, db_index=True)
    Type = models.CharField(max_length=20, choices=typeChoice, default='type1', db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    Finished_Date = models.DateTimeField()
    Keyword = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.title