#coding=utf-8
'''
@Author Milo
@Date 2018／06／21 11:09
'''

from django.http import JsonResponse
def websockets(request):
    return JsonResponse({'code': 200, 'msg': 'OK'})