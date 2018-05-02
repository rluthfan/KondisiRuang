# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Datum
from .serializers import DatumSerializer
from django.views.generic import View

from numpy import mean
from datetime import datetime, timedelta

import json

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})
    
class HistoricView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts2.html', {})

class ContourView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'heatmap.html', {})

class DatumList(APIView):

    def get(self, request):
        datums = Datum.objects.all()
        serializer = DatumSerializer(datums, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DatumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataDayEndpoint(APIView):
    ''' INI BUAT NGELOMPOKIN 1 HARI TERAKHIR BUAT GRAFIK '''
    def get(self, request):
        # last 1 days
        # datums = Datum.objects.filter(date_n__gte=datetime.now()-timedelta(days=0))
        # datums = Datum.objects.filter(date_n=datetime.now()-timedelta(days=1))
        datums = Datum.objects.filter(date_n=datetime.now())
        # print(datetime.now()-timedelta(days=1))
        # Inisialisasi variable yang mau di-return
        return_with_date = {}
        return_all_dict = {}

        # Temperature
        hour_bucket = set()
        # for dt in day_value:
        for dt in datums:
            hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
        list_data_per_hour = {}
        for hb in hour_bucket:
            list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai temperature
        for dt in datums:
            list_data_per_hour[dt.time_n.hour].append(dt.temperature)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []

        for k, value in list_data_per_hour.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["temperature"] = return_dictionary

        # Humidity
        hour_bucket = set()
        # for dt in day_value:
        for dt in datums:
            hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
        list_data_per_hour = {}
        for hb in hour_bucket:
            list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai humidity
        for dt in datums:
            list_data_per_hour[dt.time_n.hour].append(dt.humidity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []

        for k, value in list_data_per_hour.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["humidity"] = return_dictionary

        # Light Intensity
        hour_bucket = set()
        # for dt in day_value:
        for dt in datums:
            hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
        list_data_per_hour = {}
        for hb in hour_bucket:
            list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai light_intensity
        for dt in datums:
            list_data_per_hour[dt.time_n.hour].append(dt.light_intensity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []

        for k, value in list_data_per_hour.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["light_intensity"] = return_dictionary
        
        # Sound Intensity
        hour_bucket = set()
        # for dt in day_value:
        for dt in datums:
            hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
        list_data_per_hour = {}
        for hb in hour_bucket:
            list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai sound_intensity
        for dt in datums:
            list_data_per_hour[dt.time_n.hour].append(dt.sound_intensity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []

        for k, value in list_data_per_hour.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["sound_intensity"] = return_dictionary

        # return_with_date[str(date)]

        return Response(return_all_dict)

class DataWeekEndpoint(APIView):
    ''' INI BUAT NGELOMPOKIN 7 HARI TERAKHIR BUAT GRAFIK '''
    def get(self, request):
        # last 1 days
        # datums = Datum.objects.filter(date_n__gte=datetime.now()-timedelta(days=0))
        # datums = Datum.objects.filter(date_n=datetime.now()-timedelta(days=1))
        datums = Datum.objects.filter(date_n__gte=datetime.now()-timedelta(days=7))
        # print(datetime.now()-timedelta(days=1))
        # Inisialisasi variable yang mau di-return
        return_with_date = {}
        return_all_dict = {}

        # Temperature
        hour_bucket = set()
        # for dt in day_value:
        for dt in datums:
            hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
        list_data_per_hour = {}
        for hb in hour_bucket:
            list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai temperature
        for dt in datums:
            list_data_per_hour[dt.time_n.hour].append(dt.temperature)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []

        for k, value in list_data_per_hour.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["temperature"] = return_dictionary

        # Humidity
        hour_bucket = set()
        # for dt in day_value:
        for dt in datums:
            hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
        list_data_per_hour = {}
        for hb in hour_bucket:
            list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai humidity
        for dt in datums:
            list_data_per_hour[dt.time_n.hour].append(dt.humidity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []

        for k, value in list_data_per_hour.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["humidity"] = return_dictionary

        # Light Intensity
        hour_bucket = set()
        # for dt in day_value:
        for dt in datums:
            hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
        list_data_per_hour = {}
        for hb in hour_bucket:
            list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai light_intensity
        for dt in datums:
            list_data_per_hour[dt.time_n.hour].append(dt.light_intensity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []

        for k, value in list_data_per_hour.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["light_intensity"] = return_dictionary
        
        # Sound Intensity
        hour_bucket = set()
        # for dt in day_value:
        for dt in datums:
            hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
        list_data_per_hour = {}
        for hb in hour_bucket:
            list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai sound_intensity
        for dt in datums:
            list_data_per_hour[dt.time_n.hour].append(dt.sound_intensity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []

        for k, value in list_data_per_hour.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["sound_intensity"] = return_dictionary

        # return_with_date[str(date)]

        return Response(return_all_dict)

class DataEndpoint(APIView):
    ''' INI BUAT NGELOMPOKIN 7 HARI TERAKHIR BUAT GRAFIK '''
    def get(self, request):
        # last 7 days
        datums = Datum.objects.filter(date_n__gte=datetime.now()-timedelta(days=6))

        # Inisialisasi variable yang mau di-return
        return_all_dict = {}

        # Cari jumlah hari
        day_bucket = set()
        for dt in datums:
            day_bucket.add(str(dt.date_n))
        # Inisialisasi pengelompokan data buat tiap harinya
        list_data_per_date = {}
        for hb in day_bucket:
            list_data_per_date[hb] = []
        # Ngelompokin berdasar harinya
        for dt in datums:
            list_data_per_date[str(dt.date_n)].append(dt)
        ### Ngelompokin jamnya ada jam berapa aja
        # Temperature
        return_all_dict["temperature"] = {}
        for key, day_value in list_data_per_date.items():
            hour_bucket = set()
            for dt in day_value:
                hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
            list_data_per_hour = {}
            for hb in hour_bucket:
                list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai temperature
            for dt in day_value:
                list_data_per_hour[dt.time_n.hour].append(dt.temperature)
            
            return_dictionary = {} 
            return_dictionary["default"] = []
            return_dictionary["labels"] = []

            for k, value in list_data_per_hour.items():
                return_dictionary["default"].append(mean(value))
                return_dictionary["labels"].append(k)

            return_all_dict["temperature"][str(key)] = return_dictionary
        # Humidity
        return_all_dict["humidity"] = {}
        for key, day_value in list_data_per_date.items():
            hour_bucket = set()
            for dt in day_value:
                hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
            list_data_per_hour = {}
            for hb in hour_bucket:
                list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai humidity
            for dt in day_value:
                list_data_per_hour[dt.time_n.hour].append(dt.humidity)

            return_dictionary = {} 
            return_dictionary["default"] = []
            return_dictionary["labels"] = []

            for k, value in list_data_per_hour.items():
                return_dictionary["default"].append(mean(value))
                return_dictionary["labels"].append(k)
            return_all_dict["humidity"][str(key)] = return_dictionary
        # Light Intensity
        return_all_dict["light_intensity"] = {}
        for key, day_value in list_data_per_date.items():
            hour_bucket = set()
            for dt in day_value:
                hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
            list_data_per_hour = {}
            for hb in hour_bucket:
                list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai light_intensity
            for dt in day_value:
                list_data_per_hour[dt.time_n.hour].append(dt.light_intensity)

            return_dictionary = {} 
            return_dictionary["default"] = []
            return_dictionary["labels"] = []

            for k, value in list_data_per_hour.items():
                return_dictionary["default"].append(mean(value))
                return_dictionary["labels"].append(k)
            return_all_dict["light_intensity"][str(key)] = return_dictionary
        # Sound Level
        return_all_dict["sound_intensity"] = {}
        for key, day_value in list_data_per_date.items():
            hour_bucket = set()
            for dt in day_value:
                hour_bucket.add(dt.time_n.hour)
        # Inisialisasi
            list_data_per_hour = {}
            for hb in hour_bucket:
                list_data_per_hour[hb] = []
        # Buat ngerata-rata dan cari modus nilai sound_intensity
            for dt in day_value:
                list_data_per_hour[dt.time_n.hour].append(dt.sound_intensity)

            return_dictionary = {} 
            return_dictionary["default"] = []
            return_dictionary["labels"] = []

            for k, value in list_data_per_hour.items():
                return_dictionary["default"].append(mean(value))
                return_dictionary["labels"].append(k)
            return_all_dict["sound_intensity"][str(key)] = return_dictionary

        return Response(return_all_dict)


class DataMapping(APIView):
    ''' INI BUAT NGELOMPOKIN 15 MENIT TERAKHIR BUAT HEAT MAP '''
    def get(self, request):
        datums = Datum.objects.filter(time_n__gte=datetime.now()+timedelta(hours=7)-timedelta(minutes=15))
        
        # Inisialisasi variable yang mau di-return
        return_all_dict = {}

        # Kelompokin berdasar sensor_id
        sensor_id_bucket = set()
        for dt in datums:
            sensor_id_bucket.add(str(dt.sensor_id))
        
        # Temperature
        # Inisialisasi pengelompokan data buat tiap Sensor ID
        list_data_per_id = {}
        for hb in sensor_id_bucket:
            list_data_per_id[hb] = []
        # Ngelompokin berdasar Sensor ID
        for dt in datums:
            list_data_per_id[str(dt.sensor_id)].append(dt.temperature)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []
        for k, value in list_data_per_id.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["temperature"] = return_dictionary

        # Humidity
        # Inisialisasi pengelompokan data buat tiap Sensor ID
        list_data_per_id = {}
        for hb in sensor_id_bucket:
            list_data_per_id[hb] = []
        # Ngelompokin berdasar Sensor ID
        # Temperature
        for dt in datums:
            list_data_per_id[str(dt.sensor_id)].append(dt.humidity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []
        for k, value in list_data_per_id.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["humidity"] = return_dictionary

        # Light Intensity
        # Inisialisasi pengelompokan data buat tiap Sensor ID
        list_data_per_id = {}
        for hb in sensor_id_bucket:
            list_data_per_id[hb] = []
        # Ngelompokin berdasar Sensor ID
        # Temperature
        for dt in datums:
            list_data_per_id[str(dt.sensor_id)].append(dt.light_intensity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []
        for k, value in list_data_per_id.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["light_intensity"] = return_dictionary

        # Sound Level
        # Inisialisasi pengelompokan data buat tiap Sensor ID
        list_data_per_id = {}
        for hb in sensor_id_bucket:
            list_data_per_id[hb] = []
        # Ngelompokin berdasar Sensor ID
        # Temperature
        for dt in datums:
            list_data_per_id[str(dt.sensor_id)].append(dt.sound_intensity)

        return_dictionary = {} 
        return_dictionary["default"] = []
        return_dictionary["labels"] = []
        for k, value in list_data_per_id.items():
            return_dictionary["default"].append(mean(value))
            return_dictionary["labels"].append(k)

        return_all_dict["sound_intensity"] = return_dictionary

        return Response(return_all_dict)
