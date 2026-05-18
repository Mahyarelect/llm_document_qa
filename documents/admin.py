from django.contrib import admin
from .models import Document, DocumentChunk, QuestionHistory


class DocumentChunkInline(admin.TabularInline):
    model = DocumentChunk
    extra = 0
    readonly_fields = ('content', 'chunk_index')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'full_text')
    readonly_fields = ('full_text', 'created_at', 'updated_at')
    inlines = [DocumentChunkInline]


@admin.register(DocumentChunk)
class DocumentChunkAdmin(admin.ModelAdmin):
    list_display = ('document', 'chunk_index')
    search_fields = ('content',)


@admin.register(QuestionHistory)
class QuestionHistoryAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    search_fields = ('question', 'answer', 'retrieved_context')
    readonly_fields = ('created_at',)