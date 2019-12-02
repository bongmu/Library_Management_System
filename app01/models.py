from django.db import models

# Create your models here.
# class Books(models.Model):
#     title = models.CharField(max_length=254)
#     price = models.DecimalField(max_digits=8,decimal_places=2)
#     publish_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)

    '''
    auto_now :每次修改数据的时候，会自动更新时间
    auto_now_add :当数据创建出来的时候，自动将创建时间记录下来
    '''
    publish = models.ForeignKey(to='Publish')
    authors = models.ManyToManyField(to='Author')

class Publish(models.Model):
    name = models.CharField(max_length=254)
    addr = models.CharField(max_length=254)

class Author(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    author_detail = models.OneToOneField(to='AuthorDetail')

class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    add = models.CharField(max_length=254)


class User(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=64)
    password = models.CharField(verbose_name='密码',max_length=64)
    gender_choices = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.IntegerField(verbose_name='性别',choices=gender_choices)

