# Generated by Django 3.2.19 on 2023-06-13 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_faqfiles_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqfiles',
            name='faq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.faq'),
        ),
        migrations.AlterField(
            model_name='faqfiles',
            name='file',
            field=models.FileField(null=True, upload_to='media/faq/files/'),
        ),
    ]
