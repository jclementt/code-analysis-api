from rest_framework import serializers

from analyzer.models.code_model import Code
from analyzer.serializers.analysis_serializer import AnalysisSerializer


class CodeSerializer(serializers.ModelSerializer):
    analysis_result = AnalysisSerializer(many=True, read_only=True)

    class Meta:
        model = Code
        fields = ['id', 'content', 'origin', 'send_date', 'analysis_result']