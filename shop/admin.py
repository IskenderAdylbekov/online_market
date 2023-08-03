from django.contrib import admin


from .models import Category, Product, Subcategory, Conversation, ConversationMessage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "created_by", "category", "subcategory"]
    list_display_links = ["name", "slug"]
    list_filter = ["is_sold", "created_at"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subcategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_display_links = ["name"]
    search_fields = ["name"]


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ["product", "slug", "created_at"]
    list_display_links = ["product", "created_at"]
    list_filter = ["modified_at", "members"]
    prepopulated_fields = {"slug": ("product",)}


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ["conversation", "slug", "created_by", "created_at"]
    list_display_links = ["conversation", "slug", "created_by"]
    list_filter = ["conversation", "created_by"]
    prepopulated_fields = {"slug": ("conversation",)}
