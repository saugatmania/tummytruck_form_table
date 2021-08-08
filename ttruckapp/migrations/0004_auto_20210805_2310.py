# Generated by Django 3.2.5 on 2021-08-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttruckapp', '0003_auto_20210805_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.CharField(choices=[('dairy', 'DAIRY'), ('beverages', 'BEVERAGES'), ('hard drinks', 'HARD DRINKS'), ('soft drinks', 'SOFT DRINKS'), ('groceries', 'GROCERIES'), ('kitchen item', 'KITCHEN ITEM'), ('madi in nepal', 'MADE IN NEPAL'), ('restaurants', 'RESTAURANTS')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='package_products',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='packages',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(),
        ),
    ]
