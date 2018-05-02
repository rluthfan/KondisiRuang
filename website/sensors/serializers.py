# Create JSON Serializer

from rest_framework import serializers

from .models import Datum

class DatumSerializer(serializers.ModelSerializer):
	"""docstring for DataSerializer"""
	
	class Meta:
		model = Datum
		fields = '__all__'

# class ProcessedDataSerializer(serializers.ModelSerializer):
# 	"""docstring for DataSerializer"""
	
# 	class Meta:
# 		model = ProcessedData
# 		fields = '__all__'