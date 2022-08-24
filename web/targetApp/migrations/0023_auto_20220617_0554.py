# Generated by Django 3.2.4 on 2022-06-17 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0022_auto_20220617_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_address',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_address', to='targetApp.domainaddress'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_city',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_city', to='targetApp.domaincity'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_country',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_country', to='targetApp.domaincountry'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_email',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_email', to='targetApp.domainemail'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_fax',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_fax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_fax', to='targetApp.domainfax'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_id',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_id', to='targetApp.domainregistrarid'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_name',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_name', to='targetApp.domainregistername'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_organization',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_organization', to='targetApp.domainregisterorganization'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_phone',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_phone', to='targetApp.domainphone'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_state',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_state', to='targetApp.domainstate'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='admin_zip_code',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='admin_zip_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_zip_code', to='targetApp.domainzipcode'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_address',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_address', to='targetApp.domainaddress'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_city',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_city', to='targetApp.domaincity'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_country',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_country', to='targetApp.domaincountry'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_email',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_email', to='targetApp.domainemail'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_fax',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_fax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_fax', to='targetApp.domainfax'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_name',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_name', to='targetApp.domainregistername'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_organization',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_organization', to='targetApp.domainregisterorganization'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_phone',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_phone', to='targetApp.domainphone'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_state',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_state', to='targetApp.domainstate'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrant_zip_code',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrant_zip_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrant_zip_code', to='targetApp.domainzipcode'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='registrar',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='registrar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='targetApp.domainregistrar'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_address',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_address', to='targetApp.domainaddress'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_city',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_city', to='targetApp.domaincity'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_country',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_country', to='targetApp.domaincountry'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_email',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_email', to='targetApp.domainemail'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_fax',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_fax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_fax', to='targetApp.domainfax'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_id',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_id', to='targetApp.domainregistrarid'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_name',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_name', to='targetApp.domainregistername'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_organization',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_organization', to='targetApp.domainregisterorganization'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_phone',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_phone', to='targetApp.domainphone'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_state',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_state', to='targetApp.domainstate'),
        ),
        migrations.RemoveField(
            model_name='domaininfo',
            name='tech_zip_code',
        ),
        migrations.AddField(
            model_name='domaininfo',
            name='tech_zip_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_zip_code', to='targetApp.domainzipcode'),
        ),
    ]
