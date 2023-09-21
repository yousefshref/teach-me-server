from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Level(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('الاسم'))
    def __str__(self):
        return self.name

    class Meta:
         verbose_name = _('المرحلة التعليمية')
         verbose_name_plural = _('المراحل التعليمية')
    

class Student(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('الاسم'))
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=_('صورة'))
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name=_('رقم الهاتف'))
    level = models.ForeignKey(Level, blank=True, on_delete=models.CASCADE, verbose_name=_('المرحلة'))
    password = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('كلمة المرور'))
    password2 = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('تأكيد كلمة المرور'))
    review = models.IntegerField(validators=[MaxValueValidator(5)], null=True, blank=True, verbose_name=_('التقييم'))
    is_paied = models.BooleanField(default=True, verbose_name=_('هل دفع'))
    renew_date = models.DateField(null=True, blank=True, verbose_name=_('معاد التجديد'))

    def __str__(self):
        return str(self.name)

    class Meta:
         verbose_name = _('الطالب')
         verbose_name_plural = _('الطلاب')
    


class HomeWork(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('اسم الواجب'))
    level = models.ForeignKey(Level, null=True, blank=True, related_name='level_homework', on_delete=models.CASCADE, verbose_name=_('المرحلة'))
    date = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name=_('التاريخ'))
    publish = models.BooleanField(default=False, verbose_name=_('هل تنشرة الان ؟'))

    def __str__(self):
        return str(self.title)
    class Meta:
         verbose_name = _('الواجب')
         verbose_name_plural = _('الواجبات')

class Question(models.Model):
    homework = models.ForeignKey(HomeWork, null=True, blank=True, related_name='homework_question', on_delete=models.CASCADE, verbose_name=_('الواجب'))
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=_('صورة'))
    text = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('السؤال'))

    def __str__(self):
        return str(self.text) 

    class Meta:
         verbose_name = _('السؤال')
         verbose_name_plural = _('الاسئلة')

class Answer(models.Model):
    homework = models.ForeignKey(HomeWork, null=True, blank=True, related_name='homework_answer', on_delete=models.CASCADE, verbose_name=_('الواجب'))
    question = models.ForeignKey(Question, null=True, blank=True, related_name='question_answer', on_delete=models.CASCADE, verbose_name=_('السؤال'))
    text = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('الاجابة'))

    is_correct = models.BooleanField(default=False, verbose_name=_('هل الاجابة صحيحة ؟'))

    def __str__(self):
        return str(self.text)

    class Meta:
         verbose_name = _('الاجابة')
         verbose_name_plural = _('الاجابات')

class AnsweredQuestion(models.Model):
    homework = models.ForeignKey(HomeWork, null=True, blank=True, related_name='student_answered', on_delete=models.CASCADE, verbose_name=_('الواجب'))
    student = models.ForeignKey(Student, null=True, blank=True, related_name='student_answered', on_delete=models.CASCADE, verbose_name=_('الطالب'))
    question = models.ForeignKey(Question, null=True, blank=True, related_name='question_answered', on_delete=models.CASCADE, verbose_name=_('السؤال'))
    answer = models.ForeignKey(Answer, null=True, blank=True, related_name='answer_answered', on_delete=models.CASCADE, verbose_name=_('الاجابة'))
    is_correct = models.BooleanField(default=False, verbose_name=_('هل صحيحة'))
    correct_answer = models.ForeignKey(Answer, null=True, blank=True, related_name='correct_answer_answered', on_delete=models.CASCADE, verbose_name=_('الاجابة الصحيحة'))
    review = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('التقييم'))
    date = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name=_('التاريخ'))

    def save(self, *args, **kwargs):
        get_question = Question.objects.get(homework__id=self.homework.pk, text=self.question.text)
        get_true_answer = Answer.objects.get(question__id=get_question.pk, is_correct=True)
        get_answer_i_wrote = Answer.objects.get(question__id=get_question.pk, text=self.answer.text)

        if get_answer_i_wrote == get_true_answer:
            self.is_correct = True
        else:
            self.is_correct = False

        self.correct_answer = get_true_answer

        super(AnsweredQuestion, self).save(*args, **kwargs)

        questions_length = Question.objects.filter(homework__id=self.homework.pk)
        student_true_answers = AnsweredQuestion.objects.filter(student__id=self.student.pk, is_correct=True, homework__id=self.homework.pk)

        super(AnsweredQuestion, self).save(*args, **kwargs)
        
        student_answers = AnsweredQuestion.objects.filter(student__id=self.student.pk, homework__id=self.homework.pk)
        for i in student_answers:
            i.review = f'{len(questions_length)} / {len(student_true_answers)}'
            i.save_base()


    def __str__(self):
        return str(self.question)

    class Meta:
         verbose_name = _('اجابة الواجبات')
         verbose_name_plural = _('اجابات الواجبات')





class Lesson(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('الاسم'))
    description = models.TextField(null=True, blank=True, verbose_name=_('الوصف'))
    level = models.ForeignKey(Level, null=True, blank=True, related_name='level_lesson', on_delete=models.CASCADE, verbose_name=_('المرحلة'))
    video = models.FileField(upload_to='videos/', null=True, blank=True, verbose_name=_('الفديو'))
    file = models.FileField(upload_to='pdf/', null=True, blank=True, verbose_name=_('ملف مرفقات'))
    date = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name=_('التاريخ'))

    def formatted_description(self):
        if self.description:
            return self.description.replace('\n', '<br>')
        return ''


    def __str__(self):
        return str(self.title)


    class Meta:
         verbose_name = _('الدرس')
         verbose_name_plural = _('الدروس')





class Media(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('الاسم'))
    description = models.TextField(null=True, blank=True, verbose_name=_('الصوف'))
    level = models.ForeignKey(Level, null=True, blank=True, related_name='level_media', on_delete=models.CASCADE, verbose_name=_('المرحلة'))
    file = models.FileField(upload_to='pdf/', null=True, blank=True, verbose_name=_('الملف'))
    date = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name=_('التاريخ'))
    
    def __str__(self):
        return str(self.title)

    class Meta:
         verbose_name = _('الملف')
         verbose_name_plural = _('الملفات')




         
class Media(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('الاسم'))
    description = models.TextField(null=True, blank=True, verbose_name=_('الصوف'))
    level = models.ForeignKey(Level, null=True, blank=True, related_name='level_media', on_delete=models.CASCADE, verbose_name=_('المرحلة'))
    file = models.FileField(upload_to='pdf/', null=True, blank=True, verbose_name=_('الملف'))
    date = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name=_('التاريخ'))
    
    def __str__(self):
        return str(self.title)

    class Meta:
         verbose_name = _('الملف')
         verbose_name_plural = _('الملفات')
