# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ciudad(models.Model):
	Nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.Nombre

class sede(models.Model):
	Nombre = models.CharField(max_length=255)
	imagen = models.ImageField(blank=True)
	ciudad = models.ForeignKey(ciudad)
	def __str__(self):
		return self.Nombre


class entrenador(models.Model):
	Nombre = models.CharField(max_length=255)
	Apellido = models.CharField(max_length=255)
	foto = models.ImageField(blank=True)
	sede = models.ForeignKey(sede)
	trx = "trx"
	funcional = "funcional"
	culturismo = "culturismo"
	powerlifter = "powerlifter"
	especialidad = (
	(trx,"trx"),
	(funcional,"funcional"),
	(culturismo,"culturismo"),
	(powerlifter,"powerlifter"),)
	Especialidad = models.CharField(max_length=255,choices=especialidad,
		default=trx)
	def __str__(self):
 		return '%s , %s' % (self.Nombre, self.sede.Nombre)


class estudiante(models.Model):
	cedula = models.CharField(max_length=11)
	Nombre = models.CharField(max_length=255)
	Apellido = models.CharField(max_length=255)
	foto = models.ImageField(blank=True)
	sede = models.ForeignKey(sede)
	telefono = models.CharField(max_length=7)
	direccion = models.CharField(max_length=255)
	correo = models.EmailField(max_length=255)
	def __str__(self):
		return '%s , %s' % (self.Nombre, self.Apellido)


class salon(models.Model):
	Nombre = models.CharField(max_length=200)
	tipo = models.BooleanField(default=False)
	sede = models.ForeignKey(sede)
	def __str__(self):
		return '%s , %s' % (self.Nombre, self.sede.Nombre)


class clase(models.Model):
	entrenador = models.ForeignKey(entrenador)
	salon = models.ForeignKey(salon)
	fecha = models.DateTimeField(max_length=255)
	Capacidad = models.IntegerField(default=30)
	def __str__(self):
		return '%s,%s,%s,' % (self.fecha ,self.entrenador.Nombre , self.salon.Nombre)

class ClaseEstudiante(models.Model):
	clase = models.ForeignKey(clase)
	estudiante = models.ForeignKey(estudiante)
	def __str__(self):
		return '%s , %s' % (self.estudiante.Nombre, self.clase.fecha)

