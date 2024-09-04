from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'get_first_name', 'get_last_name', 'user_group', 'create_by_adr')  # Usa métodos personalizados para obtener los nombres
    search_fields = ('user__username', 'user__groups__name')  # Asegúrate de que los campos sean válidos
    list_filter = ('user__groups__name',)  # list_filter debe ser una tupla o lista

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
    user_group.short_description = 'Group'

admin.site.register(Profile, ProfileAdmin)
