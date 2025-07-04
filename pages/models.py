import re
from django.db import models
from django.urls import reverse
from django.utils import timezone
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
from .utils import int_to_roman, parse_description

class Category(models.Model):
  name = models.CharField("Название", max_length=150)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = "Категория новости"
    verbose_name_plural = "Категории новостей"

class AchievmentCategory(models.Model):
  name = models.CharField("Название", max_length=150)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = "Категория достижения"
    verbose_name_plural = "Категории достижений"

class GalleryCategory(models.Model):
  name = models.CharField("Название", max_length=150)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = "Категория галереи"
    verbose_name_plural = "Категории галереи"

class Gallery(models.Model):
  title = models.CharField("Заголовок", max_length=200)
  created_at = models.DateField(default=timezone.now)
  category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, null=True, blank=True)
  
  def __str__(self):
    return self.title

  def short_title(self):
    return self.title if len(self.title) <= 26 else self.title[:26] + "..."

  def first_image_url(self):
    first_item = self.galleryitem_set.first()
    if first_item and first_item.image:
        return first_item.image.url
    return None
  
  class Meta:
    verbose_name = "Галерея"
    verbose_name_plural = "Галереи"

class GalleryItem(models.Model):
  gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
  image = models.ImageField(upload_to="gallery/")

  def __str__(self):
    return self.image.name
  
  class Meta:
    verbose_name = "Фото в галерее"
    verbose_name_plural = "Фото в галереях"

