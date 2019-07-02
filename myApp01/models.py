# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    id = models.IntegerField(primary_key=True,db_column='address_id')
    userid = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True,db_column='user_id')
    addressName = models.CharField(max_length=200, blank=True, null=True,db_column='address_name')
    tel = models.CharField(max_length=200, blank=True, null=True,db_column='address_tel')
    province = models.CharField(max_length=200, blank=True, null=True,db_column='address_provice')
    detail = models.CharField(max_length=400, blank=True, null=True,db_column='address_detail')
    code = models.IntegerField(blank=True, null=True,db_column='address_code')

    def __str__(self):
        return self.addressName

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True,db_column='category_id')
    category_name = models.CharField(max_length=200, blank=True, null=True,db_column='category_name')
    category_parent = models.IntegerField(blank=True, null=True,db_column='category_parent')

    def __str__(self):
        return self.category_name



    class Meta:
        managed = False
        db_table = 'category'


class City(models.Model):
    # city_id = models.IntegerField(primary_key=True ,db_column='city_id')
    id = models.IntegerField(primary_key=True, db_column='city_id')
    # city_name = models.CharField(max_length=200, blank=True, null=True,db_column='city_name')
    name = models.CharField(max_length=200, blank=True, null=True, db_column='city_name')
    # city_sortkey = models.CharField(max_length=200, blank=True, null=True,db_column='city_sortkey')
    sortKey = models.CharField(max_length=200, blank=True, null=True, db_column='city_sortkey')
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'city'


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    prodouct = models.ForeignKey('Prodouct', models.DO_NOTHING, blank=True, null=True)
    comment_conent = models.CharField(max_length=400, blank=True, null=True)
    comment_time = models.CharField(max_length=100, blank=True, null=True)
    comment_star = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.comment_id

    class Meta:
        managed = False
        db_table = 'comment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()



    class Meta:
        managed = False
        db_table = 'django_migrations'


class Favorite(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    prodouct = models.ForeignKey('Prodouct', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.favorite_id

    class Meta:
        managed = False
        db_table = 'favorite'


class Orders(models.Model):
    orders_id = models.AutoField(primary_key=True, db_column='orders_id')
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, db_column='user_id')
    orders_prodouct_count = models.IntegerField(blank=True, null=True, db_column='orders_prodouct_count')
    orders_time = models.CharField(max_length=100, blank=True, null=True, db_column='orders_time')
    orders_all_price = models.CharField(max_length=200, blank=True, null=True, db_column='orders_all_price')
    orders_paystate = models.IntegerField(blank=True, null=True, db_column='orders_paystate')
    orders_prodouct_id = models.IntegerField(blank=True, null=True, db_column='orders_prodouct_id')

    def __str__(self):
        return self.orders_id

    class Meta:
        managed = False
        db_table = 'orders'


class Prodouct(models.Model):
    id = models.IntegerField(primary_key=True, db_column='prodouct_id')
    categoryId = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True,db_column='category_id')
    shopId = models.ForeignKey('Shop', models.DO_NOTHING, blank=True, null=True, db_column='shop_id')
    sub_category = models.ForeignKey('SubCategory', models.DO_NOTHING, blank=True, null=True, db_column='sub_category_id')#没改
    CityId = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True, db_column='city_id')
    title = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_title')
    sortTitle = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_sort_title')
    imgUrl = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_image')
    startTime = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_start_time')
    value = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_value')
    price = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_price')
    ribat = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_ribat')
    bought = models.CharField(max_length=11, blank=True, null=True, db_column='prodouct_bought')
    minQuota = models.IntegerField( db_column='prodouct_minquota')
    maxQuota = models.IntegerField(blank=True, null=True, db_column='prodouct_maxquota')
    post = models.CharField(max_length=200, blank=True, null=True, db_column='prodouct_post')
    soldOut = models.CharField(max_length=200, blank=True, null=True, db_column='prodouct_soldout')
    tip = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_tip')
    endTime = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_end_time')
    detail = models.CharField(max_length=400, blank=True, null=True, db_column='prodouct_detail')
    isRefund = models.IntegerField(blank=True, null=True, db_column='prodouct_is_refund')
    isOverTime = models.IntegerField(blank=True, null=True, db_column='prodouct_is_over_time')

    def __str__(self):
        return self.sortTitle

    class Meta:
        managed = False
        db_table = 'prodouct'


class Shop(models.Model):
    id = models.AutoField(primary_key=True, db_column='shop_id')
    name = models.CharField(max_length=400, blank=True, null=True, db_column='shop_name')
    tel = models.CharField(max_length=400, blank=True, null=True, db_column='shop_tel')
    address = models.CharField(max_length=400, blank=True, null=True, db_column='shop_address')
    area = models.CharField(max_length=400, blank=True, null=True, db_column='shop_area')
    opentime = models.CharField(max_length=400, blank=True, null=True, db_column='shop_open_time')
    lon = models.CharField(max_length=200, blank=True, null=True, db_column='shop_lon')
    lat = models.CharField(max_length=200, blank=True, null=True, db_column='shop_lat')
    shop_traffic_info = models.CharField(max_length=400, blank=True, null=True, db_column='shop_traffic_info')

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'shop'


class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    sub_category_name = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_category'


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    orders = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)
    ticket_valid_time = models.CharField(max_length=400, blank=True, null=True)
    ticket_number = models.IntegerField(blank=True, null=True)
    ticket_pwd = models.CharField(max_length=200, blank=True, null=True)
    ticket_is_used = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ticket_id

    class Meta:
        managed = False
        db_table = 'ticket'


class User(models.Model):
    id = models.AutoField(primary_key=True,db_column='user_id')
    name = models.CharField(max_length=200, blank=True, null=True,db_column='user_name')
    loginPwd = models.CharField(max_length=200, blank=True, null=True,db_column='user_login_pwd')
    payPwd = models.CharField(max_length=200, blank=True, null=True,db_column='user_pay_pwd')
    tel = models.CharField(max_length=200, blank=True, null=True,db_column='user_tel')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'user'
