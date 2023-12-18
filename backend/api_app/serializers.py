from rest_framework import serializers
from . models import student

class studentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=student
        fields=["first_name","last_name","domain"]