class Achievment(models.Model):
  category = models.ForeignKey(AchievmentCategory, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField("Заголовок", max_length=300)
  created_at = models.DateField(default=timezone.now)
  short_title = models.CharField("Короткий заголовок", max_length=150)
  description = models.TextField("Полное описание", max_length=12000)
  short_description = models.TextField("Краткое описание", max_length=1200)
  image = models.ImageField("Изображение", upload_to='article_images/')

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = "Достижение"
    verbose_name_plural = "Достижения"

class Article(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
  is_on_feed = models.BooleanField("Отображать на главной странице?", default=False)
  title = models.CharField("Заголовок", max_length=300)
  created_at = models.DateField(default=timezone.now)
  short_title = models.CharField("Короткий заголовок", max_length=150, default="...")
  description = models.TextField("Полное описание", max_length=12000)
  short_description = models.TextField("Краткое описание", max_length=1200)
  image = models.ImageField("Изображение", upload_to='article_images/')

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = "Новость"
    verbose_name_plural = "Новости"

class AdministrativeControl(models.Model):
  title = models.CharField("Заголовок", max_length=200)
  description = models.TextField("Описание", max_length=12000)

  def __str__(self):
    return self.title
  
  def get_short_description(self):
    return self.description[:227] + "..." if len(self.description) > 229 else self.description
  
  def get_roman_id(self):
    return int_to_roman(self.id)
  
  class Meta:
    verbose_name = "Орган управления"
    verbose_name_plural = "Органы управления"

class AdministrativeControlLink(models.Model):
  control = models.ForeignKey(
    AdministrativeControl,
    on_delete=models.CASCADE,
    related_name='links',
    verbose_name='Орган управления'
  )
  name = models.CharField("Название ссылки", max_length=255)
  url = models.URLField("URL ссылки")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Ссылка органа управления"
    verbose_name_plural = "Ссылки органа управления"

class AdditionalOrganization(models.Model):
  title = models.CharField("Заголовок", max_length=200)
  description = models.TextField("Описание", max_length=12000)

  def __str__(self):
    return self.title
  
  def get_roman_id(self):
    return int_to_roman(self.id)
  
  def save(self, *args, **kwargs):
    self.description = parse_description(self.description)
    super().save(*args, **kwargs)
  
  class Meta:
    verbose_name = "Сведения об образовательной организации"
    verbose_name_plural = "Сведения об образовательной организации"

class SocialPsychologyService(SingletonModel):
  title = models.CharField("Заголовок", max_length=200)
  description = models.TextField("Описание", max_length=12000)

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = "Социально-психологическая служба"
    verbose_name_plural = "Социально-психологическая служба"

class SocialPsychologyServiceLink(models.Model):
  control = models.ForeignKey(
    SocialPsychologyService,
    on_delete=models.CASCADE,
    related_name='links',
    verbose_name='Социально-психологическая служба'
  )
  name = models.CharField("Название ссылки", max_length=255)
  url = models.URLField("URL ссылки")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Ссылка cоциально-психологической служба"
    verbose_name_plural = "Ссылки cоциально-психологической службы"

class AdditionalEducation(SingletonModel):
  title = models.CharField("Заголовок", max_length=200)
  description = models.TextField("Описание", max_length=12000)

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = "Дополнительное образование"
    verbose_name_plural = "Дополнительное образование"

class AdditionalEducationLink(models.Model):
  control = models.ForeignKey(
    AdditionalEducation,
    on_delete=models.CASCADE,
    related_name='links',
    verbose_name='Дополнительное образование'
  )
  name = models.CharField("Название ссылки", max_length=255)
  url = models.URLField("URL ссылки")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Ссылка для дополнительного образования"
    verbose_name_plural = "Ссылки для дополнительного образования"

class Contact(SingletonModel):
  email = models.CharField("Электронная почта", max_length=100)
  phone = models.CharField("Телефон", max_length=100)
  address = models.CharField("Адрес", max_length=100)
  vk_link = models.CharField("Ссылка на VK", max_length=100)

  def __str__(self):
    return f"{self.email} / {self.phone}"
  
  class Meta:
    verbose_name = "Контакты"
    verbose_name_plural = "Контакты"

class MainPage(SingletonModel):
  hero_title = models.CharField("Заголовок на баннере", max_length=100)

  joining_step_1_title = models.CharField("Шаг 1 — заголовок", max_length=100)
  joining_step_1_description = models.CharField("Шаг 1 — описание", max_length=100)

  joining_step_2_title = models.CharField("Шаг 2 — заголовок", max_length=100)
  joining_step_2_description = models.CharField("Шаг 2 — описание", max_length=100)

  joining_step_3_title = models.CharField("Шаг 3 — заголовок", max_length=100)
  joining_step_3_description = models.CharField("Шаг 3 — описание", max_length=100)

  joining_step_4_title = models.CharField("Шаг 4 — заголовок", max_length=100)
  joining_step_4_description = models.CharField("Шаг 4 — описание", max_length=100)

  right_image = models.ImageField("Изображение справа", upload_to="main_page/right_image")

  class Meta:
    verbose_name = "Главная страница"
    verbose_name_plural = "Главная страница"

  def __str__(self):
    return "Главная страница"

class SchoolInformationMain(SingletonModel):
  image = models.ImageField("Изображение на баннере", upload_to='school_information/')
  hero_title = models.CharField("Заголовок на баннере", max_length=500, null=True, blank=True)

  class Meta:
    verbose_name = "Информация о школе: Главная"
    verbose_name_plural = "Информация о школе: Главная"

  def __str__(self):
    return "Информация о школе: Главная"
  
class SchoolInformationMainItem(models.Model):
  school_information = models.ForeignKey(SchoolInformationMain, on_delete=models.CASCADE)
  image = models.ImageField("Изображение", upload_to='school_information/', null=True, blank=True)
  subtitle = models.CharField("Надзаголовок", max_length=1000, null=True, blank=True)
  title = models.CharField("Заголовок", max_length=1000, null=True, blank=True)
  text = models.TextField("Текст", max_length=2000, null=True, blank=True)
  link_text = models.CharField("Текст ссылки", max_length=1000, null=True, blank=True)
  link_url = models.CharField("Ссылка", max_length=1000, null=True, blank=True)

  class Meta:
    verbose_name = "Элемент главной страницы"
    verbose_name_plural = "Элемент главной страницы"

  def __str__(self):
    return self.title
  
class SchoolInformationHelpMini(SingletonModel):
  image = models.ImageField("Изображение", upload_to='school_information/', null=True, blank=True)
  title = models.CharField("Заголовок", max_length=1000, null=True, blank=True)
  text = models.TextField("Текст", max_length=2000, null=True, blank=True)

  class Meta:
    verbose_name = "Помощь школе: Мини-блок"
    verbose_name_plural = "Помощь школе: Мини-блок"
  
class SchoolInformationHelp(SingletonModel):
  title = models.CharField("Заголовок", max_length=1000, null=True, blank=True)

  class Meta:
    verbose_name = "Информация о школе: Помощь от учеников"
    verbose_name_plural = "Информация о школе: Помощь от учеников"

  def __str__(self):
    return f"..."
  
class SchoolInformationHelpItem(models.Model):
  school_information = models.ForeignKey(SchoolInformationHelp, on_delete=models.CASCADE, null=True, blank=True)
  integer = models.IntegerField("Число статистики")
  subtitle = models.CharField("Текст статистики", max_length=1000, null=True, blank=True)

  class Meta:
    verbose_name = "Элемент статистики"
    verbose_name_plural = "Элемент статистики"

  def __str__(self):
    return f"..."
  
class SchoolInformationDonation(models.Model):
  title = models.CharField("Заголовок", max_length=1000)
  description = models.TextField("Текст", max_length=1000)

  class Meta:
    verbose_name = "Информация о школе: Реквизиты для поддержки"
    verbose_name_plural = "Информация о школе: Реквизиты для поддержки"

  def __str__(self):
    return self.title
  
class SchoolInformationPage(models.Model):
  page_title = models.CharField("Название страницы", max_length=1000, default="...")
  image = models.ImageField("Изображение", upload_to="school_information/", null=True, blank=True)
  title = models.CharField("Заголовок блока с изображением", max_length=1000, null=True, blank=True)
  subtitle = models.CharField("Подзаголовок блока с изображением", max_length=1000, null=True, blank=True)
  should_add_support = models.BooleanField('Добавить блок "Поддержка школы"', default=False)
  custom_breadcrumbs = models.CharField('Указать "хлебные крошки"', null=True, blank=True)
  content = models.TextField("Текст", max_length=50000)

  def get_absolute_url(self):
    return reverse("page_school_information_detail", args=[self.id])
  
  def get_roman_id(self):
    return int_to_roman(self.id)

  def save(self, *args, **kwargs):
    self.content = parse_description(self.content)
    super().save(*args, **kwargs)

  class Meta:
    verbose_name = "Информация о школе: Дополнительные страницы"
    verbose_name_plural = "Информация о школе: Дополнительные страницы"

  def __str__(self):
    return self.page_title

class HistoryOfSchool(SingletonModel):
  image = models.ImageField("Изображение", upload_to="school_information/")
  title = models.CharField("Заголовок", max_length=1000)
  subtitle = models.CharField("Подзаголовок", max_length=1000)
  content = models.TextField("Текст", max_length=50000)

  def save(self, *args, **kwargs):
    self.content = parse_description(self.content)
    super().save(*args, **kwargs)

  class Meta:
    verbose_name = "Информация о школе: История Казанской церкви"
    verbose_name_plural = "Информация о школе: История Казанской церкви"

  def __str__(self):
    return self.title

class WebsiteImage(models.Model):
  name = models.CharField("Название изображения", max_length=1000)
  image = models.ImageField("Изображение", upload_to="all_images/")

  class Meta:
    verbose_name = "Загрузка изображения"
    verbose_name_plural = "Загрузка изображений"

  def __str__(self):
    return self.name
  
class AppendAlgoritm(SingletonModel):
  image = models.ImageField("Изображение", upload_to="school_information/")
  title = models.CharField("Заголовок", max_length=1000)

  class Meta:
    verbose_name = "Алгоритм поступления"
    verbose_name_plural = "Алгоритм поступления"

  def __str__(self):
    return self.title
  
class AppendAlgoritmStep(models.Model):
  algoritm = models.ForeignKey(
    AppendAlgoritm,
    on_delete=models.CASCADE,
    related_name='steps',
    verbose_name='Шаги'
  )
  title = models.CharField("Заголовок", max_length=1000)
  text = models.CharField("Текст", max_length=1000, null=True, blank=True)

  class Meta:
    verbose_name = "Шаг алгоритма поступления"
    verbose_name_plural = "Шаги алгоритма поступления"

  def __str__(self):
    return self.title
  
class Cuisine(SingletonModel):
  image = models.ImageField("Изображение", upload_to="school_information/")
  title = models.CharField("Заголовок", max_length=1000)
  subtitle = models.CharField("Подзаголовок", max_length=1000)
  content = models.TextField("Текст", max_length=50000)

  class Meta:
    verbose_name = "Питание"
    verbose_name_plural = "Питания"

  def __str__(self):
    return self.title
  
class CuisineRegime(models.Model):
  cuisine = models.ForeignKey(
    Cuisine,
    on_delete=models.CASCADE,
    related_name='regime',
    verbose_name='Режим питания'
  )
  time = models.TimeField("Время")
  text = models.CharField("Заголовок", max_length=1000)

  class Meta:
    verbose_name = "Режим питания"
    verbose_name_plural = "Режим питания"

  def __str__(self):
    return f"{self.time} - {self.text}"

class Document(models.Model):
  title = models.CharField("Заголовок", max_length=200)
  description = models.TextField("Описание", max_length=12000)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    self.description = parse_description(self.description)
    super().save(*args, **kwargs)
  
  def get_short_description(self):
    return self.description[:227] + "..." if len(self.description) > 229 else self.description
  
  def get_roman_id(self):
    return int_to_roman(self.id)
  
  class Meta:
    verbose_name = "Документ"
    verbose_name_plural = "Документы"

class DocumentLink(models.Model):
  document = models.ForeignKey(
    Document,
    on_delete=models.CASCADE,
    related_name='links',
    verbose_name='Ссылка на документ'
  )
  name = models.CharField("Название ссылки", max_length=255)
  url = models.URLField("URL ссылки")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Ссылка документа"
    verbose_name_plural = "Ссылки документов"

class Vacancy(models.Model):
  title = models.CharField("Название", max_length=200)
  url = models.URLField("URL ссылки", null=True, blank=True)

  class Meta: 
    verbose_name = "Вакансия"
    verbose_name_plural = "Вакансии"

  def __str__(self):
    return self.title

class VacancyTag(models.Model):
  vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='tags', verbose_name="Тег вакансии")
  name = models.CharField("Название", max_length=100)

  class Meta: 
    verbose_name = "Тег вакансии"
    verbose_name_plural = "Теги вакансий"

  def __str__(self):
    return self.name

class BellSchedule(models.Model):
  time_start = models.TimeField("Начало")
  time_end = models.TimeField("Конец")
  text = models.CharField("Описание", max_length=300)
  is_red = models.BooleanField("Сделать описание красного цвета?", default=False  )
  break_after = models.PositiveIntegerField("Будет ли перемена? Если да, то укажите ее продолжительность", null=True, blank=True)
  duration = models.PositiveIntegerField("Продолжительность(опционально)", null=True, blank=True)

  class Meta: 
    verbose_name = "Расписание звонков"
    verbose_name_plural = "Расписание звонков"

  def __str__(self):
    return f"{self.time_start} - {self.time_end} ({self.text})"

class BusSchedule(models.Model):
  title = models.CharField("Название маршрута", max_length=2000)
  image = models.ImageField("Изображение с картой", upload_to="maps/", null=True, blank=True)

  class Meta: 
    verbose_name = "Расписание автобусов"
    verbose_name_plural = "Расписание автобусов"

  def __str__(self):
    return f"{self.title}"
  
class BusScheduleTime(models.Model):
  schedule = models.ForeignKey(BusSchedule, on_delete=models.CASCADE, related_name="times")
  time = models.TimeField("Время", null=True, blank=True)
  text = models.CharField("Описание", max_length=300, null=True, blank=True)

  class Meta: 
    verbose_name = "Время расписания автобусов"
    verbose_name_plural = "Время расписания автобусов"

  def __str__(self):
    return f"{self.time} - {self.text}"
  
class Attestation(SingletonModel):
  image = models.ImageField("Изображение", upload_to="attestation/", null=True, blank=True)
  title = models.CharField("Заголовок", max_length=2000)
  description = models.TextField("Описание", max_length=12000)

  def save(self, *args, **kwargs):
    self.description = parse_description(self.description)
    super().save(*args, **kwargs)

  class Meta: 
    verbose_name = "Государственная итоговая аттестация"
    verbose_name_plural = "Государственная итоговая аттестация"

  def __str__(self):
    return f"Государственная итоговая аттестация"

class AttestationItem(models.Model):
  attestation = models.ForeignKey(Attestation, on_delete=models.CASCADE, related_name="links")
  name = models.TextField("Название", max_length=2000)
  url = models.CharField("Ссылка", null=True, blank=True)

  class Meta: 
    verbose_name = "Ссылка на странице"
    verbose_name_plural = "Ссылки на странице"

  def __str__(self):
    return f"{self.name}"

class GenericPageCategory(models.Model):
  name = models.CharField("Название", max_length=1000)
  link = models.CharField("Ссылка на страницу", max_length=1000, null=True, blank=True)

  class Meta: 
    verbose_name = "Категория в навигации"
    verbose_name_plural = "Категории в навигации"

  def __str__(self):
    return f"{self.name}"

class GenericPageA(models.Model):
  show_in_nav = models.BooleanField("Показать страницу в навигации?", default=False)
  category = models.ForeignKey(GenericPageCategory, verbose_name="Категория", on_delete=models.CASCADE, related_name="pages_a", null=True, blank=True)
  path = models.CharField("Путь к странице", max_length=800, null=True, blank=True)
  page_title = models.CharField("Название страницы", max_length=2000)
  
  def get_absolute_url(self):
    return reverse("page_type_a", args=[self.id])

  class Meta: 
    verbose_name = "Страница типа 'А'"
    verbose_name_plural = "Страницы типа 'А'"

  def __str__(self):
    return f"{self.category if self.category else "-"} | {self.page_title}"

class GenericPageA_Paragraph(models.Model):
  page = models.ForeignKey(GenericPageA, on_delete=models.CASCADE, related_name="paragraphs")
  title = models.CharField("Заголовок", max_length=2000)
  description = models.TextField("Описание", max_length=20000)

  def save(self, *args, **kwargs):
    self.description = parse_description(self.description)
    super().save(*args, **kwargs)

  class Meta: 
    verbose_name = "Абзац"
    verbose_name_plural = "Абзацы"

  def __str__(self):
    return f"{self.title}"
  
class GenericPageB(models.Model):
  COLOR_CHOICES = [
    ('#913232', 'Красный'),
    ('#4F5F4D', 'Зелёный'),
  ]

  show_in_nav = models.BooleanField("Показать страницу в навигации?", default=False)
  category = models.ForeignKey(GenericPageCategory, verbose_name="Категория", on_delete=models.CASCADE, related_name="pages_b", null=True, blank=True)
  path = models.CharField("Путь к странице", max_length=800, null=True, blank=True)
  page_title = models.CharField("Название страницы", max_length=2000)
  description = models.TextField("Описание", max_length=20000)
  title_color = models.CharField("Цвет заголовка", max_length=7, choices=COLOR_CHOICES, default='#913232')

  def save(self, *args, **kwargs):
    self.description = parse_description(self.description)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("page_type_b", args=[self.id])

  class Meta:
    verbose_name = "Страница типа 'Б'"
    verbose_name_plural = "Страницы типа 'Б'"

  def __str__(self):
    return f"{self.category if self.category else "-"} | {self.page_title}"

class SubjectWeek(models.Model):
  name = models.CharField("Название", max_length=2000)
  color = models.CharField("Цвет предмета", max_length=30)
  description = models.TextField("Описание", max_length=20000)

  def save(self, *args, **kwargs):
    self.description = parse_description(self.description)
    super().save(*args, **kwargs)

  class Meta: 
    verbose_name = "Предметная неделя"
    verbose_name_plural = "Предметные недели"

  def __str__(self):
    return f"{self.name}"
  
class Tag(models.Model):
  name = models.CharField("Название", max_length=1000, unique=True)

  def __str__(self):
    return self.name
  
  class Meta: 
    verbose_name = "Тег учителя"
    verbose_name_plural = "Теги учителей"

class TeacherCategory(models.Model):
  name = models.CharField("Название", max_length=1000, unique=True)

  def __str__(self):
    return self.name
  
  class Meta: 
    verbose_name = "Категория учителя"
    verbose_name_plural = "Категории учителей"

class Teacher(models.Model):
  image = models.ImageField("Фото", upload_to="teachers/", null=True, blank=True)
  full_name = models.CharField("ФИО", max_length=255)
  category = models.ForeignKey(TeacherCategory, verbose_name="Категория", related_name='categories', on_delete=models.CASCADE, null=True, blank=True)
  tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name='teachers')
  education = models.CharField("Образование", max_length=1000)
  direction = models.CharField("Направление подготовки ", max_length=1000)
  degree = models.CharField("Ученая степень ", max_length=1000)
  experience = models.CharField("Стаж работы ", max_length=1000)

  def __str__(self):
    return self.full_name
  
  class Meta: 
    verbose_name = "Учитель"
    verbose_name_plural = "Учителя"

