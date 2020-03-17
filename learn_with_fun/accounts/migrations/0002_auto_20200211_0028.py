# Generated by Django 3.0.3 on 2020-02-11 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='c_city_province_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Province', verbose_name='province id'),
        ),
        migrations.AlterField(
            model_name='province',
            name='p_province_country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Country', verbose_name='country name'),
        ),
        migrations.AlterField(
            model_name='province',
            name='p_province_name',
            field=models.CharField(max_length=90, verbose_name='province/State name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_student_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.City', verbose_name='student city'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_student_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Country', verbose_name='student country'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_student_province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Province', verbose_name='student province'),
        ),
    ]
