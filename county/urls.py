from django.urls import path
from . import views

app_name = "county"
urlpatterns = [
    path('subcounties', views.SubCountyView.as_view(), name='subcounty'),
    path('subcounties/<int:pk>', views.SubCountyDetail.as_view(), name='subcounty'),
    path('wards', views.WardView.as_view(), name='wards'),
    path('wards/create', views.CreateWardView.as_view(), name='wards'),
    path('wards/<int:pk>', views.WardDetail.as_view(), name='wards'),
    path('locations', views.LocationView.as_view(), name='locations'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name='locations'),
    path('locations/create', views.CreateLocationView.as_view(), name='locations'),
    path('sub-locations', views.SubLocationView.as_view(), name='sub-locations'),
    path('sub-locations/create', views.CreateSubLocationView.as_view(), name='sub-locations'),
    path('sub-locations/<int:pk>', views.SubLocationDetail.as_view(), name='sub-locations'),
    path('villages', views.VillageView.as_view(), name='villages'),
    path('villages/create', views.CreateVillageView.as_view(), name='villages'),
    path('allocate', views.AllocationView.as_view(), name='allocation'),
    path('allocate/<int:pk>', views.AllocationDetail.as_view(), name='allocation'),
    path('villages/<int:pk>', views.VillageDetail.as_view(), name='villages')
]
