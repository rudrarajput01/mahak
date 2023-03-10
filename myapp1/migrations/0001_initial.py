# Generated by Django 4.0.1 on 2023-01-06 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChallanModels',
            fields=[
                ('Challan_no', models.AutoField(primary_key=True, serialize=False)),
                ('Company_Name', models.CharField(max_length=200)),
                ('Contact_Person', models.CharField(max_length=200)),
                ('Mobile_no', models.CharField(max_length=10)),
                ('StartDate', models.DateField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('Assigned', 'Assigned'), ('Pending', 'Pending'), ('Waiting', 'Waiting'), ('Ready', 'Ready'), ('Delivered', 'Delivered')], default='pending', max_length=10)),
                ('Remark', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Company_Name', models.CharField(max_length=200)),
                ('Contact_Person', models.CharField(max_length=200)),
                ('Mobile_no', models.CharField(max_length=20, primary_key='true', serialize=False)),
                ('Email_id', models.CharField(max_length=20)),
                ('Area', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('Pincode', models.CharField(max_length=20)),
                ('Gstin', models.CharField(max_length=20)),
                ('Reference', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JobsheetModels',
            fields=[
                ('Jobsheet_no', models.AutoField(primary_key=True, serialize=False)),
                ('Job_Name', models.CharField(max_length=200)),
                ('Contact_Person', models.CharField(max_length=200)),
                ('Mobile_no', models.CharField(max_length=10)),
                ('StartDate', models.DateField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('Assigned', 'Assigned'), ('Pending', 'Pending'), ('Waiting', 'Waiting'), ('Ready', 'Ready'), ('Delivered', 'Delivered')], default='pending', max_length=10)),
                ('Remark', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TeamsModels',
            fields=[
                ('Member_name', models.CharField(max_length=20)),
                ('Designation', models.CharField(max_length=20)),
                ('Department', models.CharField(max_length=20)),
                ('Mobile_no', models.CharField(max_length=20)),
                ('Email_id', models.CharField(max_length=20)),
                ('Area', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('Pincode', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('passcode', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PriceModels',
            fields=[
                ('Challan_no_part', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp1.challanmodels')),
                ('Total_Price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('Advance_Price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('Net_Price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('Paid_by', models.CharField(choices=[('Paytm', 'Paytm'), ('Cash', 'Cash'), ('Phonepe', 'Phonepe'), ('Other', 'Other')], default='Cash', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=20)),
                ('size_name', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField()),
                ('print_type', models.CharField(max_length=20)),
                ('print_color', models.CharField(max_length=20)),
                ('paper_name', models.CharField(max_length=20)),
                ('binding', models.CharField(max_length=20)),
                ('lamination', models.CharField(max_length=20)),
                ('folding', models.CharField(max_length=20)),
                ('perforated', models.CharField(max_length=20)),
                ('rate', models.CharField(max_length=20)),
                ('amount', models.CharField(max_length=20)),
                ('job_status', models.CharField(default='pending', max_length=20)),
                ('Customer_mob_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ParticularsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Particular_Name', models.CharField(max_length=200)),
                ('Size', models.CharField(max_length=20)),
                ('Rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('Quantity', models.IntegerField(blank=True, default=22)),
                ('Amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('Challan_no_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.challanmodels')),
            ],
        ),
        migrations.CreateModel(
            name='DesignerAllotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designer_name', models.CharField(max_length=20)),
                ('Customer_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.customer')),
                ('Job_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.product')),
            ],
        ),
    ]
