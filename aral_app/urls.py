from django.urls import path
from .views import home, blog_detail, project_details, custom_404

urlpatterns = [
    path('', home, name='home'),
    path('blog-details/<int:id>/', blog_detail, name='blog_detail'),
    path('portfolio-details/<int:id>/', project_details, name='project_details'),
    path('404/', custom_404, name='404'),
]