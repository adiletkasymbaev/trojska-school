from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django.contrib import messages
from django.utils.html import format_html
from .models import *

admin.site.register(Category)
admin.site.register(Article)

admin.site.register(AchievmentCategory)
admin.site.register(Achievment)

admin.site.register(GalleryCategory)
admin.site.register(Gallery)
admin.site.register(GalleryItem)

admin.site.register(AdditionalOrganization)
admin.site.register(SchoolInformationDonation)

admin.site.register(WebsiteImage)
admin.site.register(BellSchedule)
admin.site.register(SubjectWeek)

admin.site.register(Grade)
admin.site.register(GradeNumber)
admin.site.register(GradeFullness)

admin.site.register(Tag)
admin.site.register(Teacher)
admin.site.register(TeacherCategory)

admin.site.register(GenericPageCategory)

class AdministrativeControlLinkInline(admin.TabularInline):
  model = AdministrativeControlLink
  extra = 1

@admin.register(AdministrativeControl)
class AdministrativeControlAdmin(admin.ModelAdmin):
  list_display = ('title',)
  inlines = [AdministrativeControlLinkInline]

class BusScheduleTimeInline(admin.TabularInline):
  model = BusScheduleTime
  extra = 1

@admin.register(BusSchedule)
class BusScheduleAdmin(admin.ModelAdmin):
  inlines = [BusScheduleTimeInline]

class DocumentLinkInline(admin.TabularInline):
  model = DocumentLink
  extra = 1

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
  list_display = ('title',)
  inlines = [DocumentLinkInline]

class GenericPageA_ParagraphInline(admin.TabularInline):
  model = GenericPageA_Paragraph
  extra = 1

@admin.register(GenericPageB)
class GenericPageBAdmin(admin.ModelAdmin):
  readonly_fields = ['public_link']

  def public_link(self, obj):
    if obj.pk:
      return format_html('<a href="{}" target="_blank">Перейти на страницу</a>', obj.get_absolute_url())
    return "Сохраните объект, чтобы получить ссылку"

  public_link.short_description = "Публичная страница"

  def response_add(self, request, obj, post_url_continue=None):
    response = super().response_add(request, obj, post_url_continue)
    messages.add_message(
      request,
      messages.INFO,
      format_html('Страница создана: <a href="{}" target="_blank">{}</a>', obj.get_absolute_url(), obj)
    )
    return response

@admin.register(GenericPageA)
class GenericPageAAdmin(admin.ModelAdmin):
  inlines = [GenericPageA_ParagraphInline]
  readonly_fields = ['public_link']

  def public_link(self, obj):
    if obj.pk:
      return format_html('<a href="{}" target="_blank">Перейти на страницу</a>', obj.get_absolute_url())
    return "Сохраните объект, чтобы получить ссылку"

  public_link.short_description = "Публичная страница"

  def response_add(self, request, obj, post_url_continue=None):
    response = super().response_add(request, obj, post_url_continue)
    messages.add_message(
      request,
      messages.INFO,
      format_html('Страница создана: <a href="{}" target="_blank">{}</a>', obj.get_absolute_url(), obj)
    )
    return response

class SocialPsychologyServiceLinkInline(admin.TabularInline):
  model = SocialPsychologyServiceLink
  extra = 1

@admin.register(SocialPsychologyService)
class SocialPsychologyServiceAdmin(SingletonModelAdmin):
  inlines = [SocialPsychologyServiceLinkInline]

class AdditionalEducationLinkInline(admin.TabularInline):
  model = AdditionalEducationLink
  extra = 1

@admin.register(AdditionalEducation)
class AdditionalEducationAdmin(SingletonModelAdmin):
  inlines = [AdditionalEducationLinkInline]

class AppendAlgoritmStepInline(admin.TabularInline):
  model = AppendAlgoritmStep
  extra = 5

@admin.register(AppendAlgoritm)
class AppendAlgoritmAdmin(SingletonModelAdmin):
  inlines = [AppendAlgoritmStepInline]

class AttestationItemInline(admin.TabularInline):
  model = AttestationItem
  extra = 3

@admin.register(Attestation)
class AttestationAdmin(SingletonModelAdmin):
  inlines = [AttestationItemInline]

class VacancyTagInline(admin.TabularInline):
  model = VacancyTag
  extra = 2

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
  inlines = [VacancyTagInline]

class CuisineRegimeInline(admin.TabularInline):
  model = CuisineRegime
  extra = 5

@admin.register(Cuisine)
class CuisineAdmin(SingletonModelAdmin):
  inlines = [CuisineRegimeInline]

@admin.register(MainPage)
class MainPageAdmin(SingletonModelAdmin):
  pass

@admin.register(HistoryOfSchool)
class HistoryOfSchoolAdmin(SingletonModelAdmin):
  pass

@admin.register(Contact)
class ContactAdmin(SingletonModelAdmin):
  pass

@admin.register(SchoolInformationHelpMini)
class SchoolInformationHelpMiniAdmin(SingletonModelAdmin):
  pass

class SchoolInformationMainItemInline(admin.TabularInline):
  model = SchoolInformationMainItem
  extra = 4

@admin.register(SchoolInformationMain)
class SchoolInformationMainAdmin(SingletonModelAdmin):
  inlines = [SchoolInformationMainItemInline]

class SchoolInformationHelpItemInline(admin.TabularInline):
  model = SchoolInformationHelpItem
  extra = 4

@admin.register(SchoolInformationHelp)
class SchoolInformationHelpAdmin(SingletonModelAdmin):
  inlines = [SchoolInformationHelpItemInline]

@admin.register(SchoolInformationPage)
class SchoolInformationPageAdmin(admin.ModelAdmin):
  readonly_fields = ['public_link']

  def public_link(self, obj):
    if obj.pk:
      return format_html('<a href="{}" target="_blank">Перейти на страницу</a>', obj.get_absolute_url())
    return "Сохраните объект, чтобы получить ссылку"

  public_link.short_description = "Публичная страница"

  def response_add(self, request, obj, post_url_continue=None):
    response = super().response_add(request, obj, post_url_continue)
    messages.add_message(
      request,
      messages.INFO,
      format_html('Страница создана: <a href="{}" target="_blank">{}</a>', obj.get_absolute_url(), obj)
    )
    return response