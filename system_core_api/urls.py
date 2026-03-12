from django.urls import path
from . import views


urlpatterns = [

    # API Endpoints for Auth-System

    path('login/', views.LoginAPIView.as_view(), name='login_api'),
    path('logout/', views.LogoutAPIView.as_view(), name="user_logout_api"),
    # path('register/', views.RegisterAPIView.as_view(), name='register_api'),
    path('password_reset/', views.PasswordResetRequestAPIView.as_view(), name='password_reset'),
    path('password_reset_confirm/', views.PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),


    path('users/', views.AllUsersAPIView.as_view(), name="all_users_api"),
    path('user/<int:pk>/', views.UserAPIView.as_view(), name="user_api"),
    path('user/add/', views.AddUserAPIView.as_view(), name="add_user_api"),
    path('user/update/<int:pk>/', views.UpdateUserAPIView.as_view(), name="update_user_api"),
    path('user/delete/<int:pk>/', views.DeleteUserAPIView.as_view(), name="delete_user_api"),

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

    path('student-courses/', views.AllStudentCoursesAPIView.as_view(), name="all_student_courses_api"),
    path('student-course/<int:pk>/', views.StudentCourseAPIView.as_view(), name="student_course_api"),
    path('student-course/add/', views.AddStudentCourseAPIView.as_view(), name="add_student_course_api"),
    path('student-course/update/<int:pk>/', views.UpdateStudentCourseAPIView.as_view(), name="update_student_course_api"),
    path('student-course/delete/<int:pk>/', views.DeleteStudentCourseAPIView.as_view(), name="delete_student_course_api"),


    path('center-books/', views.AllCenterBooksAPIView.as_view(), name="all_center_books_api"),
    path('center-book/<int:pk>/', views.CenterBookAPIView.as_view(), name="center_book_api"),
    path('center-book/add/', views.AddCenterBookAPIView.as_view(), name="add_center_book_api"),
    path('center-book/update/<int:pk>/', views.UpdateCenterBookAPIView.as_view(), name="update_center_book_api"),
    path('center-book/delete/<int:pk>/', views.DeleteCenterBookAPIView.as_view(), name="delete_center_book_api"),


    path('received-books/', views.AllReceivedBooksAPIView.as_view(), name="all_received_books_api"),
    path('received-book/<int:pk>/', views.ReceivedBookAPIView.as_view(), name="received_book_api"),
    path('received-book/add/', views.AddReceivedBookAPIView.as_view(), name="add_received_book_api"),
    path('received-book/update/<int:pk>/', views.UpdateReceivedBookAPIView.as_view(), name="update_received_book_api"),
    path('received-book/delete/<int:pk>/', views.DeleteReceivedBookAPIView.as_view(), name="delete_received_book_api"),

    path('book-reservations/', views.BookReservationListAPIView.as_view(), name="book_reservation_list_api"),
    path('book-reservation/<int:pk>/', views.BookReservationDetailAPIView.as_view(), name="book_reservation_detail_api"),
    path('book-reservation/add/', views.BookReservationCreateAPIView.as_view(), name="book_reservation_add_api"),
    path('book-reservation/update/<int:pk>/', views.BookReservationUpdateAPIView.as_view(), name="book_reservation_update_api"),
    path('book-reservation/delete/<int:pk>/', views.BookReservationDeleteAPIView.as_view(), name="book_reservation_delete_api"),


    path('districts/', views.DistrictListAPIView.as_view(), name="district_list_api"),
    path('district/<int:pk>/', views.DistrictDetailAPIView.as_view(), name="district_detail_api"),
    path('district/add/', views.DistrictCreateAPIView.as_view(), name="district_add_api"),
    path('district/update/<int:pk>/', views.DistrictUpdateAPIView.as_view(), name="district_update_api"),
    path('district/delete/<int:pk>/', views.DistrictDeleteAPIView.as_view(), name="district_delete_api"),




    # path("scan-qr/", views.ScanQRAPIView.as_view(), name="scan-qr"), # only use for Image type/file
    path('scan-qr/', views.ScanQRTXTAPIView.as_view(), name="scan_qr"),


    path("issue-book/", views.IssueBookAPIView.as_view(), name="issue_book"),
    path("student-book-reservation/<uuid:uuid>/", views.MakeBookReservationAPIView.as_view(), name="make_book_reservation"),
    path("view-center-allocation/<uuid:uuid>/", views.ViewCenterAllocationAPIView.as_view(), name="view_center_allocation"),

    path("dashboard/", views.DashboardAPIView.as_view(), name="dashboard"),

    path("create-staff/", views.CreateStaffAPIView.as_view(), name="create_staff"),
    path('test/', views.TestAPI.as_view(), name="testapi")
]
