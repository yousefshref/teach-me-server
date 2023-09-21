from django.contrib import admin
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('sign_up/', views.sign_up),
    path('log_in/', views.log_in),

    path('get_levels/', views.get_levels),
    path('get_student/', views.get_student),


    path('get_homework/', views.get_homework),
    path('get_homework_answer/', views.get_homework_answer),
    path('send_answer/', views.send_answer),
    path('get_student_answers/', views.get_student_answers),


    path('get_lessons/', views.get_lessons),
    path('get_media/', views.get_media),


    path('students/<int:pk>/update-image/', views.StudentImageUpdateView.as_view(), name='student-image-update'),


    path('get_total_infos/', views.get_total_infos),


    path('get_lessons_names/', views.get_lessons_names),

]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)