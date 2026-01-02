from django.urls import path
from . import views

urlpatterns = [

    # API Endpoints for Auth-System

    path('login/', views.LoginAPIView.as_view(), name='login_api'),
    path('register/', views.RegisterAPIView.as_view(), name='register_api'),
    path('password_reset/', views.PasswordResetRequestAPIView.as_view(), name='password_reset'),
    path('password_reset_confirm/', views.PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),

    # API Endpoints for Student management

    path('student/', views.AllStudentAPIView.as_view(), name='all_student_api'),
    path('student/<int:pk>/', views.StudentAPIView.as_view(), name='student_api'),
    path('student_register/', views.StudentRegAPIView.as_view(), name='student_register_api'),
    path('student/<int:pk>/update/', views.StudentUpdateAPIView.as_view(), name='student_update_api'),
    path('student/delete/<int:pk>/', views.StudentDeleteAPIView.as_view(), name='student_delete_api'),

    # API Endpoints for Faculty Management

    path('faculties/', views.AllFacultiesAPIView.as_view(), name="all_faculties_api"),
    path('faculties/<int:pk>/', views.FacultyAPIView.as_view(), name="faculty_api"),
    path('add_faculty/', views.AddFacultyAPIView.as_view(), name="add_faculty_api"),
    path('faculty/<int:pk>/update', views.UpdateFacultyAPIView.as_view(), name="update_faculty_api"),
    path('faculty/delete/<int:pk>', views.DeleteFacultyAPIView.as_view(), name="delete_faculty_api"),

    # API Endpoints for Department Management

    path('departments/', views.AllDepartmentsAPIView.as_view(), name="all_departments_api"),
    path('departments/<int:pk>/', views.DepartmentAPIView.as_view(), name="department_api"),
    path('add_department/', views.AddDepartmentAPIView.as_view(), name="add_department_api"),
    path('department/<int:pk>/update', views.UpdateDepartmentAPIView.as_view(), name="update_department_api"),
    path('department/delete/<int:pk>', views.DeleteDepartmentAPIView.as_view(), name="delete_department_api"),

    path('test/', views.TestAPI.as_view(), name="testapi")
]
