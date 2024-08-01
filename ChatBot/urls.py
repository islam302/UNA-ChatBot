# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from Homepage import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('upload', views.upload_file_view, name='upload_file'),
    # path('test-question/', views.test_question_page, name='test_question'),
    path('question', views.get_question_from_user, name='get_question'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Homepage.views.custom_404'
handler500 = 'Homepage.views.custom_500'
