from django.contrib import admin
from .models import Type, Task, Status, ImportanceParameters,\
    FAQ, TaskFile, TaskCommentFile, TaskComment, TaskParameters, UsersImage,FAQFiles

admin.site.register(Type)
admin.site.register(Task)
admin.site.register(UsersImage)
admin.site.register(Status)
admin.site.register(ImportanceParameters)
admin.site.register(FAQ)
admin.site.register(TaskFile)
admin.site.register(TaskCommentFile)
admin.site.register(TaskComment)
admin.site.register(TaskParameters)
admin.site.register(FAQFiles)

# Register your models here.
