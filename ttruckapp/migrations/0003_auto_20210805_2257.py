# Generated by Django 3.2.5 on 2021-08-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttruckapp', '0002_auto_20210805_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=100)),
                ('package', models.CharField(choices=[('employee_package', 'EMPLOYEE PACKAGE'), ('total_veg_package', 'TOTAL VEG PACKAGE')], max_length=50)),
                ('week', models.CharField(choices=[('first_week', 'FIRST WEEK'), ('second_week', 'SECOND WEEK'), ('third_week', 'THIRD WEEK'), ('fourth_week', 'FOURTH WEEK')], max_length=50)),
                ('day', models.CharField(choices=[('sunday', 'SUNDAY'), ('monday', 'MONDAY'), ('tuesday', 'TUESDAY'), ('wednesday', 'WEDNESDAY'), ('thursday', 'THURSDAY'), ('friday', 'FRIDAY'), ('saturday', 'SATURDAY')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='packages',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
