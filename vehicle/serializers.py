from rest_framework import serializers

from vehicle.models import Car, Moto, Milage


class CarSerializer(serializers.ModelSerializer):
    #last_milage = serializers.IntegerField(source='milage_set.all.first.milage')

    class Meta:
        model = Car
        fields = '__all__'

class MotoSerializer(serializers.ModelSerializer):
    # last_milage =

    class Meta:
        model = Moto
        fields = '__all__'


class MilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = '__all__'
