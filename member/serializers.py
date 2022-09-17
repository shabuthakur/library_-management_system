from rest_framework import serializers
from member.models import *

class BorrowedSerializer(serializers.ModelSerializer):
  class Meta:
    model =BookBorrwed
    fields='__all__'