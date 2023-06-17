from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LoginView

router = routers.SimpleRouter()
router.register(r'tasks', TaskView)
router.register(r'types', TypeView)
router.register(r'users', UsersView)
router.register(r'statuses', StatusView)
router.register(r'task-comments', TaskCommentView)
router.register(r'task-comments-files', TaskCommentFileView)
router.register(r'task-files', TaskFileView)
router.register(r'importance-parameters', ImportanceParametersView)
router.register(r'task-parameters', TaskParametersView)
router.register(r'faq', FAQView)
router.register(r'faq-files', FAQFilesView)

urlpatterns = [
    path('sign-in/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
    path('login/', LoginView.as_view(),name='login'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)