from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from prof_rater.models import Department, Professor, Review, Course, WordCloud
from django.views import generic
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your views here.


#index page will have the search input form and display results on the same page
def index(request):
    return render(request, 'prof_rater/index.html', {
        'prof_list' : get_prof_list(),
        'course_list' : get_course_list(),
        'dept_list' : get_dept_list(),
    })

#
def department(request, dept_code):
    dept = ''
    try:
        dept = get_object_or_404(Department, code=dept_code.upper()+'')
        try:
            course_list = get_course_list()
            for i in range(len(course_list)-1,-1,-1):
                if(course_list[i].subject.upper() != dept_code.upper()):
                    course_list[i].subject = 'DELETE'
                    course_list.pop(i)
            return render(request, 'prof_rater/department.html', {
                'dept': dept,
                'course_list': course_list,
            })
        except Exception as e:
            return render(request, 'prof_rater/department.html', {'message' : "This department "+dept_code+" has no course. ",})
    except Exception as e:
        return render(request, 'prof_rater/department.html', {'message' : ""+dept_code + " is not a valid department code.",})


# 
def course(request, dept_code, course_num):   
    prof_list = get_prof_list_by_course(dept_code.upper(), course_num)
    for prof in prof_list:
        prof.meta_score = calculate_metascore(prof.id)
        prof.review_set_count = len(Review.objects.filter(course_subject=dept_code)
                                                  .filter(course_number=course_num)
                                                  .filter(professor=prof))
    return render(request, 'prof_rater/course.html', {
        'h1': dept_code + str(course_num),
        'prof_list': prof_list,
    }) 


# professor's profile wil have name of prof and the reviews for him/her and his meta score
def profile(request, prof_id):
        professor = get_object_or_404(Professor, pk=prof_id)
        meta_score = calculate_metascore(prof_id)
        return render(request, 'prof_rater/profile.html', {
        'professor' : professor,
                'meta_score': meta_score,
        'word_cloud_entries': get_word_cloud_entries(prof_id),
    })

# access profile from the course page
def profile_from_course(request, dept_code, course_num, prof_id):
    #profile(request, prof_id)
        professor = get_object_or_404(Professor, pk=prof_id)
        meta_score = calculate_metascore(prof_id)
        return render(request, 'prof_rater/profile.html', {
        'professor' : professor,
        'meta_score': meta_score,
        'word_cloud_entries': get_word_cloud_entries(prof_id),
    })


# review creation page for a professor of your choice
def review(request, prof_id):
    professor = get_object_or_404(Professor, pk=prof_id)
    return render(request, 'prof_rater/review.html', {
                  'professor' : professor })

def create_review(request, prof_id):
    professor = get_object_or_404(Professor, pk=prof_id)
    
    comment = request.POST.get('comments','')
    finalScore = request.POST.get('final_score','')
    courseNumber = request.POST.get('course_number','')
    courseSubject = request.POST.get('course_subject','')
    courseInterest = request.POST.get('interest_in_course','')

    #getting wordcloud entries
    phrase1 = request.POST.get('phrase_one','')
    phrase2 = request.POST.get('phrase_two','')
    phrase3 = request.POST.get('phrase_three','')

    if len(comment) == 0:
        return render(request, 'prof_rater/profile.html', {
            'professor': professor,
            'meta_score': calculate_metascore(prof_id),
            'word_cloud_entries': get_word_cloud_entries(prof_id),
            'error_message': "You need to comment before you can rate",
        })
    else:
        professor.review_set.create(comments = comment, 
                                    final_score = finalScore,
                                    #course_taken = courseTaken, 
                                    course_number = courseNumber,
                                    course_subject = courseSubject,
                                    interest_in_course = courseInterest,
                                    date_published = timezone.now())

        professor.wordcloud_set.create(phrase_one = phrase1,
                                       phrase_two = phrase2,
                                       phrase_three = phrase3)
    
        return HttpResponseRedirect(reverse('profile', args=(professor.id,)))


