from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Student(models.Model):
    Name = models.CharField(max_length=200,)
    Gender = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Age_field = models.IntegerField(default=0)


    def __str__(self):
        return self.Name







