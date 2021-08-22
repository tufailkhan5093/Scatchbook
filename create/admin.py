from django.contrib import admin
from .models import Occasion,Step2,Step3,prompt1,prompt2

# Register your models here.
@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    list_display=['event']

@admin.register(prompt1)
class Prompt1Admin(admin.ModelAdmin):
    list_display=['msg']

@admin.register(prompt2)
class Prompt2Admin(admin.ModelAdmin):
    list_display=['msg']

@admin.register(Step2)
class Step2Admin(admin.ModelAdmin):
    list_display=['firstname','lastname','cover_pic','dead_line']

@admin.register(Step3)
class Step3Admin(admin.ModelAdmin):
    list_display=['first','second','third']