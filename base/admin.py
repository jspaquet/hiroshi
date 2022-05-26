from django.contrib import admin

from base.models import Bookmark
import requests
from bs4 import BeautifulSoup


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


class BookmarkAdmin(admin.ModelAdmin):
    actions = [fetch_missing_titles]


admin.site.register(Bookmark, BookmarkAdmin)
