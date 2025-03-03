from django.contrib import admin
from .models import Question, Answer, Score, GameUser

# Register your models here.
admin.site.register(Answer)
admin.site.register(Score)
admin.site.register(GameUser)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'q_type', 'difficulty', 'category', 'created_at')
    search_fields = ('text',)
    list_filter = ('q_type', 'category', 'difficulty')
    inlines = [AnswerInline]  # Hozzáadjuk az Answer modellt inline-ként