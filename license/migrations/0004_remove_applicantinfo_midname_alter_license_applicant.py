# Generated by Django 4.0.5 on 2022-08-12 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('license', '0003_alter_applicantinfo_blood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicantinfo',
            name='midname',
        ),
        migrations.AlterField(
            model_name='license',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
