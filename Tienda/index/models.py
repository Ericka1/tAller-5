from django.db import models

class Usuarios(models.Model):
	id = models.IntegerField(primary_key=True)
	nombres = models.CharField(max_length=50)
	correo	= models.EmailField()
	mensaje = models.CharField(max_length=300)

class Sucursal(models.Model):
	id_sucursal = models.CharField(primary_key=True, max_length=20)
	sucursal = models.CharField(max_length=50)
	estado = models.CharField(max_length=1)

class Vendedor(models.Model):
	id_vendedor = models.CharField(primary_key=True, max_length=20)
	nombres =models.CharField(max_length=100)
	sucursal = models.ForeignKey(Sucursal,null=True,blank=True)
	estado = models.CharField(max_length=1)

class Ventas(models.Model):
	id_venta = models.IntegerField(primary_key=True)
	cliente = models.CharField(max_length=200)
	direccion = models.CharField(max_length=500)
	vendedor = models.ForeignKey(Vendedor,null=True,blank=True)
	producto = models.CharField(max_length=80)
	cantidad = models.IntegerField()
	valor = models.DecimalField(max_digits=6, decimal_places=3,blank=True,null=True)
	subtotal = models.DecimalField(max_digits=6, decimal_places=3,blank=True,null=True)
	valiva = models.DecimalField(max_digits=6, decimal_places=3,blank=True,null=True)
	total = models.DecimalField(max_digits=6, decimal_places=3,blank=True,null=True)
	fecha = models.DateTimeField()

