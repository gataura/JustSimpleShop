from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'JustSimpleShop'

urlpatterns = [
                  url(r'^$', views.product_list, name='product_list'),
                  url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
                  url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
