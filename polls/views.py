from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world !")


from django.shortcuts import render,redirect

from django.http import HttpResponse
import json
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from .serializers import PageperformanceSerializer

from .models import Pageperformance

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework import serializers

import json
import requests


# Create your views here.
def chatgptindex(request):
    return HttpResponse("Hello, world !")
pageinsights_api_key = "your-api-key"

dot = './media/json/'

class DesktopView(ListCreateAPIView):
    queryset = Pageperformance.objects.all()
    serializer_class = PageperformanceSerializer

    def post(self, request):
        input_url = request.data.get('input_url')
        if not input_url:
            input_url = request.query_params.get('input_url')
        # api_key = "your-api-key"
        strategy = "desktop"  # or "desktop" OR "mobile" 

        # Use the PageSpeed Insights API to fetch a report on website performance, best practices, accessibility, and PWA
        psi_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={input_url}&key={pageinsights_api_key}&strategy={strategy}&category=performance&category=accessibility&category=seo&category=best-practices"  
        #psi_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}&strategy={strategy}&category=performance,accessibility,best-practices,seo,pwa"
        response = requests.get(psi_url)
        report = response.json()

        # Print the report
        # print(report)

        # Serializing json
        json_object = json.dumps(report, indent=4)
        
        # Writing to sample.json
        # print(dot)
        filepath = dot+"desktop.json"
        with open(filepath, "w") as outfile:
            outfile.write(json_object)
        with open(filepath) as f:
            data = json.load(f)
            #print(data)
            performance_score =  data["lighthouseResult"]["categories"]["performance"]["score"]* 100
            accessibility_score = data["lighthouseResult"]["categories"]["accessibility"]["score"]* 100
            best_practices_score =  data["lighthouseResult"]["categories"]["best-practices"]["score"]* 100
            seo_score = data["lighthouseResult"]["categories"]["seo"]["score"]* 100
            # print(performance_score)
            # print(accessibility_score)
            # print(best_practices_score)
            # print(seo_score)
        x = {"performance": round(performance_score), "accessibility": round(accessibility_score), "best-practices":round(best_practices_score), "seo": round(seo_score)}
        # output_data = json.dumps(x, indent = 5) 
        output_data = json.dumps(x, indent = 4) 
        print(output_data)
        # print(x)
        seo = Pageperformance.objects.create(input_url=input_url, output_data=output_data)
        # print(output_data)
        serializer = PageperformanceSerializer(seo)
        return Response(serializer.data)



class DesktopUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Pageperformance.objects.all()
    serializer_class = PageperformanceSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]