from django.contrib import admin
from .models import Question, Choice


#admin.site.register(Question)
#admin.site.register(Choice)

#admin.site.site_header = "Polls admin"
#admin.site.site_title = "Polls admin area"
#admin.site.index_title = "Wecome to polls admin area"

class ChoiceInline (admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
