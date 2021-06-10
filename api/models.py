from django.db import models

# Create your models here.
class Log(models.Model):
    created_at=models.DateTimeField(
        verbose_name='登録時間',
        auto_now_add=True,
    )
    temperature=models.FloatField(
        verbose_name='気温',
        blank=True
    )
    humidity=models.FloatField(
        verbose_name='湿度',
        blank=True
    )
#登録時間、気温、湿度の登録モデルの作成

    def __str__(self):
        return str(self.created_at)

    class Meta:
        verbose_name='採取データ'
        verbose_name_plural='採取データ'
