from django.db import models
from django.conf import settings


class UsersImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    image = models.ImageField(upload_to='media/users/images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Фото пользователя'
        verbose_name_plural = 'Фото пользователей'

    def __str__(self):
        return f'{self.user.username} - {self.image}'


class Status(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return f'{self.id} - {self.name}'


class ImportanceParameters(models.Model):
    name = models.CharField(max_length=50)
    priority_coefficient = models.FloatField()

    class Meta:
        verbose_name = 'Параметр важности'
        verbose_name_plural = 'Параметры важности'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    date_created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    date_updated = models.DateTimeField(auto_now=False, verbose_name='Дата обновления', null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    resolved_previously = models.BooleanField(default=False)
    resolved_task = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    priority = models.FloatField(default=0.0)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id} - {self.name}'


class TaskParameters(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    importance_parameter = models.ForeignKey(ImportanceParameters, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Параметр задач'
        verbose_name_plural = 'Параметры задач'

    def __str__(self):
        return f'{self.task.name} - {self.importance_parameter.name}'


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    comment = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Коментарий задач'
        verbose_name_plural = 'Коментарии задач'

    def __str__(self):
        return f'{self.id} - {self.comment}'


class TaskCommentFile(models.Model):
    comment = models.ForeignKey(TaskComment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/task-comment/files/')

    class Meta:
        verbose_name = 'Файл комментариев'
        verbose_name_plural = 'Файлы комментариев'

    def __str__(self):
        return f'{self.comment.comment} - {self.file}'


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/task/files/')

    class Meta:
        verbose_name = 'Файл задач'
        verbose_name_plural = 'Файлы задач'

    def __str__(self):
        return f'{self.task.name} - {self.file}'


class FAQ(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    html = models.TextField(null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    resolved_task = models.ManyToManyField(Task, null=True, blank=True,)

    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'

    def __str__(self):
        return f'{self.id} - {self.name}'
    

class FAQFiles(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True, default='')
    file = models.FileField(upload_to='media/faq/files/')

    class Meta:
        verbose_name = 'ЧаВо файл'
        verbose_name_plural = 'ЧаВо файлы'

    def __str__(self):
        return f'{self.faq} - {self.name}'
# Create your models here.
