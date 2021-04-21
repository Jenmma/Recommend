# 类似于表的创建语句
# 做的是表结构和django内对象的映射关系
# 可以从model => 创建表
# 也可以创建表 => 导出为model
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.FloatField(blank=True, null=True, default=0.0)
    category = models.IntegerField(blank=True, null=True, default=0)
    categoryName = models.CharField(max_length=255,null=True, default="无")

    class Meta:
        managed = True
        db_table = 'user'


class UserRelation(models.Model):
    startid = models.IntegerField(blank=True, null=True, default=0)
    endid = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = True
        db_table = 'userrelation'
