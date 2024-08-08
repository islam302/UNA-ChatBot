from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from Homepage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='index'),
    path('upload', views.upload_file_view, name='upload_file'),
    path('question', views.get_question_from_user, name='get_question'),
    path('get_answer/<uuid:question_id>/', views.get_answer, name='get_answer'),
    path('add', views.add_question, name='add_question'),
    path('edit/<uuid:id>', views.edit_question, name='edit_question'),
    path('delete/<uuid:id>', views.delete_question, name='delete_question'),
    path('store_unanswered/', views.store_unanswered_question, name='store_unanswered_question'),
    path('unanswered/', views.unanswered_questions, name='unanswered_questions'),
    path('add_answer/<uuid:question_id>/', views.add_answer_to_question, name='add_answer_to_question'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Homepage.views.custom_404'
handler500 = 'Homepage.views.custom_500'
