# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.query import QuerySet
# from django_group_by import GroupByMixin

# Create your models here.
# class DatumQuerySet(QuerySet, GroupByMixin):
#     pass

class Datum(models.Model):
	# objects = DatumQuerySet.as_manager()

	date_n = models.DateField()
	time_n = models.TimeField()
	mode_belajar = models.CharField(max_length=20)
	sensor_id = models.IntegerField()
	temperature = models.FloatField()
	recommend_temperature = models.TextField()
	humidity = models.FloatField()
	recommend_humidity = models.TextField()
	light_intensity = models.IntegerField()
	recommend_light = models.TextField()
	sound_intensity = models.IntegerField()
	recommend_sound = models.TextField()
	
        def __str__(self):
		stringprint = 'Date '
		stringprint += str(self.date_n) + ', '
		stringprint += 'Time = '
		stringprint += str(self.time_n)
		
		return (stringprint)

##	def __str__(self):
##		stringprint = 'Sensor ID: '
##		stringprint += str(self.sensor_id) + ', '
##		stringprint += 'Temperature = '
##		stringprint += str(self.temperature) + ', '
##		stringprint += 'Humidity = '
##		stringprint += str(self.humidity) + ', '
##		stringprint += 'Light Intensity = '
##		stringprint += str(self.light_intensity) + ', '
##		stringprint += 'Sound Level = '
##		stringprint += str(self.sound_intensity)
##		return (stringprint)

# class ProcessedData(models.Model):
# 	temperature = models.FloatField()
# 	time_n = models.TimeField()