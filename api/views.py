from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class GetEntry(APIView):

    def get(self, request):
        return Response({'get_entry': 'single'})
    
class GetEntries(APIView):
    
    def get(self, request):
        return Response({'get_entries' : 'all'})
    
class PostEntry(APIView):

    def post(self, request):
        return Response({'post_entry', 'single'})
    
class PutEntry(APIView):

    def put(self, request):
        return Response({'put_entry': 'single'})
    
class DeleteEntry(APIView):

    def delete(self, request):
        return Response({'delete_entry': 'single'})

