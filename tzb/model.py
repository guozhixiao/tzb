# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DongtaiGanzhiCopy1(models.Model):
    title = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    add_time = models.CharField(max_length=30)
    shijianbiaoti = models.TextField(blank=True, null=True)
    shijianmailuo = models.TextField(blank=True, null=True)
    shijianliebiao = models.TextField(blank=True, null=True)
    chuanboqushi = models.TextField(blank=True, null=True)
    ciyun = models.TextField(blank=True, null=True)
    meitihuoyuedu = models.TextField(blank=True, null=True)
    meitilaiyuan = models.TextField(blank=True, null=True)
    qingganzhanbi = models.TextField(blank=True, null=True)
    qingganfenxi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dongtai_ganzhi_copy1'


class EnterprisesNumber(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    key = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enterprises_number'


class GangEnterprises(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=20)
    range = models.CharField(max_length=255)
    hangye = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    from_field = models.CharField(db_column='from', max_length=20)  # Field renamed because it was a Python reserved word.
    legal_name = models.CharField(max_length=255)
    zhuce_ziben = models.CharField(max_length=255)
    all_num = models.IntegerField()
    status = models.IntegerField()
    landmark = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gang_enterprises'


class Gangaotai(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    birthday = models.IntegerField()
    age = models.IntegerField()
    shenfen = models.CharField(max_length=20)
    zhiye = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    gettime = models.IntegerField()
    phone = models.CharField(max_length=20)
    landmark = models.CharField(max_length=30)
    mark = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gangaotai'


class GangaotaiBak(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    birthday = models.IntegerField()
    age = models.IntegerField()
    shenfen = models.CharField(max_length=20)
    zhiye = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    gettime = models.IntegerField()
    phone = models.CharField(max_length=20)
    landmark = models.CharField(max_length=30)
    mark = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gangaotai_bak'


class GatEnterprises(models.Model):
    name = models.CharField(max_length=255)
    from_field = models.CharField(db_column='from', max_length=20)  # Field renamed because it was a Python reserved word.
    phone = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    birthday = models.CharField(max_length=20)
    education = models.CharField(max_length=255)
    charge_name = models.CharField(max_length=255)
    charge_birthday = models.CharField(max_length=255)
    charge_education = models.CharField(max_length=255)
    all_num = models.IntegerField()
    tj_num = models.IntegerField()
    dl_num = models.IntegerField()
    status = models.IntegerField()
    landmark = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gat_enterprises'


class HotArc(models.Model):
    type = models.IntegerField()
    news_uuid = models.CharField(max_length=32)
    news_title = models.CharField(max_length=255)
    news_url = models.CharField(max_length=500)
    picurl = models.CharField(max_length=500)
    news_posttime = models.DateTimeField()
    app_name = models.CharField(max_length=255)
    news_read_count = models.IntegerField()
    status = models.IntegerField()
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hot_arc'


class Independents(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    work_job = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=True, null=True)
    education = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    political = models.CharField(max_length=255)
    status = models.IntegerField()
    landmark = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'independents'


class IndependentsZhishi(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    work_job = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=True, null=True)
    education = models.CharField(max_length=255)
    dang_time = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    jisheng_time = models.CharField(max_length=255)
    status = models.IntegerField()
    landmark = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'independents_zhishi'


class Keys(models.Model):
    openid = models.CharField(max_length=50)
    biz = models.CharField(max_length=50)
    uinion = models.CharField(max_length=50)
    money = models.FloatField()
    keys = models.TextField()
    istui = models.IntegerField()
    isuse = models.IntegerField()
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'keys'


class Log(models.Model):
    openid = models.CharField(max_length=50)
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'log'


class MapLandmark(models.Model):
    relate_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20)
    source = models.CharField(max_length=255, blank=True, null=True)
    remark = models.TextField()
    pic = models.CharField(max_length=255, blank=True, null=True)
    fuzeren = models.CharField(max_length=20, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'map_landmark'


class Member(models.Model):
    openid = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100)
    realname = models.CharField(max_length=30)
    headimg = models.CharField(max_length=200)
    uinion = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    money = models.FloatField()
    getmoney = models.FloatField()
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'member'


class Namestr(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'namestr'


class PartyMember(models.Model):
    member_name = models.CharField(max_length=10, blank=True, null=True)
    member_sex = models.CharField(max_length=5, blank=True, null=True)
    member_birth = models.CharField(max_length=50, blank=True, null=True)
    work_place = models.CharField(max_length=150, blank=True, null=True)
    member_post = models.CharField(max_length=255, blank=True, null=True)
    member_posts = models.CharField(max_length=255, blank=True, null=True)
    postname = models.CharField(max_length=20, blank=True, null=True)
    education = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_member'


class PartyMinjian(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    birth = models.CharField(max_length=50, blank=True, null=True)
    work_post = models.CharField(max_length=255, blank=True, null=True)
    work_posts = models.CharField(max_length=255, blank=True, null=True)
    personal_phone = models.CharField(max_length=150, blank=True, null=True)
    office_phone = models.CharField(max_length=150, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'party_minjian'


class PartyMinmeng(models.Model):
    ally_name = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    ally_number = models.IntegerField(blank=True, null=True)
    join_time = models.CharField(max_length=50, blank=True, null=True)
    birth_time = models.CharField(max_length=50, blank=True, null=True)
    work_place = models.CharField(max_length=255, blank=True, null=True)
    work_post = models.CharField(max_length=20, blank=True, null=True)
    work_posts = models.CharField(max_length=255, blank=True, null=True)
    personal_phone = models.CharField(max_length=150, blank=True, null=True)
    office_phone = models.CharField(max_length=150, blank=True, null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    university = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=20, blank=True, null=True)
    political_work = models.TextField(blank=True, null=True)
    work_honor = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'party_minmeng'


class PartyXinshehui(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    mingzu = models.CharField(max_length=5, blank=True, null=True)
    native_place = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    birth = models.CharField(max_length=150, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    work_start = models.CharField(max_length=50, blank=True, null=True)
    work_name = models.CharField(max_length=255, blank=True, null=True)
    work_area = models.CharField(max_length=255, blank=True, null=True)
    jieceng_type = models.CharField(max_length=150, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'party_xinshehui'


class PrivateEnterprises(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=20)
    job = models.CharField(max_length=255)
    work_job = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255)
    remark2 = models.CharField(max_length=255)
    landmark = models.CharField(max_length=30)
    status = models.IntegerField()
    pic = models.CharField(max_length=255)
    descr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'private_enterprises'


class ReportData(models.Model):
    address = models.CharField(max_length=255)
    zj_num = models.IntegerField()
    gat_num = models.IntegerField()
    mzd_num = models.IntegerField()
    wdp_num = models.IntegerField()
    stqy_num = models.IntegerField()
    landmark = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'report_data'


class SensitivePersonnel(models.Model):
    name = models.CharField(max_length=22, blank=True, null=True)
    id_card = models.CharField(max_length=18, blank=True, null=True)
    face_address = models.TextField(blank=True, null=True)
    face_information = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensitive_personnel'


class TongzhanMsg(models.Model):
    type = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tongzhan_msg'


class TongzhanNumber(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tongzhan_number'


class TongzhanWeiyuan(models.Model):
    zhenbie = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    weiyuan = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    minzu = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    landmark = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tongzhan_weiyuan'


class TongzhanZhuangan(models.Model):
    zhenbie = models.CharField(max_length=255)
    zhuangan = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    minzu = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tongzhan_zhuangan'


class User(models.Model):
    username = models.CharField(max_length=255)
    auth_key = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=255)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    role = models.SmallIntegerField()
    status = models.SmallIntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class VideoMonitor(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'video_monitor'


class WxGroup(models.Model):
    group_name = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bad_word = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    landmark = models.CharField(max_length=30)
    last_time = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'wx_group'


class WxNickname(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    wx_nickname = models.CharField(db_column='WX_NICKNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    wx_openid = models.CharField(db_column='WX_OPENID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    wx_biz = models.CharField(db_column='WX_BIZ', max_length=150, blank=True, null=True)  # Field name made lowercase.
    wx_type = models.IntegerField(db_column='WX_TYPE', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    wx_name = models.CharField(db_column='WX_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    wx_logo = models.CharField(db_column='WX_LOGO', max_length=900, blank=True, null=True)  # Field name made lowercase.
    wx_qrcode = models.CharField(db_column='WX_QRCODE', max_length=900, blank=True, null=True)  # Field name made lowercase.
    wx_note = models.CharField(db_column='WX_NOTE', max_length=1500, blank=True, null=True)  # Field name made lowercase.
    wx_vip = models.CharField(db_column='WX_VIP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wx_vip_note = models.CharField(db_column='WX_VIP_NOTE', max_length=900, blank=True, null=True)  # Field name made lowercase.
    wx_country = models.CharField(db_column='WX_COUNTRY', max_length=90, blank=True, null=True)  # Field name made lowercase.
    wx_province = models.CharField(db_column='WX_PROVINCE', max_length=90, blank=True, null=True)  # Field name made lowercase.
    wx_city = models.CharField(db_column='WX_CITY', max_length=90, blank=True, null=True)  # Field name made lowercase.
    wx_title = models.CharField(db_column='WX_TITLE', max_length=600, blank=True, null=True)  # Field name made lowercase.
    wx_url = models.CharField(db_column='WX_URL', max_length=600, blank=True, null=True)  # Field name made lowercase.
    wx_url_posttime = models.CharField(db_column='WX_URL_POSTTIME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    time_start = models.CharField(db_column='TIME_START', max_length=60, blank=True, null=True)  # Field name made lowercase.
    time_end = models.CharField(db_column='TIME_END', max_length=60, blank=True, null=True)  # Field name made lowercase.
    time_get = models.CharField(db_column='TIME_GET', max_length=60, blank=True, null=True)  # Field name made lowercase.
    time_stop = models.CharField(db_column='TIME_STOP', max_length=60, blank=True, null=True)  # Field name made lowercase.
    uid = models.BigIntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    add_time = models.CharField(db_column='ADD_TIME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    isenable = models.IntegerField(db_column='ISENABLE', blank=True, null=True)  # Field name made lowercase.
    ispush = models.IntegerField(db_column='ISPUSH', blank=True, null=True)  # Field name made lowercase.
    category_id = models.CharField(max_length=300, blank=True, null=True)
    category_name = models.CharField(max_length=300, blank=True, null=True)
    category_sub_name = models.CharField(max_length=300, blank=True, null=True)
    link_name = models.CharField(max_length=300, blank=True, null=True)
    link_unit = models.CharField(max_length=765, blank=True, null=True)
    link_position = models.CharField(max_length=300, blank=True, null=True)
    link_tel = models.CharField(max_length=60, blank=True, null=True)
    link_wx = models.CharField(max_length=300, blank=True, null=True)
    link_qq = models.CharField(max_length=60, blank=True, null=True)
    link_email = models.CharField(max_length=150, blank=True, null=True)
    update_time = models.CharField(max_length=765, blank=True, null=True)
    update_status = models.IntegerField(blank=True, null=True)
    overseas = models.IntegerField(blank=True, null=True)
    types = models.CharField(max_length=90, blank=True, null=True)
    wx_district = models.CharField(db_column='WX_DISTRICT', max_length=150, blank=True, null=True)  # Field name made lowercase.
    copyright = models.IntegerField(blank=True, null=True)
    wci = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    update_wx = models.CharField(max_length=765, blank=True, null=True)
    wx_nickname_tags = models.CharField(max_length=765, blank=True, null=True)
    wx_account_tags = models.CharField(max_length=765, blank=True, null=True)
    wx_url_hour = models.IntegerField(blank=True, null=True)
    is_many_times = models.IntegerField(blank=True, null=True)
    is_subscription = models.IntegerField(blank=True, null=True)
    is_rank = models.IntegerField(blank=True, null=True)
    density = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    row_update_time = models.DateTimeField()
    read_book_id = models.CharField(max_length=150, blank=True, null=True)
    update_wx_vip_time = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wx_nickname'


class ZongjiaoAddrinfo(models.Model):
    name = models.CharField(max_length=20)
    pic = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    zongjiao = models.CharField(max_length=50)
    fuzeren = models.CharField(max_length=20)
    landmark = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    descr = models.CharField(max_length=1000)
    addtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zongjiao_addrinfo'


class ZongjiaoMingzu(models.Model):
    mingzu = models.CharField(max_length=50)
    nannumber = models.IntegerField()
    nvnumber = models.IntegerField()
    allnumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zongjiao_mingzu'


class ZongjiaoNumber(models.Model):
    zongjiao = models.CharField(max_length=50)
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zongjiao_number'
