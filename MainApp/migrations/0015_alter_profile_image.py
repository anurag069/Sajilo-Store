# Generated by Django 5.2.1 on 2025-06-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0014_alter_profile_gender_alter_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/default.png', upload_to='profiles/'),
        ),
    ]
