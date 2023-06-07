# Generated by Django 4.0.6 on 2022-11-26 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='ctg1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='telegram_bot.category1'),
        ),
    ]