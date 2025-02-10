from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Pipeline(models.Model):
    PipelineID = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор трубопровода")
    Diameter = models.FloatField(verbose_name="Внутренний диаметр трубопровода (мм)")
    Length = models.FloatField(verbose_name="Длина трубопровода (км)")
    ElevationDifference = models.FloatField(verbose_name="Разность нивелирных высот (м)")
    ResidualHead = models.FloatField(verbose_name="Остаточный напор (м)")
    Temperature = models.FloatField(verbose_name="Расчетная температура (К)")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pipelines', verbose_name="Пользователь")

    def __str__(self):
        return f"Pipeline {self.PipelineID} by {self.user.username}"

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор продукта")  # Уникальный идентификатор продукта
    Name = models.CharField(max_length=100, verbose_name="Название продукта")  # Название продукта
    Density293 = models.FloatField(verbose_name="Плотность при 293К (кг/м³)")  # Плотность при 293К (кг/м³)
    Viscosity273 = models.FloatField(verbose_name="Вязкость при 273К (мм²/с)")  # Вязкость при 273К (мм²/с)
    Viscosity293 = models.FloatField(verbose_name="Вязкость при 293К (мм²/с)")  # Вязкость при 293К (мм²/с)

    def __str__(self):
        return self.Name

class Transportation(models.Model):
    TransportationID = models.AutoField(primary_key=True, verbose_name="Уникальный идентификатор перевозки")  # Уникальный идентификатор перевозки
    PipelineID = models.ForeignKey(Pipeline, on_delete=models.CASCADE, verbose_name="Трубопровод")  # Связь с таблицей Pipeline
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")  # Связь с таблицей Product
    Quantity = models.FloatField(verbose_name="Количество перевозимого продукта (млн.т/год)")  # Количество перевозимого продукта (млн.т/год)
    Percentage = models.FloatField(verbose_name="Процентное содержание продукта в перевозке")  # Процентное содержание продукта в перевозке

    def __str__(self):
        return f"Transportation {self.TransportationID}"

class MainPump(models.Model):
    # Типы насосов
    PUMP_TYPE_CHOICES = [
        ('sectional', 'Секционный многоступенчатый'),
        ('spiral', 'Спиральный одноступенчатый'),
    ]

    # Основные поля
    name = models.CharField(max_length=255, verbose_name="Название насоса")
    pump_type = models.CharField(max_length=20, choices=PUMP_TYPE_CHOICES, verbose_name="Тип насоса")
    flow_rate = models.FloatField(verbose_name="Производительность (м³/ч)")
    head_per_stage = models.FloatField(verbose_name="Напор на ступень (м)")
    max_stages = models.IntegerField(verbose_name="Максимальное количество ступеней", default=1)
    power_per_stage = models.FloatField(verbose_name="Мощность на ступень (кВт)")
    efficiency = models.FloatField(verbose_name="КПД (%)", default=80)
    max_temperature = models.FloatField(verbose_name="Максимальная температура (К)", default=373)
    material = models.CharField(max_length=255, verbose_name="Материал корпуса", default="Нержавеющая сталь")
    fluid_type = models.CharField(max_length=255, verbose_name="Тип перекачиваемой жидкости", default="Вода")

    def to_dict(self):
        return {
            'name': self.name,
            'flow_rate': self.flow_rate,
            'head_per_stage': self.head_per_stage,
            'max_stages': self.max_stages,
            'max_temperature': self.max_temperature,
            'power_per_stage': self.power_per_stage,
            'efficiency': self.efficiency,
        }

    def __str__(self):
        return self.name

class BoosterPump(models.Model):
    # Основные поля
    name = models.CharField(max_length=255, verbose_name="Название насоса")
    flow_rate = models.FloatField(verbose_name="Производительность (м³/ч)")
    head = models.FloatField(verbose_name="Напор (м)")
    power = models.FloatField(verbose_name="Мощность (кВт)")
    efficiency = models.FloatField(verbose_name="КПД (%)", default=70)
    max_temperature = models.FloatField(verbose_name="Максимальная температура (К)", default=373)
    material = models.CharField(max_length=255, verbose_name="Материал корпуса", default="Нержавеющая сталь")
    fluid_type = models.CharField(max_length=255, verbose_name="Тип перекачиваемой жидкости", default="Вода")


    def to_dict(self):
        return {
            'name': self.name,
            'flow_rate': self.flow_rate,
            'head': self.head,
            'power': self.power,
            'efficiency': self.efficiency,
            }
    def __str__(self):
        return self.name



from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('admin', 'Admin'),
    ]
    surname = models.CharField(max_length=150, blank=True, verbose_name="Фамилия")
    name = models.CharField(max_length=150, blank=True, verbose_name="Имя")
    patronymic = models.CharField(max_length=150, blank=True, verbose_name="Отчество")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='engineer', verbose_name="Роль")

    def __str__(self):
        return self.username