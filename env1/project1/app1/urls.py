from django.urls import path
from . import views

urlpatterns = [
    path('',views.default),
    path('guide',views.guide),
    path('home',views.default),
    path('findit',views.default),
    path('subjects',views.subjects),
    path('guide', views.guide),
    # path('view3', views.view3),
    # path('view2', views.view2),
    path('findit/<int:id_no>',views.findit),
    path('exam',views.exam),
    path('cal',views.cal),
]