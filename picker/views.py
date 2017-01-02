from django.db.models import Max
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from picker.models import Car
from picker.serializers import CarSerializer


@api_view(['GET'])
def car_list(request):
    """
    List all cars
    """
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

def get_default_prefs():
    return {field.name: 0 for field in Car._meta.fields}

def find_next_car(prefs):
    top = max(prefs, key=prefs.get)
    return Car.objects.order_by(top).reverse().first()

def update_prefs(existing, update):
    for key in update:
        if key in existing:
            existing[key] += 1
    return existing

@api_view(['GET', 'POST'])
def next_car(request):
    if 'prefs' not in request.session:
        request.session['prefs'] = get_default_prefs()
    if request.method == 'POST':
        request.session['prefs'] = update_prefs(request.session['prefs'], request.data)
    car = find_next_car(request.session['prefs'])
    serializer = CarSerializer(car)
    return Response(serializer.data)
