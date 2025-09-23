from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class User_table(models.Model):
    LOGIN=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    pin=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    phone=models.BigIntegerField()

class Table_table(models.Model):
    tablename=models.CharField(max_length=200)
    capacity=models.IntegerField()

class Feedback_table(models.Model):
    USER=models.ForeignKey(User_table,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=200)
    date=models.DateField()


class Food_Items_table(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    quantity=models.BigIntegerField(default=1)


class Booking_table(models.Model):
    USER=models.ForeignKey(User_table,on_delete=models.CASCADE)
    TABLE=models.ForeignKey(Table_table,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=200)

class Order_main_table(models.Model):
    USER=models.ForeignKey(User_table,on_delete=models.CASCADE)
    amount=models.FloatField()
    quantity=models.BigIntegerField()
    status=models.CharField(max_length=200)


class Order_sub_table(models.Model):
    ORDERMAIN=models.ForeignKey(Order_main_table,on_delete=models.CASCADE)
    FOOD=models.ForeignKey(Food_Items_table,on_delete=models.CASCADE)
    quantity=models.BigIntegerField()
    amount=models.FloatField()





class Payment_table(models.Model):
    ORDER=models.ForeignKey(Order_main_table,on_delete=models.CASCADE)
    date=models.DateField()
    amount=models.FloatField()
    status=models.CharField(max_length=200)

class Cart_table(models.Model):
    ORDERSUB=models.ForeignKey(Order_sub_table,on_delete=models.CASCADE)
    status=models.CharField(max_length=200,default='cart')
    total_amount=models.FloatField()
    date=models.DateField(default=timezone.now)
