# Generated by Django 3.2.5 on 2021-07-30 06:26

import api.models.users
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
            name='ValsRoomUserInvitation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no', models.IntegerField(default=api.models.users.generate_invitation_no, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ValsRoomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('django_user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
