from django.urls import path, include
from . import views

urlpatterns = [
    path('list_test/',views.test_assign_list,name='test_list'), # get req. to retrieve and display all records
    path('relation_form/', views.rel_form,name='relation_add'), # get and post req. for update operation
]