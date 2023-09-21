from django.shortcuts import render

from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.db.models import Count, F
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
import fractions


@api_view(['POST'])
def sign_up(request):
    data = request.data

    name = data['name']
    phone = data['phone']
    password = data['password']
    password2 = data['password2']
    level = data['level']

    if len(phone) != 11:
        return Response({"error": "اكتب رقم هاتفك صحيح يجب ان يكون 11 رقم"})

    try:
        exist = models.Student.objects.get(phone=phone)
        return Response({"error": "رقم الهاتف مسجل بالفعل, يرجي تسجيل الدخول بدلا من انشاء حساب جديد"})
    except:
        pass

    if len(password) < 8:
        return Response({"error": "كلمة المرور يجب ان تكون اكثر من 8 احرف"})

    if password != password2:
        return Response({"error": "يجب ان تكون كلمتان المرور متطابقتان"})

    if len(name) == 0:
        return Response({"error": "يجب ان تكتب اسمك"})

    if level == 0 or level == '' or level == False or not level:
        return Response({"error": "يجب ان تختار مرحلة تعليمك"})

    ser = serializers.StudentSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
    return Response({"success": "تم انشاء الحساب بنجاح"})

# {
    # "name":"",
    # "phone":"",
    # "password":"",
    # "password2":"",
    # "level":"",
# }


@api_view(['POST'])
def log_in(request):
    data = request.data

    phone = data['phone']
    password = data['password']

    if len(phone) != 11:
        return Response({"error": "اكتب رقم الهاتف صحيح, يجب ان يكون 11 رقم"})

    try:
        exist = models.Student.objects.get(phone=phone)
        if exist.password == password:
            return Response({"success": "تم تسجيل الدخول بناح"})
        return Response({"error": "كلمة المرور غير صحيحة"})

    except:
        return Response({"error": "هذا الرقم غير موجود, لو هذه اول مره تدخل فيها يرجي انشاء حساب جديد"})

# {
# "phone":"01095753871",
# "password":"01095753871Ysmb#@"
# }


@api_view(['GET'])
def get_levels(request):
    q = models.Level.objects.all()
    ser = serializers.LevelSerializer(q, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_student(request):
    phone = request.GET.get('phone')
    q = models.Student.objects.get(phone=phone)
    ser = serializers.StudentSerializer(q)
    return Response(ser.data)





@api_view(['GET'])
def get_homework(request):
    q = models.HomeWork.objects.all()    
    id_param = request.GET.get('id')
    level_param = request.GET.get('level')

    q = q.filter(level=level_param)

    if id_param:
        q = q.filter(id=id_param)

    ser = serializers.HomeWorkSerializer(q.order_by('-id'), many=True)

    return Response(ser.data)


@api_view(['GET'])
def get_homework_answer(request):
    q = models.AnsweredQuestion.objects.all()
    q2 = models.Answer.objects.all()
    homework = request.GET.get('homework')
    student = request.GET.get('student')

    q = q.filter(homework__id=homework, student__phone=student)
    try:
        q2 = q2.filter(homework__id=q.first().homework.pk)
        if q == q2:
            return Response({"thereis":"s"})
        print(q)
        print(q2)
    except:
        print('not there')
        return Response({"notthere":"s"})

    return Response({"":""})





@api_view(['GET'])
def get_student_answers(request):
    homework = request.GET.get('homework')
    student = request.GET.get('student')
    q = models.AnsweredQuestion.objects.filter(
        homework__id=homework,
        student__phone=student
    )

    ser = serializers.AnsweredQuestionSerializer(q, many=True)
    return Response(ser.data)





@api_view(['POST'])
def send_answer(request):
    homework_id = request.data['homework']
    student_id = request.data['student']
    question_id = request.data['question']
    answer_id = request.data['answer']

    if not answer_id:
        return Response({"error":"يجب ان تدخل اجابة"})
    else:
        models.AnsweredQuestion(
            homework_id=homework_id,
            student_id=student_id,
            question_id=question_id,
            answer_id=answer_id,
        ).save()
        return Response({"success":"done"})
    








@api_view(['GET'])
def get_lessons(request):
    level = request.GET.get('level')

    q = models.Lesson.objects.filter(level__id=level)

    if request.GET.get('id'):
        q = q.filter(id=request.GET.get('id'))

    if request.GET.get('name'):
        q = q.filter(title=request.GET.get('name'))

    ser = serializers.LessonSerializer(q.order_by('-id'), many=True)

    return Response(ser.data)





@api_view(['GET'])
def get_media(request):
    level = request.GET.get('level')
    q = models.Media.objects.filter(level__id=level)

    if request.GET.get('id'):
        q = q.filter(id=request.GET.get('id'))

    ser = serializers.MediaSerializer(q.order_by('-id'), many=True)

    return Response(ser.data)



class StudentImageUpdateView(generics.UpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    parser_classes = (MultiPartParser, FormParser)






@api_view(['GET'])
def get_total_infos(request):
    level = request.GET.get('level')
    phone = request.GET.get('phone')
    
    # total answerd homeworks
    student_answerd_homeworks = models.AnsweredQuestion.objects.filter(student__phone=phone) # all student answers
    annotated_queryset = student_answerd_homeworks.values('homework').annotate(count=Count('homework'))
    length = len(annotated_queryset)

    # total homeworks did't answered
    all_homeworks = models.HomeWork.objects.filter(level__id=level)
    length_all_homeworks = len(all_homeworks)

    didnt_answerd = length_all_homeworks - length

    results = {
        "total_answerd_hms":length,
        "didnt_answerd":didnt_answerd,
    }

    return Response({"data":results})



@api_view(['GET'])
def get_lessons_names(request):
    level = request.GET.get('level')

    all_lessons = models.Lesson.objects.filter(level__id=level)

    names = []

    for i in all_lessons:
        names.append(i.title)


    print(names)

    return Response({"names":names})





