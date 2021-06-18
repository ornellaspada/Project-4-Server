from django.contrib import admin
from .models import Comment, Runaway, Rental, Purchase


admin.site.register(Runaway)
admin.site.register(Comment)
admin.site.register(Rental)
admin.site.register(Purchase)




