from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import CreateProduct, Fetchsales,Product,MakeSale,FetchSale

app_name = 'Record'


router = routers.DefaultRouter()
router.register('product', Product, 'product'),
router.register('sale', MakeSale, 'sale'),
router.register('allsales', Fetchsales, 'allsales'),
router.register('create', CreateProduct, 'create'),

urlpatterns = [
path('sales',FetchSale.as_view(),name="sales"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += router.urls
# urlpatterns 

