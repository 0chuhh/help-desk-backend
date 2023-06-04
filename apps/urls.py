from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views import *
router = routers.SimpleRouter()
router.register(r'tasks', TaskView)
router.register(r'types', TypeView)
router.register(r'statuses', StatusView)
router.register(r'task-comments', TaskCommentView)
router.register(r'task-comments-files', TaskCommentFileView)
router.register(r'task-files', TaskFileView)
router.register(r'importance-parameters', ImportanceParametersView)
router.register(r'task-parameters', TaskParametersView)
router.register(r'faq', FAQView)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)