from django.urls import path
from . import views
# from django.views.generic.base import RedirectView

# favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # path(r'^favicon\.ico$', favicon_view),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage'),
    path('qna/', views.qna, name='qna'),
    path('', views.index, name='index'),
    path('<str:a>/', views.check, name='a' ),
    ]