# This function calcuates the metascore of a professor
def calculate_metascore(prof_id):
    professor = Professor.objects.get(pk=prof_id)
    total_score = 0
    for review in professor.review_set.all():
            total_score += review.final_score

    if(total_score <= 0):
            return "n/a"
    else:
            max_score = professor.review_set.count() * 5
            meta_score = total_score/max_score * 5
            return "%.1f" % meta_score

# This function gets first 10 random wordcloud entries for a professor
def get_word_cloud_entries(prof_id):
    professor = Professor.objects.get(pk=prof_id)
    word_cloud_entries = professor.wordcloud_set.order_by('?')[:10]
    return word_cloud_entries
    

# This function calcuates the metascore of a department
def calculate_department_metascore(_course_subject):
    review_list = Review.objects.filter(course_subject=_course_subject)
    total_score = 0
    for review in review_list:
        total_score += review.final_score
    if(total_score <= 0):
            return "n/a"
    else:
            max_score = review_list.count() * 5
            meta_score = total_score/max_score * 5
            return "%.1f" % meta_score


# This function calcuates the metascore of a course
def calculate_course_metascore(_course_subject, _course_number):
    review_list = Review.objects.filter(course_subject=_course_subject).filter(course_number=_course_number)
    total_score = 0
    for review in review_list:
        total_score += review.final_score
    if(total_score <= 0):
            return "no ratings yet"
    else:
            max_score = review_list.count() * 5
            meta_score = total_score/max_score * 5
            return "%.1f" % meta_score



# This function returns a prof_list array that contains all unique professors
# retrieved from Professor objects with metascore calculated.
def get_prof_list():
    prof_list = Professor.objects.all()
    for p in prof_list:
        p.meta_score = calculate_metascore(p.pk)
    return prof_list

# This function returns a prof_list array that contains all professors who
# have taught this specific course
def get_prof_list_by_course(subject, number):
    # get all reviews about this specific course
    review_list = Review.objects.filter(course_subject=subject).filter(course_number=number)
    prof_list = []
    for review in review_list:
        if(prof_in_prof_list(prof_list, review.professor) == False):
            prof = review.professor
            prof_list.append(prof)
    return prof_list

# this function is to check whether this prof is inside the prof_list array
# called by get_prof_list_by_course()
def prof_in_prof_list(prof_list, prof):
    for p in prof_list:
        if (p == prof):
            return True
    return False

# This function returns a dept_list array that contains all unique departments
# retrieved from Department objects with metascore calculated.
def get_dept_list():
    dept_list = Department.objects.all()
    for d in dept_list:
        d.meta_score = calculate_department_metascore(d.code)
        d.review_set_count = len(Review.objects.filter(course_subject=d.code))
    return dept_list


# This function returns a course_list array that contains all unique courses
# retrieved from Review objects with metascore calculated.
def get_course_list():
    review_list = Review.objects.all()  # returns a dictionary
    course_list = []
    for review in review_list:
        if(course_in_course_list(course_list, review.course_subject, review.course_number) == False):
            course = Course(title = find_course_title_by_subject_and_number(review.course_subject, review.course_number),
                            subject = review.course_subject,
                            number = review.course_number,
                            meta_score = calculate_course_metascore(review.course_subject, review.course_number) )
            
            course.department_name = find_dept_name_by_code(review.course_subject)
            course.review_set_count = len(Review.objects.filter(course_subject=review.course_subject).filter(course_number=review.course_number))
            course_list.append(course)
    return course_list


# this function is to check whether this course is inside the course_list array
# called by get_course_list()
def course_in_course_list(list, subject, number):
    course_sub_and_num = subject + str(number)
    for c in list:
        c_sub_and_num = c.subject + str(c.number)
        if (course_sub_and_num.find( c_sub_and_num ) >= 0 ):
            return True
    return False


# This function takes a department code
# and returns the corresponding department name in string
def find_dept_name_by_code(_code):
    try:
        return get_object_or_404(Department, code=_code).name
    except Exception as e:
        return "Dept not found"


# This function takes the course subject and number
# and returns the corresponding course name in string
def find_course_title_by_subject_and_number(_subject, _number):
    try:
        return get_object_or_404(Course, subject=_subject).title
    except Exception as e:
        return "Course title not found"

