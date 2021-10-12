# Generated by Django 3.1.7 on 2021-10-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='name')),
                ('lastName', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='lastName')),
                ('patronymic', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='patronymic')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('dateOfBirth', models.CharField(blank=True, max_length=255, null=True, verbose_name='dateOfBirth')),
                ('passNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='passNumber')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('analysisDate', models.CharField(blank=True, max_length=255, null=True, verbose_name='analysisDate')),
                ('completeDate', models.CharField(blank=True, max_length=255, null=True, verbose_name='completeDate')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
