from rest_framework import serializers
from analyzer.models.analysis_model import Analysis


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ['id', 'complexity', 'number_lines', 'comments']