class Grade(models.Model):
  title = models.CharField("Название", max_length=2000)

  def __str__(self):
    return self.title
  
  class Meta: 
    verbose_name = "Свободные места: Школа"
    verbose_name_plural = "Свободные места: Школы"

class GradeNumber(models.Model):
  grade = models.ForeignKey(Grade, verbose_name="Школа", on_delete=models.CASCADE, related_name="schools")
  number = models.PositiveIntegerField("Номер класса")

  def __str__(self):
    return f"{self.number} класс"
  
  class Meta: 
    verbose_name = "Свободные места: Класс"
    verbose_name_plural = "Свободные места: Классы"

class GradeFullness(models.Model):
  grade_number = models.ForeignKey(GradeNumber, verbose_name="Класс", on_delete=models.CASCADE, related_name="classes")
  parallel = models.CharField("Параллель", max_length=100)
  is_full = models.BooleanField("Есть ли свободные места?", default=False)
  teacher = models.ForeignKey(Teacher, verbose_name="Учитель", on_delete=models.CASCADE, related_name="teachers")

  def __str__(self):
    return f"{self.grade_number} - {"Нет свободных мест" if self.is_full else "Есть свободные места"}"
  
  class Meta: 
    verbose_name = "Свободные места"
    verbose_name_plural = "Свободные места"