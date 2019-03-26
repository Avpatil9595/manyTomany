from django.db import models

class Customer(models.Model):

    Cid=models.IntegerField()
    Cname=models.CharField(max_length=100)
    Cgen=models.CharField(max_length=5)
    Cadd=models.CharField(max_length=100)



class C(models.Model):
    name=models.CharField(max_length=100)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
# Create your models here.
