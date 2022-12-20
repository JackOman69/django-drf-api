from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from fitnesskit_task.models import Sources, BasicAuth, RequestBody, ParametersRequestBody

class BasicAuthSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BasicAuth
        fields = ['login', 'password']
        
class ParametersSerializer(serializers.ModelSerializer): 

    class Meta:
        model = ParametersRequestBody
        fields = ['ServiceId']

class RequestBodySerializer(WritableNestedModelSerializer):
       
    Parameters = ParametersSerializer()
       
    class Meta:
        model = RequestBody
        fields = ['Request_id', 'ClubId', 'Method', 'Parameters']

class SourcesSerializer(WritableNestedModelSerializer):
    
    basic_auth = BasicAuthSerializer()
    request_body = RequestBodySerializer()
    

    class Meta:
        model = Sources
        fields = ['id', 'url', 'name', 'date', 'basic_auth', 'request_body']