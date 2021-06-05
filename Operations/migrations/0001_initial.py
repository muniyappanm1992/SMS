# Generated by Django 3.2 on 2021-06-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='godryModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('TimeStamp', models.CharField(max_length=100, null=True)),
                ('ModifiedBy', models.CharField(max_length=100, null=True)),
                ('SO NAME', models.CharField(max_length=100, null=True)),
                ('DO NAME', models.CharField(max_length=100)),
                ('SALES AREA', models.CharField(max_length=100, null=True)),
                ('RO CODE', models.CharField(max_length=100)),
                ('RO NAME', models.CharField(max_length=100)),
                ('SUPPLY LOCATION', models.CharField(max_length=100, null=True)),
                ('PRODUCT', models.CharField(max_length=100)),
                ('NO. OF TANKS', models.CharField(max_length=100, null=True)),
                ('TANKAGE', models.CharField(max_length=100, null=True)),
                ('STOCK DATE/ TIME', models.CharField(max_length=100, null=True)),
                ('STOCK AVAILABLE (L)', models.CharField(max_length=100, null=True)),
                ('DEAD STOCK (L)', models.CharField(max_length=100, null=True)),
                ('STOCK ON WHEEL AVAILABLE (L)', models.CharField(max_length=100, null=True)),
                ('PENDING INDENT QUANTITY (L)', models.CharField(max_length=100, null=True)),
                ('AVERAGE NOZZLE SALES (L)', models.CharField(max_length=100, null=True)),
                ('INDENT EXECUTION TIME (HRS.)', models.CharField(max_length=100, null=True)),
                ('TRANSIT TIME (HRS.)', models.CharField(max_length=100, null=True)),
                ('STOCK SURVIVAL HOURS (HRS.)', models.CharField(max_length=100, null=True)),
                ('EXPECTED DRYOUT DATE/ TIME', models.DateTimeField(max_length=100)),
                ('STATUS CRITICAL', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'godry',
            },
        ),
        migrations.CreateModel(
            name='outofstockModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('TimeStamp', models.CharField(max_length=100, null=True)),
                ('ModifiedBy', models.CharField(max_length=100, null=True)),
                ('SO NAME', models.CharField(max_length=100, null=True)),
                ('DO NAME', models.CharField(max_length=100)),
                ('SALES AREA', models.CharField(max_length=100, null=True)),
                ('DATE', models.CharField(max_length=100, null=True)),
                ('RO CODE', models.CharField(max_length=100)),
                ('RO NAME', models.CharField(max_length=100)),
                ('PRODUCT', models.CharField(max_length=100)),
                ('NO. OF TANK', models.CharField(max_length=100, null=True)),
                ('TOTAL HOURS STOCK OUT', models.CharField(max_length=100, null=True)),
                ('POTENTIAL LOSS (IN LITERS)', models.CharField(max_length=100, null=True)),
                ('STOCK OUT HOURS - CUR MONTH', models.CharField(max_length=100, null=True)),
                ('POTENTIAL LOSS - CUR MONTH (IN LITERS)', models.CharField(max_length=100, null=True)),
                ('STOCK OUT HOURS - PREVIOUS MONTH', models.CharField(max_length=100, null=True)),
                ('POTENTIAL LOSS - PREVIOUS MONTH (IN LITERS)', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'outofstock',
            },
        ),
        migrations.CreateModel(
            name='rolistModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('TimeStamp', models.CharField(max_length=100, null=True)),
                ('ModifiedBy', models.CharField(max_length=100, null=True)),
                ('Ship2Party', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100, null=True)),
                ('SOff.', models.CharField(max_length=100, null=True)),
                ('Rg', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'rolist',
            },
        ),
        migrations.CreateModel(
            name='romobileModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('TimeStamp', models.CharField(max_length=100, null=True)),
                ('ModifiedBy', models.CharField(max_length=100, null=True)),
                ('Mobile Number', models.CharField(max_length=100)),
                ('Ship-To Party', models.CharField(max_length=100)),
                ('Sales Office', models.CharField(max_length=100)),
                ('Distribution Channel', models.CharField(max_length=100, null=True)),
                ('Differ.Refer.Code', models.CharField(max_length=100, null=True)),
                ('Mobile Type', models.CharField(max_length=100)),
                ('Name 1', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100, null=True)),
                ('Description', models.CharField(max_length=100, null=True)),
                ('Created By', models.CharField(max_length=100, null=True)),
                ('Created On', models.CharField(max_length=100, null=True)),
                ('Time', models.CharField(max_length=100, null=True)),
                ('E-Mail Address', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'romobile',
            },
        ),
        migrations.CreateModel(
            name='yv208Model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('TimeStamp', models.CharField(max_length=100, null=True)),
                ('ModifiedBy', models.CharField(max_length=100, null=True)),
                ('Exception', models.CharField(max_length=100, null=True)),
                ('Material', models.CharField(max_length=100)),
                ('Shipment', models.CharField(max_length=100, null=True)),
                ('Shp.Status', models.CharField(max_length=100, null=True)),
                ('Vehicle', models.CharField(max_length=100)),
                ('Ship2Party', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Delivery', models.CharField(max_length=100, null=True)),
                ('Quantity', models.CharField(max_length=100, null=True)),
                ('Sales Unit', models.CharField(max_length=100, null=True)),
                ('Delivery quantity', models.CharField(max_length=100, null=True)),
                ('Seal No.', models.CharField(max_length=100, null=True)),
                ('Invoice', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'yv208',
            },
        ),
        migrations.CreateModel(
            name='yv209dModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('TimeStamp', models.CharField(max_length=100, null=True)),
                ('ModifiedBy', models.CharField(max_length=100, null=True)),
                ('Exception', models.CharField(max_length=100, null=True)),
                ('DelCt', models.CharField(max_length=100, null=True)),
                ('PRTY', models.CharField(max_length=100, null=True)),
                ('Requested deliv.date', models.CharField(max_length=100, null=True)),
                ('Sales Document', models.CharField(max_length=100)),
                ('Distribution Channel', models.CharField(max_length=100, null=True)),
                ('Ship2Party', models.CharField(max_length=100)),
                ('Name 1', models.CharField(max_length=100)),
                ('RTD(in KM)', models.CharField(max_length=100)),
                ('Material', models.CharField(max_length=100)),
                ('OrderQty', models.CharField(max_length=100, null=True)),
                ('Target quantity UoM', models.CharField(max_length=100, null=True)),
                ('Truck no.', models.CharField(max_length=100, null=True)),
                ('Sales Group Desc.', models.CharField(max_length=100, null=True)),
                ('REMARKS', models.CharField(max_length=100, null=True)),
                ('Sales Document Type', models.CharField(max_length=100, null=True)),
                ('Sales Document Item', models.CharField(max_length=100, null=True)),
                ('Created By', models.CharField(max_length=100, null=True)),
                ('Sales Group', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'yv209d',
            },
        ),
        migrations.CreateModel(
            name='yv26Model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('TimeStamp', models.CharField(max_length=100, null=True)),
                ('ModifiedBy', models.CharField(max_length=100, null=True)),
                ('Rec. Code', models.CharField(max_length=100)),
                ('Receiver', models.CharField(max_length=100)),
                ('Document', models.CharField(max_length=100, null=True)),
                ('Disp.Mat.Doc.', models.CharField(max_length=100, null=True)),
                ('Disp.Item', models.CharField(max_length=100, null=True)),
                ('Disp.St.Loc.', models.CharField(max_length=100, null=True)),
                ('Recv.Mat.Doc.', models.CharField(max_length=100, null=True)),
                ('Recv.Item', models.CharField(max_length=100, null=True)),
                ('Recv.St.Loc.', models.CharField(max_length=100, null=True)),
                ('PGI Date', models.DateTimeField(max_length=100)),
                ('Batch', models.CharField(max_length=100, null=True)),
                ('Mat.Code', models.CharField(max_length=100)),
                ('MoT', models.CharField(max_length=100, null=True)),
                ('InvoiceNo.', models.CharField(max_length=100)),
                ('Assign.No.', models.CharField(max_length=100, null=True)),
                ('Volume(KL)', models.CharField(max_length=100)),
                ('Volume(K15)', models.CharField(max_length=100, null=True)),
                ('Volume(K29)', models.CharField(max_length=100, null=True)),
                ('Volume(TO)', models.CharField(max_length=100, null=True)),
                ('Qty(EA)', models.CharField(max_length=100, null=True)),
                ('State', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'yv26',
            },
        ),
    ]
