from django.db import models


class SubCounties(models.Model):
    name = models.CharField(max_length=50)


class Allocation(models.Model):
    amount = models.IntegerField()


class Ward(models.Model):
    name = models.CharField(max_length=50)
    sub_county = models.ForeignKey(SubCounties, on_delete=models.CASCADE)


class Location(models.Model):
    name = models.CharField(max_length=50)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)


class SubLocation(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Village(models.Model):
    name = models.CharField(max_length=50)
    sub_location = models.ForeignKey(SubLocation, on_delete=models.CASCADE)
