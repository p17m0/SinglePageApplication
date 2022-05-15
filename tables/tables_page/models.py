from django.utils import timezone

from django.db import models

# Create your models here.
# columns: date, name, quantity, distance
# Таблица должна иметь сортировку по всем полям кроме даты. 
# Фильтрация должна быть в виде двух выпадающих списков и текстового поля:
#     1. Выбор колонки, по которой будет фильтрация
#     2. Выбор условия (равно, содержит, больше, меньше)
#     3. Поле для ввода значения для фильтрации
# Таблица должна содержать пагинацию
# Вся таблица должна работать без перезагрузки страницы.


class Table(models.Model):
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=30, null=True)
    quantity = models.CharField(max_length=30, null=True)
    distance = models.CharField(max_length=30, null=True)
