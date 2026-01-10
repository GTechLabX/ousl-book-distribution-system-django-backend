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


    path('degree-programs/', views.AllDegreeProgramsAPIView.as_view(), name="all_degree_programs_api"),
    path('degree-program/<int:pk>/', views.DegreeProgramAPIView.as_view(), name="degree_program_api"),
    path('degree-program/add/', views.AddDegreeProgramAPIView.as_view(), name="add_degree_program_api"),
    path('degree-program/update/<int:pk>/', views.UpdateDegreeProgramAPIView.as_view(), name="update_degree_program_api"),
    path('degree-program/delete/<int:pk>/', views.DeleteDegreeProgramAPIView.as_view(), name="delete_degree_program_api"),


    path('courses/', views.AllCoursesAPIView.as_view(), name="all_courses_api"),
    path('course/<int:pk>/', views.CourseAPIView.as_view(), name="course_api"),
    path('course/add/', views.AddCourseAPIView.as_view(), name="add_course_api"),
    path('course/update/<int:pk>/', views.UpdateCourseAPIView.as_view(), name="update_course_api"),
    path('course/delete/<int:pk>/', views.DeleteCourseAPIView.as_view(), name="delete_course_api"),


    path('books/', views.AllBooksAPIView.as_view(), name="all_books_api"),
    path('book/<int:pk>/', views.BookAPIView.as_view(), name="book_api"),
    path('book/add/', views.AddBookAPIView.as_view(), name="add_book_api"),
    path('book/update/<int:pk>/', views.UpdateBookAPIView.as_view(), name="update_book_api"),
    path('book/delete/<int:pk>/', views.DeleteBookAPIView.as_view(), name="delete_book_api"),

    path('centers/', views.AllCentersAPIView.as_view(), name="all_centers_api"),
    path('center/<int:pk>/', views.CenterAPIView.as_view(), name="center_api"),
    path('center/add/', views.AddCenterAPIView.as_view(), name="add_center_api"),
    path('center/update/<int:pk>/', views.UpdateCenterAPIView.as_view(), name="update_center_api"),
    path('center/delete/<int:pk>/', views.DeleteCenterAPIView.as_view(), name="delete_center_api"),


    path('degree-program-courses/', views.AllDegreeProgramCoursesAPIView.as_view(), name="all_degree_program_courses_api"),
    path('degree-program-course/<int:pk>/', views.DegreeProgramCourseAPIView.as_view(), name="degree_program_course_api"),
    path('degree-program-course/add/', views.AddDegreeProgramCourseAPIView.as_view(), name="add_degree_program_course_api"),
    path('degree-program-course/update/<int:pk>/', views.UpdateDegreeProgramCourseAPIView.as_view(), name="update_degree_program_course_api"),
    path('degree-program-course/delete/<int:pk>/', views.DeleteDegreeProgramCourseAPIView.as_view(), name="delete_degree_program_course_api"),



    path('test/', views.TestAPI.as_view(), name="testapi")
]
