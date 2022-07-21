from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from base.models import Bookmark
import requests
from bs4 import BeautifulSoup


class BookmarkResource(resources.ModelResource):
    class Meta:
        model = Bookmark


@admin.action(description='Fetch missing titles')
def fetch_missing_titles(modeladmin, request, queryset):
    for item in queryset:
        if item.title == '':
            item_requests = requests.get(item.link)
            soup = BeautifulSoup(item_requests.text, 'html.parser')
            print("Title of the website is : ")
            for title in soup.find_all('title'):
                print(title.get_text())
                item.title = title.get_text()
                item.save()


class BookmarkAdmin(ImportExportModelAdmin):
    actions = [fetch_missing_titles]
    resource_class = BookmarkResource


admin.site.register(Bookmark, BookmarkAdmin)
