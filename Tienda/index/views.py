from django.shortcuts import render,redirect
from .forms import SesionForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import Context
from django.db.models import Sum
from .models import Ventas,Vendedor,Sucursal
import MySQLdb

def plantilla_cargada(request):
	
	return render(request,"homepage.html")


def sesion(request):
	form = SesionForm(request.POST or None)
	if request.method == "POST":	
		if form.is_valid():
			data = form.cleaned_data
			nombre_usuario = data.get("usuario")
			password_usuario =data.get("password")
			acceso = authenticate(username=nombre_usuario,password=password_usuario)
			if acceso is not None:
				login(request,acceso)
				return HttpResponseRedirect("/gerencia")
			else:
				return HttpResponseRedirect("/")


		else:
			form = SesionForm()

	var ={"form":form,}

	return render(request,"login.html",var)


def cerrar_sesion(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

@login_required
def gerencial(request):
	db = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	cursor = db.cursor()
	cursor.execute("SELECT COUNT(iv.id_venta) AS cantidad FROM tienda.index_ventas iv, tienda.index_vendedor v,tienda.index_sucursal s WHERE iv.vendedor_id=v.id_vendedor AND	v.sucursal_id=s.id_sucursal GROUP BY s.sucursal ORDER BY s.id_sucursal ASC") 
	ventas = [row[0] for row in cursor.fetchall()]
	db.close()
	prod=fun_prod()
	mont=fun_mont_vent()
	mat=fun_mont_prod_mat()
	suc1=fun_mont_prod_suc1()
	suc2=fun_mont_prod_suc2()
	suc3=fun_mont_prod_suc3()
	empmat=fun_vent_emp_mat()
	empsuc1=fun_vent_emp_suc1()
	empsuc2=fun_vent_emp_suc2()
	empsuc3=fun_vent_emp_suc3()
	print(mat[5])
	context = {'ventas': ventas[0],'ventas1':ventas[1],
			   'ventas2':ventas[2],'ventas3':ventas[3],
			   'producto1': prod[0],'producto2':prod[1],
			   'producto3':prod[2],'producto4':prod[3],
			   'producto5':prod[4],'producto6':prod[5],
			   'producto7':prod[6],'producto8':prod[7],
			   'producto9':prod[8],'producto10':prod[9],
			   'producto11':prod[10],'producto12':prod[11],
			   'producto13':prod[12],'producto14':prod[13],
			   'montmat1':mont[0],'montmat2':mont[1],
			   'montmat3':mont[2],'montsuc11':mont[3],
			   'montsuc12':mont[4],'montsuc13':mont[5],
			   'montsuc21':mont[6],'montsuc22':mont[7],
			   'montsuc23':mont[8],'montsuc31':mont[9],
			   'montsuc32':mont[10],'montsuc33':mont[11],
			   'promat11':mat[0],'promat12':mat[1],
			   'promat13':mat[2],'promat21':mat[3],
			   'promat22':mat[4],'promat23':mat[5],
			   'promat31':mat[6],'promat32':mat[7],
			   'promat33':mat[8],'prosuc111':suc1[0],
			   'prosuc112':suc1[1],'prosuc113':suc1[2],
			   'prosuc121':suc1[3],'prosuc122':suc1[4],
			   'prosuc123':suc1[5],'prosuc131':suc1[6],
			   'prosuc132':suc1[7],'prosuc133':suc1[8],
			   'prosuc211':suc2[0],'prosuc212':suc2[1],
			   'prosuc213':suc2[2],'prosuc221':suc2[3],
			   'prosuc222':suc2[4],'prosuc223':suc2[5],
			   'prosuc231':suc2[6],'prosuc232':suc2[7],
			   'prosuc233':suc2[8],'prosuc311':suc3[0],
			   'prosuc312':suc3[1],'prosuc313':suc3[2],
			   'prosuc321':suc3[3],'prosuc322':suc3[4],
			   'prosuc323':suc3[5],'prosuc331':suc3[6],
			   'prosuc332':suc3[7],'prosuc333':suc3[8],
			   'empmat1':empmat[0],'empmat2':empmat[1],
			   'empmat3':empmat[2],'empsuc11':empsuc1[0],
			   'empsuc12':empsuc1[1],'empsuc21':empsuc2[0],
			   'empsuc22':empsuc2[1],'empsuc23':empsuc2[2],
			   'empsuc31':empsuc3[0],'empsuc32':empsuc3[1]}
	return render(request,"gerencia.html",context)

def fun_prod():
	db_prod = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_prod=db_prod.cursor()
	c_prod.execute("SELECT SUM(iv.cantidad) AS cantidad FROM tienda.index_ventas iv,tienda.index_vendedor v,tienda.index_sucursal s where iv.vendedor_id=v.id_vendedor and v.sucursal_id=s.id_sucursal and year(iv.fecha)=year(now()) GROUP BY iv.producto ORDER BY iv.producto ASC")
	producto = [b[0] for b in c_prod.fetchall()]
	db_prod.close()
	return producto

def fun_mont_vent():
	db_mont_vent = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_mont_vent=db_mont_vent.cursor()
	c_mont_vent.execute("SELECT SUM(iv.total) AS MONTO FROM tienda.index_ventas iv,tienda.index_vendedor v WHERE iv.vendedor_id=v.id_vendedor GROUP BY MONTH(iv.fecha),v.sucursal_id ORDER BY v.sucursal_id,MONTH(iv.fecha) ASC")
	monto_venta = [m[0] for m in c_mont_vent.fetchall()]
	c_mont_vent.close()
	return monto_venta

def fun_mont_prod_mat():
	db_prod_mat = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_prod_mat=db_prod_mat.cursor()
	c_prod_mat.execute("(SELECT sum(iv.total) AS total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor and v.sucursal_id='001' and MONTH(iv.fecha)='1' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3) union (SELECT sum(iv.total) total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor   and v.sucursal_id='001'   and MONTH(iv.fecha)='2' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3) union (SELECT sum(iv.total) total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor   and v.sucursal_id='001'   and MONTH(iv.fecha)='3' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3)")
	prod_mat = [mat[0] for mat in c_prod_mat.fetchall()]
	c_prod_mat.close()
	return prod_mat

def fun_mont_prod_suc1():
	db_prod_suc1 = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_prod_suc1=db_prod_suc1.cursor()
	c_prod_suc1.execute("(SELECT sum(iv.total) AS total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor and v.sucursal_id='002' and MONTH(iv.fecha)='1' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3) union (SELECT sum(iv.total) total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor   and v.sucursal_id='002'   and MONTH(iv.fecha)='2' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3) union (SELECT sum(iv.total) total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor   and v.sucursal_id='002'   and MONTH(iv.fecha)='3' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3)")
	prod_suc1 = [suc1[0] for suc1 in c_prod_suc1.fetchall()]
	c_prod_suc1.close()
	return prod_suc1

def fun_mont_prod_suc2():
	db_prod_suc2 = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_prod_suc2=db_prod_suc2.cursor()
	c_prod_suc2.execute("(SELECT sum(iv.total) AS total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor and v.sucursal_id='003' and MONTH(iv.fecha)='1' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3) union (SELECT sum(iv.total) total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor   and v.sucursal_id='003'   and MONTH(iv.fecha)='2' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3) union (SELECT sum(iv.total) total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor   and v.sucursal_id='003'   and MONTH(iv.fecha)='3' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3)")
	prod_suc2 = [suc2[0] for suc2 in c_prod_suc2.fetchall()]
	c_prod_suc2.close()
	return prod_suc2	

def fun_mont_prod_suc3():
	db_prod_suc3 = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_prod_suc3=db_prod_suc3.cursor()
	c_prod_suc3.execute("(SELECT sum(iv.total) AS total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor and v.sucursal_id='004' and MONTH(iv.fecha)='1' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3) union (SELECT sum(iv.total) total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor   and v.sucursal_id='004'   and MONTH(iv.fecha)='2' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3) union (SELECT sum(iv.total) total FROM tienda.index_ventas iv, tienda.index_vendedor v where iv.vendedor_id=v.id_vendedor   and v.sucursal_id='004'   and MONTH(iv.fecha)='3' group by iv.producto,MONTH(iv.fecha) order by sum(iv.total) desc limit 0,3)")
	prod_suc3 = [suc3[0] for suc3 in c_prod_suc3.fetchall()]
	c_prod_suc3.close()
	return prod_suc3

def fun_vent_emp_mat():
	db_emp_mat = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_emp_mat=db_emp_mat.cursor()
	c_emp_mat.execute("SELECT sum(iv.total) as VENTAS FROM tienda.index_ventas iv,tienda.index_vendedor v WHERE iv.vendedor_id= v.id_vendedor AND v.sucursal_id='001' GROUP BY iv.vendedor_id ORDER BY iv.vendedor_id ASC")
	emp_mat = [emat[0] for emat in c_emp_mat.fetchall()]
	c_emp_mat.close()
	return emp_mat

def fun_vent_emp_suc1():
	db_emp_suc1 = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_emp_suc1=db_emp_suc1.cursor()
	c_emp_suc1.execute("SELECT sum(iv.total) as VENTAS FROM tienda.index_ventas iv, tienda.index_vendedor v WHERE iv.vendedor_id= v.id_vendedor AND v.sucursal_id='002' GROUP BY iv.vendedor_id ORDER BY iv.vendedor_id ASC")
	emp_suc1 = [esuc1[0] for esuc1 in c_emp_suc1.fetchall()]
	c_emp_suc1.close()
	return emp_suc1

def fun_vent_emp_suc2():
	db_emp_suc2 = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_emp_suc2=db_emp_suc2.cursor()
	c_emp_suc2.execute("SELECT sum(iv.total) as VENTAS FROM tienda.index_ventas iv, tienda.index_vendedor v WHERE iv.vendedor_id= v.id_vendedor AND v.sucursal_id='003' GROUP BY iv.vendedor_id ORDER BY iv.vendedor_id ASC")
	emp_suc2 = [esuc2[0] for esuc2 in c_emp_suc2.fetchall()]
	c_emp_suc2.close()
	return emp_suc2	

def fun_vent_emp_suc3():
	db_emp_suc3 = MySQLdb.connect(user='root', db='tienda', passwd='123456', host='localhost')
	c_emp_suc3=db_emp_suc3.cursor()
	c_emp_suc3.execute("SELECT sum(iv.total) as VENTAS FROM tienda.index_ventas iv, tienda.index_vendedor v WHERE iv.vendedor_id= v.id_vendedor AND v.sucursal_id='004' GROUP BY iv.vendedor_id ORDER BY iv.vendedor_id ASC")
	emp_suc3 = [esuc3[0] for esuc3 in c_emp_suc3.fetchall()]
	c_emp_suc3.close()
	return emp_suc3	

def mostrar_menu(request):
	return render(request,"menu.html")
