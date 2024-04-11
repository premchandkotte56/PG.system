from django.urls import path
from . import views

urlpatterns=[
    path('first',views.firstpage,name='firstpageurl'),
    path('stdlogin',views.studentlogin,name='studentloginurl'),
    path('stdsignup',views.studentsignup,name='studentsignupurl'),
    path('pglogin',views.pglogin,name='pgloginurl'),
    path('pgsignup',views.pgsignup,name='pgsignupurl'),
    path('pgform',views.pgform,name='pgformurl'),
    path('pgdetails',views.pgdetails,name='pgdetailsurl'),
    path('pgmain',views.pgmain,name='pgmainurl'),
    path('pgshare',views.pgshare,name='pgshareurl'),
    path('logout',views.user_logout,name='logouturl'),
    path('pglogout',views.admin_logout,name='pglogouturl'),
    path('complete/<int:eno>',views.complete,name='completeurl'),
    path('registerpg/<int:eno>',views.registerpg,name='registerpgurl'),
    path('stdlist/',views.stdlist,name='stdlisturl'),
    path('delete/<int:eno>',views.deleteData , name='deleteurl')
]