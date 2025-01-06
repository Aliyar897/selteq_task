from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.db import connection
from .models import Task
from .serializers import TaskSerializer


# Create Task (POST API)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get Last 4 Tasks (GET API)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user).order_by('-created_at')[:4]
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


# Retrieve Task by Logged-in User using Raw SQL Query (GET API)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def retrieve_task(request, task_id):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM myapp_task
                WHERE id = %s AND user_id = %s
            """, [task_id, request.user.id])
            row = cursor.fetchone()

        if row:
            task = {
                'id': row[0],
                'title': row[1],
                'duration': row[2],
                'created_at': row[3],
                'updated_at': row[4]
            }
            return Response(task)
        else:
            return Response({'detail': 'Task not found or not authorized.'}, status=status.HTTP_404_NOT_FOUND)


# Update Task Title using Raw SQL Query (PUT API)
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_task(request, task_id):
    if request.method == 'PUT':
        title = request.data.get('title', None)
        if title:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE myapp_task
                    SET title = %s
                    WHERE id = %s AND user_id = %s
                """, [title, task_id, request.user.id])
            return Response({'detail': 'Task title updated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Title is required to update the task.'}, status=status.HTTP_400_BAD_REQUEST)


# Delete Task by Logged-in User (DELETE API)
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_task(request, task_id):
    if request.method == 'DELETE':
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
        return Response({'detail': 'Task deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
