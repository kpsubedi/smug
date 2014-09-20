from django.conf.urls import patterns, url
from forensic import views

urlpatterns = patterns('',
    # ex: /forensic/
    url(r'^$', views.index, name='index'),
    # ex: /forensic/5/
    url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
    # ex: /forensic/5/results/
    url(r'^(?P<user_id>\d+)/results/$', views.results, name='results'),
    # ex: /forensic/5/play/
    url(r'^(?P<user_id>\d+)/play/$', views.play, name='play'),   
)

