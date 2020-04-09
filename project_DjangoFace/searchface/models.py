from django.db import models
from accounts.models import User

class Mysearchface(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    name = models.CharField("Имя", max_length=100)
    passport = models.CharField("Паспорт", max_length=12)

    def get_image_name(instance, img):
        stat = 'main/test/'
        author = '%s' % instance.author
        format= '.png'
        path = stat + author + format
        return path
    image = models.ImageField("Фотопортрет", upload_to=get_image_name, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поиск"
        verbose_name_plural = "Поиски"