# Generated by Django 3.2.19 on 2023-06-05 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20230605_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='resolved_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.task'),
        ),
    ]
