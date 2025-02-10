from django.contrib import admin
from .models import Pipeline, Product, Transportation,BoosterPump,MainPump,User
# Регистрируем модели для админки
admin.site.register(Pipeline)
admin.site.register(Product)
admin.site.register(Transportation)
admin.site.register(MainPump)
admin.site.register(BoosterPump)
admin.site.register(User)

