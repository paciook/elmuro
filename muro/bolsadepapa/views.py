from django.shortcuts import render
from django.http import HttpResponse
from bolsadepapa.models import Mensaje

# Create your views here.

def muro(request, msg=""):

	if (msg != ""):
		r = Mensaje(msg=msg)
		r.save()

	muro = Mensaje.objects.all()

	response = ""

	for frase in muro:
		response += frase.msg + "<br>"

	return HttpResponse(response)
