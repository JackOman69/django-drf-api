from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from django.http import Http404
from fitnesskit_task.models import Sources
from fitnesskit_task.serializers import SourcesSerializer
import httpx
import json
    
class SourcesApiView(GenericAPIView):
    
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Sources.objects.all()
    serializer_class = SourcesSerializer
    
    def get(self, *args, **kwargs):
        sources = Sources.objects.all()
        serializer = SourcesSerializer(sources, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SourcesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetailsViewSet(viewsets.ViewSet):
    
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = SourcesSerializer

    def get_object(self, id):
        try:
            return Sources.objects.get(id=id)
        except Sources.DoesNotExist:
            raise Http404

    def none_to_empty_str(items):
        return {k: v if v is not None else "" for k, v in items}
    
    @action(detail=True, methods=["get"])
    async def retrieve(self, request, id):
        source = self.get_object(id)
        serializer = SourcesSerializer(source)
        post_request = httpx.post(
            serializer.data["url"], 
            auth=(
                serializer.data["basic_auth"]["login"], 
                serializer.data["basic_auth"]["password"]
            ),
            json=serializer.data["request_body"]
        )
        
        json_data = []
        single_worker = {}
        list_of_workers = json.loads(json.dumps(post_request.json(), ensure_ascii=False))["Parameters"]
        
        for i in list_of_workers:
            single_worker.update({
                "id": i["ID"],
                "name": i["Name"],
                "last_name": i["Surname"],
                "phone": i["Phone"],
                "image_url": i["Photo"]
            })
            json_data.append({i: single_worker[i] if single_worker[i] is not None else "" for i in single_worker})
            single_worker = {}
            
        result = {"workers_list": json_data}
        
        return Response(result)
    
    @action(detail=True, methods=["put"])
    def update(self, request, id, *args, **kwargs):
        source = self.get_object(id)
        serializer = SourcesSerializer(source, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["delete"])
    def destroy(self, request, id):
        source = self.get_object(id)
        source.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    