# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    admin_name = models.CharField(primary_key=True, max_length=10)
    passwd = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'admins'
        unique_together = (('admin_name', 'passwd'),)
        
class Dealers(models.Model):
    dealer_id = models.CharField(primary_key=True, max_length=5)
    dealer_name=models.CharField(max_length=20)
    dlpasswd = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'dealers'
        unique_together = (('dealer_id', 'dealer_name','dlpasswd'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    cust_id = models.CharField(max_length=5,primary_key=True)
    cust_name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=7)
    annual_income = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Deal(models.Model):
    deal_date = models.DateField(primary_key=True)
    dealer = models.ForeignKey('DealerInventory', models.DO_NOTHING)
    cust_id = models.CharField(max_length=5)
    vin = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vin')

    class Meta:
        managed = False
        db_table = 'deal'
        unique_together = (('deal_date', 'dealer', 'vin', 'cust_id'),)


class DealerInventory(models.Model):
    dealer_id = models.CharField(primary_key=True, max_length=5)
    dealer_name = models.CharField(max_length=20)
    buy_in_date = models.DateField()
    vin = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vin')

    class Meta:
        managed = False
        db_table = 'dealer_inventory'
        unique_together = (('dealer_id', 'buy_in_date', 'vin'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Engines(models.Model):
    engine_id = models.CharField(primary_key=True, max_length=5)
    model = models.CharField(max_length=5, blank=True, null=True)
    supplier_id = models.CharField(max_length=5)
    supplier_name = models.CharField(max_length=20)
    engine_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'engines'
        unique_together = (('engine_id', 'supplier_id', 'supplier_name', 'engine_date'),)


class Options(models.Model):
    vin = models.OneToOneField('Vehicle', models.DO_NOTHING, db_column='vin', primary_key=True)
    color = models.CharField(max_length=10)
    engine = models.ForeignKey(Engines, models.DO_NOTHING, blank=True, null=True)
    trans = models.ForeignKey('Transmissions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class PlantInventory(models.Model):
    plant_id = models.CharField(primary_key=True, max_length=5)
    plant_name = models.CharField(max_length=20)
    assembly_date = models.DateField()
    vin = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vin')

    class Meta:
        managed = False
        db_table = 'plant_inventory'
        unique_together = (('plant_id', 'assembly_date', 'vin'),)


class Price(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    style = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price'
        unique_together = (('brand', 'model', 'style'),)


class Transmissions(models.Model):
    trans_id = models.CharField(primary_key=True, max_length=5)
    model = models.CharField(max_length=5, blank=True, null=True)
    supplier_id = models.CharField(max_length=5)
    supplier_name = models.CharField(max_length=20)
    trans_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'transmissions'
        unique_together = (('trans_id', 'supplier_id', 'supplier_name', 'trans_date'),)


class Vehicle(models.Model):
    vin = models.CharField(primary_key=True, max_length=7)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    style = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'vehicle'
        unique_together = (('vin', 'brand', 'model', 'style'),)
