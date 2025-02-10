import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from trans.models import MainPump

# Данные для основных насосов
main_pumps_data = [
    {
        "name": "НМ 125-550",
        "pump_type": "sectional",
        "flow_rate": 125,
        "head_per_stage": 550,
        "max_stages": 5,
        "power_per_stage": 400,
        "efficiency": 72,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Вода"
    },
    {
        "name": "НМ 180-500",
        "pump_type": "sectional",
        "flow_rate": 180,
        "head_per_stage": 500,
        "max_stages": 5,
        "power_per_stage": 400,
        "efficiency": 72,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Вода"
    },
    {
        "name": "НМ 250-475",
        "pump_type": "sectional",
        "flow_rate": 250,
        "head_per_stage": 475,
        "max_stages": 5,
        "power_per_stage": 500,
        "efficiency": 75,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Вода"
    },
    {
        "name": "НМ 360-460",
        "pump_type": "sectional",
        "flow_rate": 360,
        "head_per_stage": 460,
        "max_stages": 3,
        "power_per_stage": 630,
        "efficiency": 78,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Вода"
    },
    {
        "name": "НМ 500-300",
        "pump_type": "sectional",
        "flow_rate": 500,
        "head_per_stage": 300,
        "max_stages": 3,
        "power_per_stage": 500,
        "efficiency": 80,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Вода"
    },
    {
        "name": "НМ 710-280",
        "pump_type": "sectional",
        "flow_rate": 710,
        "head_per_stage": 280,
        "max_stages": 3,
        "power_per_stage": 800,
        "efficiency": 80,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Вода"
    },
    {
        "name": "НМ 1250-260",
        "pump_type": "spiral",
        "flow_rate": 1250,
        "head_per_stage": 260,
        "max_stages": 1,
        "power_per_stage": 1250,
        "efficiency": 80,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Нефтепродукты"
    },
    {
        "name": "НМ 1800-240",
        "pump_type": "spiral",
        "flow_rate": 1800,
        "head_per_stage": 240,
        "max_stages": 1,
        "power_per_stage": 1600,
        "efficiency": 83,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Нефтепродукты"
    },
    {
        "name": "НМ 2500-230",
        "pump_type": "spiral",
        "flow_rate": 2500,
        "head_per_stage": 230,
        "max_stages": 1,
        "power_per_stage": 2000,
        "efficiency": 86,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Нефтепродукты"
    },
    {
        "name": "НМ 3600-230",
        "pump_type": "spiral",
        "flow_rate": 3600,
        "head_per_stage": 230,
        "max_stages": 1,
        "power_per_stage": 2500,
        "efficiency": 87,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Нефтепродукты"
    },
    {
        "name": "НМ 5000-210",
        "pump_type": "spiral",
        "flow_rate": 5000,
        "head_per_stage": 210,
        "max_stages": 1,
        "power_per_stage": 3150,
        "efficiency": 88,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Нефтепродукты"
    },
    {
        "name": "НМ 7000-210",
        "pump_type": "spiral",
        "flow_rate": 7000,
        "head_per_stage": 210,
        "max_stages": 1,
        "power_per_stage": 5000,
        "efficiency": 89,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Нефтепродукты"
    },
    {
        "name": "НМ 10000-210",
        "pump_type": "spiral",
        "flow_rate": 10000,
        "head_per_stage": 210,
        "max_stages": 1,
        "power_per_stage": 6300,
        "efficiency": 89,
        "max_temperature": 373,
        "material": "Нержавеющая сталь",
        "fluid_type": "Нефтепродукты"
    }
]

# Заполнение базы данных основными насосами
for pump_data in main_pumps_data:
    MainPump.objects.create(**pump_data)

print("Основные насосы успешно добавлены!")