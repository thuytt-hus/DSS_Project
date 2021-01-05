# from django.conf.urls import url
from django.urls import path
from . import views
# from .views import (
#     StudentView,
# )

urlpatterns = [
    # url(r'^list-posts/$', StudentView.as_view(), name='list-posts'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('emp/', views.emp),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy, name='destroy'),
]
