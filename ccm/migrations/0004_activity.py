# Generated by Django 5.0.6 on 2024-06-28 19:21

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccm', '0003_rename_target_indicator_target'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('activity', models.CharField()),
                ('activity_code', models.CharField(max_length=5, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ccm.indicator')),
            ],
            options={
                'db_table': 'activity',
            },
        ),
    ]
