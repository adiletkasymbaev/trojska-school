# myapp/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import (
    Article, Achievment, Gallery, Document,
    GenericPageA, GenericPageB, SchoolInformationPage
)

# Статические страницы
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        return [
            'page_main', 'page_news', 'page_available_spots', 
            'page_teachers', 'page_achievments', 'page_append', 
            'page_cuisine', 'page_help_school', 'page_vacancy', 
            'page_attestation', 'page_schedule', 'page_schedule_bus',
            'page_subjects', 'page_social_psychology', 'page_additional_education',
            'page_additional_organization', 'page_school_information_main',
            'page_school_information_history', 'page_contacts',
            'page_administrative_control', 'page_documents', 'page_gallery'
        ]

    def location(self, item):
        return reverse(item)

# Новости
class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Article.objects.all()

    def location(self, obj):
        return reverse('page_news_detail', args=[obj.id])

# Достижения
class AchievmentSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Achievment.objects.all()

    def location(self, obj):
        return reverse('page_achievments_detail', args=[obj.id])

# Галереи
class GallerySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Gallery.objects.all()

    def location(self, obj):
        return reverse('page_gallery_detail', args=[obj.id])

# Документы
class DocumentSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Document.objects.all()

    def location(self, obj):
        return reverse('page_documents_detail', args=[obj.id])

# Generic Page A
class GenericPageASitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return GenericPageA.objects.all()

    def location(self, obj):
        return reverse('page_type_a', args=[obj.id])

# Generic Page B
class GenericPageBSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return GenericPageB.objects.all()

    def location(self, obj):
        return reverse('page_type_b', args=[obj.id])

# Школьные страницы
class SchoolInformationPageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return SchoolInformationPage.objects.all()

    def location(self, obj):
        return reverse('page_school_information_detail', args=[obj.id])