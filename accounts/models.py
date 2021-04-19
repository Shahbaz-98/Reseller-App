from django.db import models

# Create your models here.

class Customers(models.Model):
	name = models.CharField(max_length=200, null = True)
	phone = models.CharField(max_length=200, null = True)
	email = models.CharField(max_length=200, null = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name


class Sellers(models.Model):
	name = models.CharField(max_length=200, null = True)
	phone = models.CharField(max_length=200, null = True)
	email = models.CharField(max_length=200, null = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name

class Resellers(models.Model):
	name = models.CharField(max_length=200, null = True)
	phone = models.CharField(max_length=200, null = True)
	email = models.CharField(max_length=200, null = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name

class Products(models.Model):
	seller = models.ForeignKey(Sellers, null=True, on_delete = models.SET_NULL)
	name = models.CharField(max_length=200, null = True)
	price = models.FloatField(null = True)
	category = models.CharField(max_length=200, null = True)
	pic = models.ImageField(null=True, blank=False)
	description = models.CharField(max_length=200, null = True, blank=True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name

class Orders(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
		)

	customer = models.ForeignKey(Customers, null=True, on_delete = models.SET_NULL)
	reseller = models.ForeignKey(Resellers, null=True, on_delete = models.SET_NULL)
	product = models.ForeignKey(Products, null=True, on_delete = models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add = True, null = True)
	status = models.CharField(max_length=200, null = True, choices=STATUS)
	note = models.CharField(max_length=200, null = True)
	commission = models.FloatField(null = True)

	def __str__(self):
		return self.product.name