from . import models, serializers, allocations
from rest_framework import generics


class SubCountyView(generics.ListCreateAPIView):
    queryset = models.SubCounties.objects.all()
    serializer_class = serializers.SubCountiesSerializer


class SubCountyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SubCounties.objects.all()
    serializer_class = serializers.SubCountiesSerializer


class WardView(generics.ListAPIView):
    queryset = models.Ward.objects.all()
    serializer_class = serializers.WardSerializer


class CreateWardView(generics.CreateAPIView):
    queryset = models.Ward.objects.all()
    serializer_class = serializers.WardCreateSerializer


class WardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ward.objects.all()
    serializer_class = serializers.WardSerializer


class LocationView(generics.ListAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer


class CreateLocationView(generics.CreateAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationCreateSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer


class SubLocationView(generics.ListAPIView):
    queryset = models.SubLocation.objects.all()
    serializer_class = serializers.SubLocationSerializer


class CreateSubLocationView(generics.CreateAPIView):
    queryset = models.SubLocation.objects.all()
    serializer_class = serializers.SubLocationCreateSerializer


class SubLocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SubLocation.objects.all()
    serializer_class = serializers.SubLocationSerializer


class VillageView(generics.ListAPIView):
    queryset = models.Village.objects.all()
    serializer_class = serializers.VillageSerializer


class CreateVillageView(generics.CreateAPIView):
    queryset = models.Village.objects.all()
    serializer_class = serializers.VillageCreateSerializer


class VillageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Village.objects.all()
    serializer_class = serializers.VillageSerializer


class AllocationView(generics.ListCreateAPIView):
    queryset = models.Allocation.objects.all()
    serializer_class = serializers.AllocationSerializer


class AllocationDetail(generics.UpdateAPIView):
    queryset = models.Allocation.objects.all()
    serializer_class = serializers.AllocationSerializer
