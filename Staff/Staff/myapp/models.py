from django.db import models

class Task(models.Model):
    name = models.CharField('Имя сотрудника', max_length=100)
    num_staff = models.CharField('Номер сотрудника', max_length=100)
    mail = models.EmailField('Почта сотрудника')
    phone_number = models.CharField('Номер телефона сотрудника', max_length=100)
    job_CHOISES = (
        ('Программист', 'Программист'),
        ('Слесарь', 'Слесарь'),
        ('Бухглатер', 'Бухглатер')
    )
    job = models.CharField('Должность', max_length=100, choices=job_CHOISES, default="")

    def __str__(self):
        return self.num_staff

    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = 'Работники'


