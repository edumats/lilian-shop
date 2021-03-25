# Generated by Django 3.1.7 on 2021-03-24 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('available', models.BooleanField(default=False, help_text='Product can be sold')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('featured_product', models.BooleanField(default=False, help_text='Product will appear in featured section')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Hantem',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.product')),
                ('size', models.CharField(choices=[('PP', 'Extra Pequeno'), ('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'), ('GG', 'Extra Grande')], max_length=2)),
            ],
            bases=('store.product',),
        ),
    ]