from django.db import models
from datetime import datetime
# В этом файле принято создавать классы, описывающие
# структуры, необходимых приложению таблиц


# https://docs.djangoproject.com/en/4.2/topics/db/models/
class Task(models.Model):
    # id создастся сам!
    nachalo = models.DateField(default=datetime.now)
    conets = models.DateField()
    description = models.CharField('Описание', max_length=256, default='')
    done = models.BooleanField('Статус', default=False)

    def __str__(self):
        return str(self.description)

    class Meta:
        verbose_name = 'Задача'
        verbose_name = 'Задачу'
        verbose_name_plural = 'задачь'
        verbose_name_plural = 'Задачи'

    def verbose_name_plural(n, var=['Задача', 'Задачи', 'Задачь']):
        n = n % 100
        if n < 5 or (n > 20):
            if (n % 10) in [2, 3, 4]:
                return var[1]
            if (n % 10) == 1:
                return var[0]
        return var[2]