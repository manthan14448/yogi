from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from home import views
admin.site.site_title ='Yogi Industries'
admin.site.site_header = 'Yogi Industries'
admin.site.index_title ='Applications'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),

]
class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            url('admin/report/report/',
                self.admin_view(views.report), name="preview"),
        ]
        return urls + custom_urls
