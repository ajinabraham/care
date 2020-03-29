# Generated by Django 2.2.11 on 2020-03-29 10:51

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0046_merge_20200329_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientregistration',
            name='real_name',
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='name',
            field=fernet_fields.fields.EncryptedCharField(max_length=200),
        ),
    ]