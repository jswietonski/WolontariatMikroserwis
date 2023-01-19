# Generated by Django 3.2.8 on 2023-01-14 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inicjatywa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.TextField(null=True)),
                ('data_rozpoczecia', models.CharField(max_length=20)),
                ('liczba_miejsc', models.IntegerField(null=True)),
                ('lokalizacja', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OperatorProjektu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('adres', models.CharField(max_length=200)),
                ('numer_kontaktowy', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Uczestnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uzytkownik', models.CharField(max_length=50, null=True)),
                ('zaakceptowany', models.BooleanField(default=False)),
                ('opis_siebie', models.TextField(null=True)),
                ('cv', models.BinaryField(null=True)),
                ('inicjatywa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wolontariat_obsluga.inicjatywa')),
            ],
        ),
        migrations.AddField(
            model_name='inicjatywa',
            name='kategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wolontariat_obsluga.kategoria'),
        ),
        migrations.AddField(
            model_name='inicjatywa',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wolontariat_obsluga.operatorprojektu'),
        ),
    ]