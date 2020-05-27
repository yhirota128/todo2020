import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Task


# Taskの必要なフィールドだけ出力するシリアライザー
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_text', 'status']


class TasksView(APIView):

    def get(self, request):
        # 全てのTaskを取得
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        # テキストを読み込んで新しいTaskを作成
        data = json.loads(request.body)
        task = Task(task_text=data['task_text'], status=0)
        task.save()

        # 作成したTaskを返却
        serializer = TaskSerializer(task)
        return Response(serializer.data, 201)


class TaskDetailView(APIView):

    def get(self, request, task_id):
        # 指定されたIDのTaskを取得、存在しなければ404
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(None, 404)

        serializer = TaskSerializer(task)
        return Response(serializer.data, 200)

    def post(self, request, task_id):
        # 指定されたIDのTaskを取得、存在しなければ400
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(None, 400)

        # 新しい値で更新
        data = json.loads(request.body)
        if 'task_text' in data:
            task.task_text = data['task_text']
        if 'status' in data:
            task.status = data['status']
        task.save()

        # 更新したTaskを返却
        serializer = TaskSerializer(task)
        return Response(serializer.data, 200)
