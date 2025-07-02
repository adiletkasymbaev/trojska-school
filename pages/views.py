from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *

def main_page(request):
  contacts = Contact.objects.all()[0]
  articles = Article.objects.all().filter(is_on_feed=True)
  main_page_info = MainPage.objects.all()[0]
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'contacts': contacts,
      'articles': articles,
      'main_page_info': main_page_info,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'index.html', context)

def news_page(request):
  if request.method == "GET":
      contacts = Contact.objects.all()[0]
      articles = Article.objects.all()
      category = Category.objects.all()
      main_page_info = MainPage.objects.all()[0]
      page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
      page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

      param_category = request.GET.get("category")

      if param_category:
          articles = articles.filter(category=param_category)

      context = {
          'contacts': contacts,
          'category': category,
          'articles': articles,
          'main_page_info': main_page_info,
          'page_for_nav_a': page_for_nav_a,
          'page_for_nav_b': page_for_nav_b,
      }

      return render(request, 'news.html', context)
  else:
      return HttpResponse("Ошибка!")

def achievments_page(request):
  if request.method == "GET":
      contacts = Contact.objects.all()[0]
      achievments = Achievment.objects.all()
      category = AchievmentCategory.objects.all()
      main_page_info = MainPage.objects.all()[0]
      page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
      page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

      param_category = request.GET.get("category")

      if param_category:
          achievments = achievments.filter(category=param_category)

      context = {
          'contacts': contacts,
          'category': category,
          'achievments': achievments,
          'main_page_info': main_page_info,
          'page_for_nav_a': page_for_nav_a,
          'page_for_nav_b': page_for_nav_b,
      }

      return render(request, 'achievments.html', context)
  else:
      return HttpResponse("Ошибка!")

def gallery_page(request):
  if request.method == "GET":
      contacts = Contact.objects.all()[0]
      gallery = Gallery.objects.all()
      category = GalleryCategory.objects.all()
      main_page_info = MainPage.objects.all()[0]
      page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
      page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

      param_category = request.GET.get("category")

      if param_category:
          gallery = gallery.filter(category=param_category)

      context = {
          'contacts': contacts,
          'category': category,
          'gallery': gallery,
          'main_page_info': main_page_info,
          'page_for_nav_a': page_for_nav_a,
          'page_for_nav_b': page_for_nav_b,
      }

      return render(request, 'gallery.html', context)
  else:
      return HttpResponse("Ошибка!")

def gallery_detail_page(request, id):
  contacts = Contact.objects.all()[0]
  gallery = get_object_or_404(Gallery, id=id)
  gallery_images = GalleryItem.objects.filter(gallery=gallery)
  main_page_info = MainPage.objects.all()[0]
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'contacts': contacts,
      'gallery': gallery,
      'gallery_images': gallery_images,
      'main_page_info': main_page_info,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'gallery_detail.html', context)

def administrative_control_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  administrative_controls = AdministrativeControl.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'administrative_controls': administrative_controls,
      'contacts': contacts,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'administrative_control.html', context)

def administrative_control_detail_page(request, id):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  administrative_control = get_object_or_404(AdministrativeControl, id=id)
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'data': administrative_control,
      'parent': {'title': 'Органы управления', 'link': 'page_administrative_control', 'is_parent': False},
      'contacts': contacts,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'generic_detail.html', context)

def social_psychology_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  data = SocialPsychologyService.objects.all()[0]
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'data': data,
      'parent': {'title': 'Социально-психологическая служба', 'is_parent': True},
      'contacts': contacts,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'generic_detail.html', context)

def additional_education_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  data = AdditionalEducation.objects.all()[0]
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'data': data,
      'parent': {'title': 'Дополнительное образование', 'is_parent': True},
      'contacts': contacts,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'generic_detail.html', context)

def additional_organization_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  paragraphs = AdditionalOrganization.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'paragraphs': paragraphs,
      'contacts': contacts,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'educational_organization.html', context)

def contacts_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'contacts.html', context)

def school_information_main(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_info = SchoolInformationMain.objects.all()[0]
  current_page_help_mini = SchoolInformationHelpMini.objects.all()[0]
  current_page_help = SchoolInformationHelp.objects.all()[0]
  current_page_donation = SchoolInformationDonation.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'current_page_help': current_page_help,
      'current_page_donation': current_page_donation,
      'current_page_help_mini': current_page_help_mini,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'about_school_main.html', context)

def school_information_detail(request, id):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_info = SchoolInformationPage.objects.get(id=id)
  current_page_help = SchoolInformationHelp.objects.all()[0]
  current_page_donation = SchoolInformationDonation.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'current_page_help': current_page_help,
      'current_page_donation': current_page_donation,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'about_school_generic.html', context)

