# Generated by Django 3.2 on 2021-10-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('article_name', models.CharField(blank=True, max_length=220)),
                ('article_id', models.CharField(blank=True, max_length=40)),
                ('article_sku', models.CharField(blank=True, max_length=100)),
                ('current_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('price_difference', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('main_picture', models.URLField(blank=True)),
                ('product_description', models.CharField(blank=True, max_length=500)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('price_difference', '-created'),
            },
        ),
    ]