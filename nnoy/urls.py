from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name="page_main"),
    path('pages/a/<int:id>/', type_a_page, name="page_type_a"),
    path('pages/b/<int:id>/', type_b_page, name="page_type_b"),
    path('news/', news_page, name="page_news"),
    path('news/<int:id>/', news_detail_page, name="page_news_detail"),
    path('available-spots/', available_spots_page, name="page_available_spots"),
    path('teachers/', teachers_page, name="page_teachers"),
    path('teachers/<int:id>/', teachers_detail_page, name="page_teachers_detail"),
    path('achievments/', achievments_page, name="page_achievments"),
    path('achievments/<int:id>/', achievments_detail_page, name="page_achievments_detail"),
    path('append/', append_page, name="page_append"),
    path('cuisine/', cuisine_page, name="page_cuisine"),
    path('help-school/', help_page, name="page_help_school"),
    path('vacancy/', vacancy_page, name="page_vacancy"),
    path('attestation/', attestation_page, name="page_attestation"),
    path('schedule/', schedule_page, name="page_schedule"),
    path('schedule-bus/', schedule_bus_page, name="page_schedule_bus"),
    path('subjects/', subjects_page, name="page_subjects"),
    path('subjects/<int:id>/', subjects_detail_page, name="page_subjects_detail"),
    path('social-psychology-service/', social_psychology_page, name="page_social_psychology"),
    path('additional-education/', additional_education_page, name="page_additional_education"),
    path('additional-organization/', additional_organization_page, name="page_additional_organization"),
    path('school-information/', school_information_main, name="page_school_information_main"),
    path('school-information/history/', school_information_history_page, name="page_school_information_history"),
    path('school-information/<int:id>/', school_information_detail, name="page_school_information_detail"),
    path('contacts/', contacts_page, name="page_contacts"),
    path('administrative-control/', administrative_control_page, name="page_administrative_control"),
    path('administrative-control/<int:id>/', administrative_control_detail_page, name="page_administrative_control_detail"),
    path('documents/', documents_page, name="page_documents"),
    path('documents/<int:id>/', documents_detail_page, name="page_documents_detail"),
    path('gallery/', gallery_page, name="page_gallery"),
    path('gallery/<int:id>/', gallery_detail_page, name="page_gallery_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)