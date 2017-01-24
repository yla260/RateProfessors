# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, EasinessVote


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """返回最近发布的5个问卷."""
        return Question.objects.order_by('-pub_date')[:5]
    
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    
class ResultsView(generic.DetailView):
    model = Question
    template_name ='polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_easinessvote = question.easinessvote_set.get(pk=request.POST['easinessvote'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice1111111.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        selected_easinessvote.votes += 1
        selected_easinessvote.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def voteeasiness(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_easinessvote = question.easinessvote_set.get(pk=request.POST['easinessvote'])
    except (KeyError, EasinessVote.DoesNotExist):
        # 发生easinessvote未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a EasinessVote22222222222222.",
        })
    else:
        selected_easinessvote.votes += 1
        selected_easinessvote.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))








