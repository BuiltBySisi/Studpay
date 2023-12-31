# Generated by Django 4.2.7 on 2023-11-07 16:02

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
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=10, null=True)),
                ('date', models.DateField()),
                ('cl', models.CharField(max_length=10)),
                ('present_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('by', models.CharField(default='School Management', max_length=20, null=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joindate', models.DateField(auto_now_add=True)),
                ('phone', models.CharField(max_length=40)),
                ('salary', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('fee', models.PositiveIntegerField(null=True)),
                ('cl', models.CharField(choices=[('Grade one', 'one'), ('Grade two', 'two'), ('Grade three', 'three'), ('Grade four', 'four'), ('Grade five', 'five'), ('Grade six', 'six'), ('Grade seven', 'seven'), ('Grade eight', 'eight'), ('Grade nine', 'nine'), ('Grade ten', 'ten')], default='Grade one', max_length=11)),
                ('status', models.BooleanField(default=False)),
                ('roll', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20, null=True)),
                ('grade', models.CharField(choices=[('A', 'Excellent'), ('B', 'Very Good'), ('C', 'Credit'), ('D', 'Pass'), ('F', 'Fail')], default='null', max_length=10)),
                ('teacherComment', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
