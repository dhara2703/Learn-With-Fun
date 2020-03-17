# Generated by Django 3.0.3 on 2020-02-10 08:47

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
            name='City',
            fields=[
                ('c_city_id', models.AutoField(primary_key=True, serialize=False, verbose_name='city id')),
                ('c_city_name', models.CharField(max_length=190, verbose_name='city name')),
                ('c_city_isactive', models.BooleanField(default=True, verbose_name='is city active')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'tblkpCity',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('c_country_id', models.AutoField(primary_key=True, serialize=False, verbose_name='country id')),
                ('c_country_name', models.CharField(max_length=90, unique=True, verbose_name='country name')),
                ('c_country_isactive', models.BooleanField(default=True, verbose_name='is country active')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'tblkpCountry',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('p_province_id', models.AutoField(primary_key=True, serialize=False, verbose_name='province id')),
                ('p_province_name', models.CharField(max_length=90, verbose_name='province name')),
                ('p_province_isactive', models.BooleanField(default=True, verbose_name='is province active')),
                ('p_province_country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Country', verbose_name='country name')),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
                'db_table': 'tblkpProvince',
                'unique_together': {('p_province_name', 'p_province_country_id')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_student_id', models.AutoField(primary_key=True, serialize=False, verbose_name='student id')),
                ('s_student_isactive', models.BooleanField(default=True, verbose_name='is student active')),
                ('s_student_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.City', verbose_name='student city')),
                ('s_student_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Country', verbose_name='student country')),
                ('s_student_province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Province', verbose_name='student province')),
                ('s_student_user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='student user id')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'db_table': 'tblStudent',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='c_city_province_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Province', verbose_name='province id'),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('c_city_name', 'c_city_province_id')},
        ),
    ]
