from django.contrib import admin
from .models import UserProfile, Registration, Templates, Video

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Registration)
admin.site.register(Templates)
admin.site.register(Video)
