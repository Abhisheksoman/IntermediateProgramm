from django.urls import path
from base import views

urlpatterns = [
    path('',views.index,name="index"),
    path('/show',views.show,name="show"),
    path('/edit',views.show,name="show"),
    path('insertData',views.insertData,name="insertData"),
    path('update/<int:id>',views.updateData,name="update_data"),
    path('delete/<int:id>',views.deleteData,name="delete_data"),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]