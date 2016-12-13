from django.db import models
from django.contrib.auth.models import User as DjangoUser

'''
DjangoのデフォルトUserモデルを継承して、インスタンスメソッドを追加している
'''
class User(DjangoUser):

    '''
    新規にtableを作成せずに継承したmodelの拡張のみを行いたいので、
    MetaクラスのproxyをTrueにしている。
    '''
    class Meta:
        proxy = True

    '''
    Userインスタンスがフォローしているuserを返す関数
    '''
    def get_followers(self):
        relations = Relationship.objects.filter(follow=self)
        return [relation.follower for relation in relations]
        


'''
フォローしている人と、フォローされている人をつなぐ中間テーブル
'''
class Relationship(models.Model):
    follow = models.ForeignKey(User, related_name='follows')
    follower = models.ForeignKey(User, related_name='followers')
