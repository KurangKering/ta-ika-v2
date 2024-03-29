# Generated by Django 3.1.4 on 2020-12-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.FloatField(blank=True, null=True)),
                ('steroid', models.FloatField(blank=True, null=True)),
                ('antivirals', models.FloatField(blank=True, null=True)),
                ('fatigue', models.FloatField(blank=True, null=True)),
                ('malaise', models.FloatField(blank=True, null=True)),
                ('anorexia', models.FloatField(blank=True, null=True)),
                ('liver_big', models.FloatField(blank=True, null=True)),
                ('liver_firm', models.FloatField(blank=True, null=True)),
                ('spleen_palpable', models.FloatField(blank=True, null=True)),
                ('spiders', models.FloatField(blank=True, null=True)),
                ('ascites', models.FloatField(blank=True, null=True)),
                ('varices', models.FloatField(blank=True, null=True)),
                ('bilirubin', models.FloatField(blank=True, null=True)),
                ('alk_posphate', models.FloatField(blank=True, null=True)),
                ('sgot', models.FloatField(blank=True, null=True)),
                ('albumin', models.FloatField(blank=True, null=True)),
                ('protime', models.FloatField(blank=True, null=True)),
                ('histology', models.FloatField(blank=True, null=True)),
                ('kelas', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
