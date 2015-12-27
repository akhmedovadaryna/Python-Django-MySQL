from django.conf.urls import include, url

urlpatterns = [
    url(r'^file/', 'student.views.filelist'),
    url(r'^addfile/', 'student.views.addfile'),
    url(r'^change/', 'student.views.change_u'),
    url(r'^change_file/', 'student.views.change_f'),
    url(r'^delete/', 'student.views.delet_f'),
    url(r'^addc/', 'student.views.addCloud_storage'),
    url(r'^user_add/', 'student.views.adduser'),
]
