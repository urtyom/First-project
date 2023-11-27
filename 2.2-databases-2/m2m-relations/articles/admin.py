from django import forms
from django.contrib import admin

from .models import Article, Tag, Scope


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass

from django.contrib import admin
from django.forms.models import BaseInlineFormSet

class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_scopes = [form.cleaned_data.get('is_main') for form in self.forms]
        if main_scopes.count(True) != 1:
            raise forms.ValidationError('Должен быть указан один и только один основной раздел.')

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormSet

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
