from django.urls import path,re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    # path('', views.news_today, name = 'projects'),
    # path('search/', views.search_results, name='search_results'),
    # path('ajax/newsletter/', views.newsletter, name='newsletter'),
    # path('api/merch/', views.MerchList.as_view()),
    # re_path('api/merch/merch-id/(?P<pk>[0-9]+)/$',
    #     views.MerchDescription.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)