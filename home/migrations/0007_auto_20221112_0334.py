# Generated by Django 3.1.4 on 2022-11-12 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('someabstractmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.someabstractmodel')),
                ('Title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            bases=('home.someabstractmodel',),
        ),
        migrations.AddField(
            model_name='sermons',
            name='image',
            field=models.ImageField(default='11.jpg', upload_to='sermon_images'),
        ),
    ]
