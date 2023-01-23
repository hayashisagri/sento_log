from django.contrib.gis.db import models

from accounts.models import UserAccount


class Area(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'areas'
        verbose_name = '市町村'


class Sento(models.Model):
    name = models.CharField(max_length=255, verbose_name='銭湯名')
    description = models.TextField(verbose_name='紹介文')
    address = models.CharField(max_length=255, verbose_name='住所')
    time_open = models.CharField(max_length=255, verbose_name='営業時間', blank=True)
    day_close = models.CharField(max_length=255, verbose_name='定休日', blank=True)
    profile_image = models.ImageField(verbose_name='画像', blank=True)
    station_distance = models.CharField(max_length=255, verbose_name='アクセス', blank=True)
    homepage_url = models.CharField(max_length=255, verbose_name='施設URL', blank=True)
    point = models.PointField(geography=True, srid=4326, verbose_name='所在地緯度経度')
    area = models.ForeignKey(Area, verbose_name='市区町村', on_delete=models.PROTECT, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sentos'
        verbose_name = '銭湯'


class UserSentoVisit(models.Model):
    user = models.ForeignKey(UserAccount, verbose_name='ユーザー', on_delete=models.CASCADE)
    sento = models.ForeignKey(Sento, verbose_name='銭湯', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_sento_visits'
        verbose_name = '銭湯訪問履歴'
