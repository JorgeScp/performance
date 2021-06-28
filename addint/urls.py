from django.urls import path, include
from . import views

urlpatterns = [
    path('addint_form/', views.addint_form,name='addint_insert'), # get and post req. for insert operation
    path('addint_update/<int:id>/', views.addint_form,name='addint_update'), # get and post req. for update operation
    path('addint_delete/<int:id>/',views.addint_delete,name='addint_delete'),
    path('item_update/<int:id>/',views.item_update,name='item_update'),
    path('item_update_concept/<int:id>/',views.item_update_concept,name='item_update_concept'),
    path('',views.addint_list,name='addint_list'), # get req. to retrieve and display all records
]