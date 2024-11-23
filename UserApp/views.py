from turtle import isvisible
from bson import is_valid, ObjectId
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Users
from UserApp.serialize import userSerializer

# Create your views here.

@csrf_exempt
def users(request, id=0):
    if request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serialize = userSerializer(data=user_data)
        if user_serialize.is_valid():
            user_serialize.save()
            return JsonResponse("User added successfully", safe=False)
        return JSONParser('Failed to Add', safe=False)
    elif request.method=='GET':
        user = Users.objects.all()  
        user_serialize = userSerializer(user, many=True)
        return JsonResponse(user_serialize.data, safe=False)
    elif request.method=='PUT':
        try:
            user_data = JSONParser().parse(request)
            # Verifique se o id é válido
            if not ObjectId.is_valid(id):
                return JsonResponse('Invalid ID', status=400)

            user = Users.objects.get(_id=ObjectId(id))  # Converter id para ObjectId
            user_serialize = userSerializer(user, data=user_data)
            if user_serialize.is_valid():
                user_serialize.save()
                return JsonResponse('Updated Successfully', safe=False)
            return JsonResponse('Failed to update', safe=False)
        except Users.DoesNotExist:
            return JsonResponse('User not found', status=404)
    elif request.method == 'DELETE':
        try:
        # Valida se o ID é um ObjectId válido
            if not ObjectId.is_valid(id):
                return JsonResponse({'error': 'Invalid ID format'}, status=400)
            
            # Busca o usuário
            user = Users.objects.get(_id=ObjectId(id))
            user.delete()
            return JsonResponse({'message': 'Deleted Successfully'}, status=200)
        
        except Users.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)