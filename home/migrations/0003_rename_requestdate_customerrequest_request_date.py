# Generated by Django 4.2.5 on 2023-09-22 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_customerrequest_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerrequest',
            old_name='requestDate',
            new_name='request_date',
        ),
    ]