from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=200)
    opt1=models.CharField(max_length=100)
    opt2=models.CharField(max_length=100)
    opt3=models.CharField(max_length=100)
    opt4=models.CharField(max_length=100)
    opt1_cnt=models.IntegerField(default=0)
    opt2_cnt=models.IntegerField(default=0)
    opt3_cnt=models.IntegerField(default=0)
    opt4_cnt=models.IntegerField(default=0)

    def __str__(self):
        return self.question
    
    def total(self):
        return self.opt1_cnt+self.opt2_cnt+self.opt3_cnt+self.opt4_cnt