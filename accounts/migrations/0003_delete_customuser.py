# Generated by Django 4.2.6 on 2023-11-02 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
