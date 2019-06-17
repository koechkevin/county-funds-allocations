from . import models

amount = 0
number_of_sub_counties = 1
try:
    allocation = models.Allocation.objects.all()
    for each in allocation:
        amount = each.__dict__['amount']
except Exception as ex:
    pass


def ward_allocations(key):
    ward_count = models.Ward.objects.count()
    number_of_wards = ward_count if ward_count > 0 else 1
    ward_allocation = amount / number_of_wards
    return ward_allocation


def sub_county_allocations(key):
    my_wards = models.Ward.objects.filter(sub_county=key).count()
    ward_allocation = ward_allocations(key)
    sub_county_allocation = ward_allocation * my_wards
    return sub_county_allocation


def location_allocations(key):
    location = models.Location.objects.filter(pk=key)
    my_ward = 0
    for e in location:
        my_ward = e.ward.__dict__['id']
    number_of_locations_in_my_ward = models.Location.objects.filter(ward_id=my_ward).count()
    if number_of_locations_in_my_ward == 0:
        number_of_locations_in_my_ward = 1
    location_allocation = ward_allocations(my_ward) / number_of_locations_in_my_ward
    return location_allocation


def sub_location_allocations(key):
    sub_location = models.SubLocation.objects.filter(pk=key)
    my_location = 0
    for i in sub_location:
        my_location = i.location.__dict__['id']
    sub_locations_in_my_ward = models.SubLocation.objects.filter(location_id=my_location).count()
    if sub_locations_in_my_ward == 0:
        sub_locations_in_my_ward = 1
    sub_location_allocation = location_allocations(my_location) / sub_locations_in_my_ward
    return sub_location_allocation


def village_allocations(key):
    village = models.Village.objects.filter(pk=key)
    my_sub_location = 0
    for i in village:
        my_sub_location = i.sub_location.__dict__['id']
    villages_in_my_sub_location = models.Village.objects.filter(sub_location_id=my_sub_location).count()
    if villages_in_my_sub_location == 0:
        villages_in_my_sub_location = 1
    village_allocation = sub_location_allocations(my_sub_location) / villages_in_my_sub_location
    return village_allocation
