from django.db import models

class Poll(models.Model):
    question=models.TextField()
    option_one=models.CharField(max_length=20,null=True, blank=True)
    option_two=models.CharField(max_length=20,null=True, blank=True)
    option_three=models.CharField(max_length=20,null=True, blank=True)
    count_op1=models.IntegerField(default=0, null=True, blank=True)
    count_op2=models.IntegerField(default=0, null=True, blank=True)
    count_op3=models.IntegerField(default=0, null=True, blank=True)

    def total(self):
        return self.count_op1 + self.count_op2 + self.count_op3
    
    def __str__(self):
        return self.question