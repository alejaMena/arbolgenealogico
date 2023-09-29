# Generated by Django 4.2.5 on 2023-09-28 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hijo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='padres', to='genealogia.persona')),
                ('padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hijos', to='genealogia.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Matrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrimonios', to='genealogia.persona')),
                ('persona2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genealogia.persona')),
            ],
        ),
    ]