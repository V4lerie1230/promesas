# Generated by Django 4.0.6 on 2022-07-14 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto', models.IntegerField()),
                ('pagado', models.BooleanField(default=False)),
                ('acudiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.acudiente')),
            ],
        ),
    ]
