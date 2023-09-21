from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models


class LevelSerializer(ModelSerializer):
    class Meta:
        model = models.Level
        fields = '__all__'



class StudentSerializer(ModelSerializer):
    level_text = serializers.CharField(source='level', read_only=True)
    class Meta:
        model = models.Student
        fields = '__all__'





class AnswerSerializer(ModelSerializer):
    question_text = serializers.CharField(source='question')
    class Meta:
        model = models.Answer
        fields = '__all__'

class QuestionkSerializer(ModelSerializer):
    # answers_s = AnswerSerializer(read_only=True, source='homework_question')
    answers = AnswerSerializer(read_only=True, many=True, source='question_answer')
    class Meta:
        model = models.Question
        fields = '__all__'
        

class HomeWorkSerializer(ModelSerializer):
    questions = QuestionkSerializer(many=True, read_only=True, source='homework_question')
    class Meta:
        model = models.HomeWork
        fields = '__all__'



class AnsweredQuestionSerializer(ModelSerializer):
    correct_answer_text_s = serializers.CharField(source='correct_answer')
    homework_text = serializers.CharField(source='homework')
    student_text = serializers.CharField(source='student')
    question_text = serializers.CharField(source='question')
    answer_text = serializers.CharField(source='answer')
    correct_answer_text = serializers.CharField(source='correct_answer')
    questionss = QuestionkSerializer(source='question')
    class Meta:
        model = models.AnsweredQuestion
        fields = '__all__'



class LessonSerializer(ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'


class MediaSerializer(ModelSerializer):
    class Meta:
        model = models.Media
        fields = '__all__'
