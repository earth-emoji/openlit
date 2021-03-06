# Generated by Django 2.1.2 on 2019-03-28 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0001_initial'),
        ('characters', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialogues', to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time', models.CharField(blank=True, max_length=255, null=True)),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('weather', models.CharField(blank=True, max_length=255, null=True)),
                ('setup', models.TextField(blank=True, null=True)),
                ('action', models.TextField(blank=True, null=True)),
                ('position', models.PositiveIntegerField()),
                ('act', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenes', to='stories.Act')),
                ('characters', models.ManyToManyField(blank=True, related_name='scenes', to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('premise', models.CharField(blank=True, max_length=300, null=True)),
                ('time', models.CharField(blank=True, max_length=255, null=True)),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('album', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='StoryCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Protagonist', 'Protagonist'), ('Deuteragonist', 'Deuteragonist'), ('Antagonist', 'Antagonist'), ('Love Interest', 'Love Interest'), ('Mentor', 'Mentor'), ('Narrator', 'Narrator'), ('Secondary', 'Secondary Character'), ('Tertiary', 'Tertiary Character'), ('Flat', 'Flat Character')], max_length=100)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='characters.Character')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story')),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='characters',
            field=models.ManyToManyField(blank=True, through='stories.StoryCharacter', to='characters.Character'),
        ),
        migrations.AddField(
            model_name='dialogue',
            name='scene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialogues', to='stories.Scene'),
        ),
        migrations.AddField(
            model_name='act',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acts', to='stories.Story'),
        ),
    ]
