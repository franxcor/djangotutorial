from django.contrib import admin

from .models import Question, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 #specifies 3 extra spots
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields" : ["question_text"]}),
        ("Date information", {"fields" : ["pub_date"], "classes": ["colllapse"]}),
    ]
    inlines=[ChoiceInline]

    list_display = ["question_text", "pub_date", "was_published_recently", "has_choices"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_per_page = 5

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "votes", "question"]
    search_fields=["choice_text"]
    list_per_page = 5
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)