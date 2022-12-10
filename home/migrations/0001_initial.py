# Generated by Django 3.1.4 on 2022-11-11 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeAbstractModel',
            fields=[
                ('id', models.UUIDField(default=home.models.get_token, editable=False, primary_key=True, serialize=False, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('someabstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.someabstractmodel')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('verse', models.CharField(max_length=255)),
            ],
            bases=('home.someabstractmodel',),
        ),
        migrations.CreateModel(
            name='SermonAttendance',
            fields=[
                ('someabstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.someabstractmodel')),
                ('male', models.IntegerField()),
                ('female', models.IntegerField()),
                ('children', models.IntegerField()),
            ],
            bases=('home.someabstractmodel',),
        ),
        migrations.CreateModel(
            name='Sermons',
            fields=[
                ('someabstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.someabstractmodel')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('video', models.CharField(max_length=255)),
            ],
            bases=('home.someabstractmodel',),
        ),
        migrations.CreateModel(
            name='Testimonies',
            fields=[
                ('someabstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.someabstractmodel')),
                ('name', models.CharField(max_length=255)),
                ('testimony', models.CharField(max_length=255)),
            ],
            bases=('home.someabstractmodel',),
        ),
        migrations.CreateModel(
            name='NewsFeeds',
            fields=[
                ('someabstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.someabstractmodel')),
                ('picture', models.ImageField(upload_to='posts/img')),
                ('body', models.CharField(max_length=255)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='likers', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('home.someabstractmodel',),
        ),
    ]