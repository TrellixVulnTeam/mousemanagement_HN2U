# Generated by Django 3.0.2 on 2020-05-01 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HarvestedBasedNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liver', models.IntegerField()),
                ('liverTumor', models.IntegerField()),
                ('others', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HarvestedMouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handler', models.TextField()),
                ('physicalId', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('mouseLine', models.TextField()),
                ('genoType', models.TextField()),
                ('birthDate', models.DateField()),
                ('endDate', models.DateField()),
                ('confirmationOfGenoType', models.BooleanField(default=False)),
                ('phenoType', models.TextField()),
                ('projectTitle', models.TextField()),
                ('experiment', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HarvestedAdvancedNumber',
            fields=[
                ('harvestedbasednumber_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='harvestmouseapp.HarvestedBasedNumber')),
                ('smallIntestine', models.IntegerField()),
                ('smallIntestineTumor', models.IntegerField()),
                ('skin', models.IntegerField()),
                ('skinHair', models.IntegerField()),
            ],
            bases=('harvestmouseapp.harvestedbasednumber',),
        ),
        migrations.AddField(
            model_name='harvestedbasednumber',
            name='harvestedMouseId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvestmouseapp.HarvestedMouse'),
        ),
    ]