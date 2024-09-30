from django.contrib import admin
from django.utils.html import format_html
from .models import FormResponse

@admin.register(FormResponse)
class FormResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'timestamp','feedback', 'photo_tag', 'cv_link')  # Display name, email, timestamp, photo, and CV
    search_fields = ('name', 'email')
    list_filter = ('timestamp',)

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<a href="{}" target="_blank">View Photo</a>',
                obj.photo.url, obj.photo.url
            )
        return "No Photo"

    def cv_link(self, obj):
        if obj.cv:
            return format_html('<a href="{}" target="_blank">View CV</a>'.format(obj.cv.url))
        return "No CV"

    photo_tag.short_description = 'Photo'  # Title for the photo column
    cv_link.short_description = 'CV'  # Title for the CV column
