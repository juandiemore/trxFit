# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import registroForm,ClaseEstudianteForm
from django.shortcuts import render, get_object_or_404
from .models import ciudad,sede,entrenador,clase,ClaseEstudiante

def inicio(request):
	
	template = loader.get_template('inicio.html')
	contex = {
	
	}
	return HttpResponse(template.render(contex, request))

def sedes(request):
	sedess = sede.objects.order_by('id')
	template = loader.get_template('sedes.html')
	contex = {
	'sedess': sedess
	}
	return HttpResponse(template.render(contex, request))

def entrenadores(request):
	entrenadorr = entrenador.objects.order_by('id')
	template = loader.get_template('entrenador.html')
	contex = {
	'entrenadorr' : entrenadorr
	}
	return HttpResponse(template.render(contex, request))

def Clase(request):
	clasee = clase.objects.order_by('id')
	template = loader.get_template('clases.html')
	contex = {
	'clasee': clasee 
	}
	return HttpResponse(template.render(contex, request))


class Registrar(CreateView):
	model = User
	template_name = 'registrar.html'
	form_class = registroForm
	success_url = reverse_lazy('inicio')

def unirseAclase(request):
	if request.method == 'POST':
		form = ClaseEstudianteForm(request.POST)
		if form.is_valid():
			ClaseEstudiante = form.save(commit=False)
			ClaseEstudiante.save()
			return HttpResponseRedirect('/')
	else:
		form = ClaseEstudianteForm(request.POST , request.FILES)
		template = loader.get_template('unirse.html')
		contex = { 'form': form

		}
		return HttpResponse(template.render(contex , request))
		