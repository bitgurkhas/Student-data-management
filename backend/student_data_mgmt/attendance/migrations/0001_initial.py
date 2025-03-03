# Generated by Django 5.1.6 on 2025-03-03 09:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], max_length=10)),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'student'}, on_delete=django.db.models.deletion.CASCADE, related_name='attendances_as_student', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(limit_choices_to={'groups__name': 'teacher'}, on_delete=django.db.models.deletion.CASCADE, related_name='attendances_as_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
