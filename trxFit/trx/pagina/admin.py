# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ciudad,sede,entrenador,estudiante,salon,clase,ClaseEstudiante

@admin.register(ciudad)
class AdminPagina(admin.ModelAdmin):
	list_display = ('id','Nombre')

@admin.register(sede)
class AdminPagina(admin.ModelAdmin):
	list_display = ('id','Nombre')

@admin.register(entrenador)
class AdminPagina(admin.ModelAdmin):
	list_display = ('id','Nombre','especialidad')

@admin.register(estudiante)
class AdminPagina(admin.ModelAdmin):
	list_display = ('id','Nombre','Apellido')

@admin.register(salon)
class AdminPagina(admin.ModelAdmin):
	list_display = ('id','Nombre','sede')

@admin.register(clase)
class AdminPagina(admin.ModelAdmin):
	list_display = ('id','entrenador','salon')

@admin.register(ClaseEstudiante)
class AdminPagina(admin.ModelAdmin):
	list_display = ('id','estudiante','clase')