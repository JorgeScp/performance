from django.urls import path, include
from . import views

urlpatterns = [
    path('appl_form/', views.appl_form,name='appl_insert'), # get and post req. for insert operation
    path('appl_list/',views.appl_list,name='appl_list'), # get req. to retrieve and display all records
    path('test_form/', views.test_form,name='test_insert'), # get and post req. for insert operation
    path('test_list/',views.test_list,name='test_list'), # get req. to retrieve and display all records
    path('test_update/<int:id>/', views.test_form,name='test_update'), # get and post req. for update operation
]