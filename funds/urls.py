from django.urls import path

from . import views

app_name = 'funds'

urlpatterns = [
    # ex: /funds/
    path('', views.index, name='index'),
    # ex: /funds/5/
    path('participant/<int:participant_id>/', views.participant, name='participant'),
    # report view
    path('report/', views.report, name='report'),

]

