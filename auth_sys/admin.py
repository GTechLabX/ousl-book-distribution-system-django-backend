from django.contrib import admin
from .models import (
    CustomUser, ActivityLogs, SecurityInformation, UserPreference,
    Country, Report, TotalReportSummary, UserProfile
)

# Simple registrations
admin.site.register(CustomUser)
admin.site.register(ActivityLogs)
admin.site.register(SecurityInformation)
admin.site.register(UserPreference)
admin.site.register(Country)
admin.site.register(Report)
admin.site.register(TotalReportSummary)
admin.site.register(UserProfile)
