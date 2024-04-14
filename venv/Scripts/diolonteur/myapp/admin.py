from django.contrib import admin
from .models import our_user, Proposition, Request, Category
admin.site.register(our_user)
admin.site.register(Proposition)
admin.site.register(Request)
admin.site.register(Category)
# Register your models here.
