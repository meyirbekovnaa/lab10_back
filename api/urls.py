from django.urls import path

# from api.views import company_list, company_detail, company_detail, vacancy_list, vacancy_detail, company_vacancies

from api.views.views_cbv import CompanyListAPIView, CompanyDetailAPIView, CompanyWithVacancyListAPIView, VacancyListAPIView, VacancyDetailAPIView
# from api.views.views_cbv import CompanyWithVacancyListAPIView
# from api.views.views_generic import CompanyListAPIView, CompanyDetailAPIView, \
#     VacancyListAPIView, VacancyDetailAPIView

from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>', CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyWithVacancyListAPIView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyDetailAPIView.as_view()),
    path('login/', obtain_jwt_token),

    # path('companies/', company_list),
    # path('companies/<int:company_id>', company_detail),
    # path('companies/<int:company_id>/vacancies/', company_vacancies),
    # path('vacancies/', vacancy_list),
    # path('vacancies/<int:vacancy_id>', vacancy_detail),

]