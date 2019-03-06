# Generated by Django 2.1.7 on 2019-03-02 10:07

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('pem_data', models.TextField()),
                ('issuer', models.CharField(blank=True, max_length=2048)),
                ('subject', models.CharField(blank=True, max_length=2048)),
                ('cn', models.CharField(blank=True, max_length=2048)),
                ('sha256_fingerprint', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]