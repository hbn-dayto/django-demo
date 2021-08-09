import datetime

from django.db import models
from django.utils import timezone

# Create a database schema (CREATE TABLE statement) for this app:
class Question(models.Model):
    def __str__(self):
        return self.question_text
    # Each field is represented by an instance of a Field class – e.g.
    # CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Create a Python database-access API for accessing QUestion and Choice objects:
  
class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question,
    on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 