def school_information_history_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_info = HistoryOfSchool.objects.all()[0]
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'about_school_history_of_school.html', context)

def append_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_info = AppendAlgoritm.objects.all()[0]
  steps = AppendAlgoritmStep.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'steps': steps,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'append.html', context)

def help_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_help_mini = SchoolInformationHelpMini.objects.all()[0]
  current_page_help = SchoolInformationHelp.objects.all()[0]
  current_page_donation = SchoolInformationDonation.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_help_mini': current_page_help_mini,
      'current_page_help': current_page_help,
      'current_page_donation': current_page_donation,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'help_school.html', context)

def cuisine_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_info = Cuisine.objects.all()[0]
  regime = CuisineRegime.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'regime': regime,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'cuisine.html', context)

def documents_page(request):
  main_page_info = MainPage.objects.all()[0]
  administrative_controls = Document.objects.all()
  contacts = Contact.objects.all()[0]
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts, 
      'administrative_controls': administrative_controls,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'documents.html', context)

def documents_detail_page(request, id):
  main_page_info = MainPage.objects.all()[0]
  administrative_control = get_object_or_404(Document, id=id)
  contacts = Contact.objects.all()[0]
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts, 
      'data': administrative_control,
      'parent': {'title': 'Документы', 'link': 'page_documents', 'is_parent': False},
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'documents_detail.html', context)

def vacancy_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  vacancies = Vacancy.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'vacancies': vacancies,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'vacancy.html', context)

def schedule_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  schedules = BellSchedule.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'schedules': schedules,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'bell_schedule.html', context)

def schedule_bus_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  schedules = BusSchedule.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'schedules': schedules,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'bus_timetable.html', context)

def attestation_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_info = Attestation.objects.all()[0]
  links = AttestationItem.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'links': links,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'attestation.html', context)

def subjects_page(request):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  subjects = SubjectWeek.objects.all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'subjects': subjects,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'subject_weeks.html', context)

def subjects_detail_page(request, id):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  subject = SubjectWeek.objects.get(id=id)
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'subject': subject,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'subject_weeks_detail.html', context)

def type_a_page(request, id):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_info = GenericPageA.objects.get(id=id)
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'customs/type_a_page.html', context)

def type_b_page(request, id):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  current_page_info = GenericPageB.objects.get(id=id)
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'customs/type_b_page.html', context)

def teachers_page(request):
  main_page_info = MainPage.objects.first()
  contacts = Contact.objects.first()
  categories = TeacherCategory.objects.all()
  tags = Tag.objects.all().exclude(name="Директор")
  teachers_by_tag = None
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  tag_name = request.GET.get('tag')
  if tag_name:
      teachers_by_tag = Teacher.objects.filter(tags__name=tag_name).distinct()
      print(teachers_by_tag)
  
  teachers = Teacher.objects.all()

  categories_with_teachers = []
  for category in categories:
      teacher_list = teachers.filter(category=category)
      if teacher_list.exists():
          categories_with_teachers.append((category, teacher_list))

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'categories': categories,
      'tags': tags,
      'categories_with_teachers': categories_with_teachers,
      'selected_tag': tag_name,
      'teachers_by_tag': teachers_by_tag,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'faculty.html', context)

def teachers_detail_page(request, id):
  main_page_info = MainPage.objects.all()[0]
  contacts = Contact.objects.all()[0]
  teacher = Teacher.objects.get(id=id)
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'teacher': teacher,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'teaching_staff.html', context)

def available_spots_page(request):
  main_page_info = MainPage.objects.first()
  contacts = Contact.objects.first()
  schools = Grade.objects.prefetch_related(
      'schools__classes__teacher'
  ).all()
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'schools': schools,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }
  
  return render(request, 'available_spots.html', context)

def news_detail_page(request, id):
  main_page_info = MainPage.objects.first()
  contacts = Contact.objects.first()
  current_page_info = Article.objects.get(id=id)
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'news_detail.html', context)

def achievments_detail_page(request, id):
  main_page_info = MainPage.objects.first()
  contacts = Contact.objects.first()
  current_page_info = Achievment.objects.get(id=id)
  page_for_nav_a = GenericPageA.objects.all().filter(show_in_nav=True)
  page_for_nav_b = GenericPageB.objects.all().filter(show_in_nav=True)

  context = {
      'main_page_info': main_page_info,
      'contacts': contacts,
      'current_page_info': current_page_info,
      'page_for_nav_a': page_for_nav_a,
      'page_for_nav_b': page_for_nav_b,
  }

  return render(request, 'news_detail.html', context)