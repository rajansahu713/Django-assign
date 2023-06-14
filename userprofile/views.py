from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from django.core.exceptions import ObjectDoesNotExist
from .serializers import ProfileSerializer
from .models import ProfileModel

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)  
    
    def post(self,request):
        
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "message": "Records successfully created",
                "success": True },
                status=status.HTTP_201_CREATED )    
        
        return Response({
            "error":serializer.errors,
            "success":False },
            status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        
        id = request.query_params.get('id', None)
        if id: 
            try:
                userprofile = ProfileModel.objects.get(id=id)
            except ObjectDoesNotExist:
                return Response({
                    "error": "Profile User does not exist",
                    "success": False },
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                "error": "Please Provide id",
                "success": False },
                status=status.HTTP_400_BAD_REQUEST) 
        
        serializer = ProfileSerializer(userprofile, data=request.data, partial=True)    
        if serializer.is_valid():
            serializer.save()
            return Response({ "data": serializer.data,"message": "Records successfully updated","success": True},status=status.HTTP_200_OK )  
        
        return Response({"error":serializer.errors,"success":False },status=status.HTTP_400_BAD_REQUEST)
    
