from django.conf.urls import patterns, include, url
from prof_rater import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<prof_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^(?P<prof_id>[0-9]+)/review/$', views.review, name='review'),
    url(r'^(?P<prof_id>[0-9]+)/rate/$', views.create_review, name='rate'),

    url(r'^(?P<dept_code>[A-z]{3,4})/$', views.department, name='department'),
    #url(r'^department/(?P<dept_code>[A-z]{3,4})/$', views.department, name='department'),

    url(r'^(?P<dept_code>[A-z]{3,4})/(?P<course_num>[0-9]{3})/$', views.course, name='course'),
    
    url(r'^(?P<dept_code>[A-z]{3,4})/(?P<course_num>[0-9]{3})/(?P<prof_id>[0-9]+)/$', views.profile_from_course, name='profile_from_course'),
        
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
