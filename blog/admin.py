from django.contrib import admin
from django.db import models
from django.forms import RadioSelect
from blog.models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'file_type')
    search_fields = ('title', 'content', 'tags')
    list_filter = ('created_at', 'file_type')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

    # 设置 file_type 字段为单选按钮
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'file_type':
            return db_field.formfield(
                widget=RadioSelect(choices=(
                    ('md', 'Markdown'),
                    ('html', 'HTML'),
                    ('txt', 'Text'),
                ))
            )
        return super().formfield_for_dbfield(db_field, request, **kwargs)

# 注册模型和对应的 ModelAdmin 类
admin.site.register(Blog, BlogAdmin)