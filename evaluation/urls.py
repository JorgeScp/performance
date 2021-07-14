from django.urls import path, include
from . import views

urlpatterns = [
    path('list_test/',views.test_assign_list,name='test_list'), # get req. to retrieve and display all records
    #path('test_update/<int:id>/', views.test_form,name='test_update'), # get and post req. for update operation
]