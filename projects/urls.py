from django.urls import path,re_path,include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name = 'index'),
    re_path('project/(\d+)', views.get_project_by_id, name='project_results'),
    path('new/project', views.new_project, name='new-project'),
    path('api/projects/', views.ProjectsList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
    # path('search/', views.search_results, name='search_results'),
    # path('ajax/newsletter/', views.newsletter, name='newsletter'),
    # re_path('api/merch/merch-id/(?P<pk>[0-9]+)/$',
    #     views.MerchDescription.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)