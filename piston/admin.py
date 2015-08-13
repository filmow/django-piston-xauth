# -*- coding: utf-8 -*-
from django.contrib import admin
from piston.models import Nonce, Token, Consumer


class ConsumerAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']


admin.site.register(Nonce)
admin.site.register(Token)
admin.site.register(Consumer, ConsumerAdmin)
