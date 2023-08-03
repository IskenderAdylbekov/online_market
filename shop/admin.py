from django.contrib import admin


from .models import Category, Product, Subcategory


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


# admin.site.register(Category)
# admin.site.register(Product)
