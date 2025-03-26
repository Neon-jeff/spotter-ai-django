from re import M
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pydantic import ValidationError

from api.models import Trip
from .schema import CurrentLocationSchema, LocationSchema
from pyngo import drf_error_details
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from rest_framework.permissions import AllowAny

# Create your views here.


class CreateTripDetails(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        print(data)
        try:
            CurrentLocationSchema.model_validate(data["current_location"])
            LocationSchema.model_validate(data["pickup_location"])
            trip = Trip.objects.create(**data)
        except ValidationError as e:
            print(drf_error_details(e))
            return Response(
                {"message": "error", "fields": drf_error_details(e)}, status=400
            )
        return Response({"status": "success", "data": model_to_dict(trip)})

    def get(self, request):
        trips = Trip.objects.all()
        return Response(
            {"status": "success", "data": [model_to_dict(trip) for trip in trips]}
        )


class GetTrip(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk=None):
        if pk == None:
            return Response({"error": "trip id is required"}, status=400)
        try:
            trip = Trip.objects.get(id=int(pk))
            return Response({"status": "success", "data": model_to_dict(trip)})

        except ObjectDoesNotExist:
            return Response({"error": "trip not found"}, status=404)
