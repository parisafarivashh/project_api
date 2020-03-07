from django.contrib import admin

from accunt_api.models import Account

class AccountAdmin(admin.ModelAdmin):
  list_display =('email','username')

admin.site.register(Account,AccountAdmin)  