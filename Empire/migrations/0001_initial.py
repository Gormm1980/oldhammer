# Generated by Django 4.0.6 on 2022-08-16 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturesModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement', models.IntegerField()),
                ('HA', models.IntegerField()),
                ('HP', models.IntegerField()),
                ('Strength', models.IntegerField()),
                ('Resistance', models.IntegerField()),
                ('Health', models.IntegerField()),
                ('Attacks', models.IntegerField()),
                ('leadership', models.IntegerField()),
                ('Equipment_Options', models.CharField(max_length=50)),
                ('Points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmpireSpecialTroops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('Special_rules', models.TextField(max_length=250)),
                ('url_images', models.URLField()),
                ('FeaturesModels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empire.featuresmodels')),
            ],
        ),
        migrations.CreateModel(
            name='EmpireSingularTroops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('Special_rules', models.TextField(max_length=250)),
                ('url_images', models.URLField()),
                ('FeaturesModels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empire.featuresmodels')),
            ],
        ),
        migrations.CreateModel(
            name='EmpireHeroes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('Special_rules', models.TextField(max_length=250)),
                ('url_images', models.URLField()),
                ('Magic_Objects', models.TextField()),
                ('MountAndMonsters', models.TextField()),
                ('FeaturesModels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empire.featuresmodels')),
            ],
        ),
        migrations.CreateModel(
            name='EmpireCommanders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('Special_rules', models.TextField(max_length=250)),
                ('url_images', models.URLField()),
                ('Magic_Objects', models.TextField()),
                ('MountAndMonsters', models.TextField()),
                ('FeaturesModels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empire.featuresmodels')),
            ],
        ),
        migrations.CreateModel(
            name='EmpireBasicTroops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('Special_rules', models.TextField(max_length=250)),
                ('url_images', models.URLField()),
                ('FeaturesModels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empire.featuresmodels')),
            ],
        ),
    ]
