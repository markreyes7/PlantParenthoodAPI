from rest_framework  import serializers

from .models import Plant, Fern, Succulent,Vine, Shopper

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ('common_name','family_name', 'botanical_name','plant_type')

class FernSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fern
        fields = ('common_name', 'family_name', 'botanical_name', 'plant_type', 'sun_exposure', 'native_area', 'watering_schedule')

class SucculentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Succulent
        fields = ('common_name', 'family_name', 'botanical_name', 'plant_type', 'sun_exposure', 'native_area', 'watering_schedule')

class VineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vine
        fields = ('common_name', 'family_name', 'botanical_name', 'plant_type', 'sun_exposure', 'native_area', 'watering_schedule')
class ShopperSerializer(serializers.HyperlinkedModelSerializer):
    items = PlantSerializer(many=True)
    class Meta:
        model = Shopper
        fields =('name', 'id', 'items')