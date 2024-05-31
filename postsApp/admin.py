from django.contrib import admin
from .models import PostClass


# Register your models here.
#tell system which models to upload to admin dashboard
admin.site.register(PostClass)
