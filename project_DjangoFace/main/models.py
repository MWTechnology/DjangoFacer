from django.db import models
from django.utils import timezone
from accounts.models import User

class Suspect(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    surname = models.CharField("Фамилия", max_length=100)
    name = models.CharField("Имя", max_length=100)
    patronymic = models.CharField("Отчество", max_length=100)
    passport = models.CharField("Паспорт", max_length=12)
    crimes = models.TextField("Характеристика")
    published_date = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField("Дата рождения", blank=True, null=True, help_text="<em>ДД.MM.ГГГГ</em>")

    def get_image_name(instance, img):
        people = 'main/train/%s/' % instance.passport
        author = '%s' % instance.author
        data_published = '_%s' % instance.published_date
        format= '.png'
        path = people + author + data_published + format
        return path
    image = models.ImageField("Фотопортрет", upload_to=get_image_name, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = "Подозреваймый"
        verbose_name_plural = "Подозреваймые"