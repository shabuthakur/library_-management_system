from rest_framework import serializers
from librarian.models import *
from member.models import MemberProfile

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model =Book
    fields='__all__'

class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model=MemberProfile
    
    fields='__all__'