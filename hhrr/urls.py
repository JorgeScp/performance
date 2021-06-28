from django.urls import path, include
from . import views

urlpatterns = [
    path('ctr_form/', views.contracts_form,name='contracts_insert'), # get and post req. for insert operation
    path('ctr_list/',views.contracts_list,name='contracts_list'), # get req. to retrieve and display all records
    path('ctr/delete/<int:id>/',views.contracts_delete,name='contracts_delete'),
    path('ctr/update/<int:id>/', views.contracts_form,name='contracts_update'), # get and post req. for update operation
]