from django.shortcuts import render
from django.http import JsonResponse

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        with open('./bot/data/sheets/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return JsonResponse({'message': 'Файл успешно загружен'})
    else:
        return JsonResponse({'error': 'Ошибка загрузки файла'}, status=400)
