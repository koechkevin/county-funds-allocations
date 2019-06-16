from rest_framework import serializers
from . import models
from . import allocations


class SubCountiesSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.sub_county_allocation

    class Meta:
        model = models.SubCounties
        fields = ('id', 'name', 'allocation')


class WardSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.ward_allocations(obj.id)

    class Meta:
        model = models.Ward
        fields = ('id', 'name', 'sub_county', 'allocation')
        depth = 1


class WardCreateSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.ward_allocations(obj.id)

    class Meta:
        model = models.Ward
        fields = ('id', 'name', 'sub_county', 'allocation')


class LocationSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.ward_allocations(obj.id)

    class Meta:
        model = models.Location
        fields = ('id', 'name', 'ward', 'allocation')
        depth = 2


class LocationCreateSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.ward_allocations(obj.id)

    class Meta:
        model = models.Location
        fields = ('id', 'name', 'ward', 'allocation')


class SubLocationSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.sub_location_allocations(obj.id)

    class Meta:
        model = models.SubLocation
        fields = ('id', 'name', 'location', 'allocation')
        depth = 3


class SubLocationCreateSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.sub_location_allocations(obj.id)

    class Meta:
        model = models.SubLocation
        fields = ('id', 'name', 'location', 'allocation')


class VillageSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.village_allocations(obj.id)

    class Meta:
        model = models.Village
        fields = ('id', 'name', 'sub_location', 'allocation')
        depth = 4


class VillageCreateSerializer(serializers.ModelSerializer):
    allocation = serializers.SerializerMethodField(read_only=True)

    def get_allocation(self, obj):
        return allocations.village_allocations(obj.id)

    class Meta:
        model = models.Village
        fields = ('id', 'name', 'sub_location', 'allocation')


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Allocation
        fields = ('id', 'amount')
