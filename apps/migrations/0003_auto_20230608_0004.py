# Generated by Django 3.2.19 on 2023-06-08 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_faq_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcommentfile',
            name='file',
            field=models.FileField(upload_to='media/task-comment/files/'),
        ),
        migrations.AlterField(
            model_name='taskfile',
            name='file',
            field=models.FileField(upload_to='media/task/files/'),
        ),
        migrations.AlterField(
            model_name='usersimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/users/images/'),
        ),
        migrations.CreateModel(
            name='FAQFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/faq/files/')),
                ('faq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.faq')),
            ],
            options={
                'verbose_name': 'ЧаВо файл',
                'verbose_name_plural': 'ЧаВо файлы',
            },
        ),
    ]