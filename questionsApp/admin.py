from django.contrib import admin
#imported from current directory, hence the fullstop
from .models import QuestionClass


# Register your models here.
#tell system which models to upload to admin dashboard
admin.site.register(QuestionClass)