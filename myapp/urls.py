from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('usercreate/',views.crudops,name='crudops'),
    path('viewall/',views.viewall,name='viewall'),
    path('adduser/',views.adduser,name='adduser'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/',views.addupdateduser,name='addupdateduser')
 
]
