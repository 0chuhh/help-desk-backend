# Generated by Django 3.2.19 on 2023-06-06 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportanceParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('priority_coefficient', models.FloatField()),
            ],
            options={
                'verbose_name': 'Параметр важности',
                'verbose_name_plural': 'Параметры важности',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(blank=True, null=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('resolved_previously', models.BooleanField(default=False)),
                ('priority', models.FloatField(default=0.0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('resolved_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.task')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.status')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.task')),
            ],
            options={
                'verbose_name': 'Коментарий задач',
                'verbose_name_plural': 'Коментарии задач',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='UsersImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Фото пользователя',
                'verbose_name_plural': 'Фото пользователей',
            },
        ),
        migrations.CreateModel(
            name='TaskParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance_parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.importanceparameters')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.task')),
            ],
            options={
                'verbose_name': 'Параметр задач',
                'verbose_name_plural': 'Параметры задач',
            },
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.task')),
            ],
            options={
                'verbose_name': 'Файл задач',
                'verbose_name_plural': 'Файлы задач',
            },
        ),
        migrations.CreateModel(
            name='TaskCommentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.taskcomment')),
            ],
            options={
                'verbose_name': 'Файл комментариев',
                'verbose_name_plural': 'Файлы комментариев',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.type'),
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('resolved_task', models.ManyToManyField(blank=True, null=True, to='apps.Task')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.type')),
            ],
            options={
                'verbose_name': 'Часто задаваемый вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
    ]
