from django.contrib import admin
from .models import Lead, User, Event, TopicCategory, UserInfo

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(UserInfo)
admin.site.register(Event)
admin.site.register(TopicCategory)