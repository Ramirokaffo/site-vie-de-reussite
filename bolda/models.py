# from django.contrib import admin
# # from .models import User

# class MyUserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'is_active', 'is_staff']

#     def get_actions(self, request):
#         actions = super().get_actions(request)

#         # Ajouter une nouvelle action personnalisée
#         custom_delete_action = admin.action(self.my_custom_delete)
#         custom_delete_action.label = 'Supprimer mes utilisateurs sélectionnés'

#         actions['my_custom_delete'] = custom_delete_action
#         return actions

#     def my_custom_delete(self, request, queryset):
#         # Effectuer une action personnalisée sur les utilisateurs sélectionnés
#         # ...
#         pass
