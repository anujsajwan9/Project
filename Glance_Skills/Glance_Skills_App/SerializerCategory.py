from rest_framework import serializers
from Glance_Skills_App.models import ProjectCategory

class CategorySerial(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'