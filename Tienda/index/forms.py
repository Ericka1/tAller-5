from django import forms

class SesionForm(forms.Form):
	usuario = forms.CharField(max_length=20,required=True,label="",widget=(forms.TextInput(attrs={"placeholder":"Nombre de Usuario","class":"form-control"})))
	password = forms.CharField(max_length=20,required=True,label="",widget=(forms.PasswordInput(attrs={"placeholder":"Clave","class":"form-control"})))