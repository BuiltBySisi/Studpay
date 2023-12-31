# Generated by Django 4.2.7 on 2023-11-15 08:52

from django.db import migrations, models
import uuid



class Migration(migrations.Migration):

    dependencies = [
        ('paytask', '0003_rename_user_performance_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='unique_code',
            field=models.CharField(default=uuid.uuid4, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='unique_code',
            field=models.CharField(default=uuid.uuid4, max_length=10, null=True),
        ),
    ]
