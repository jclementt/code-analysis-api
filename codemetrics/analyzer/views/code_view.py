from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import radon.complexity as radon_complexity

from analyzer.models.analysis_model import Analysis
from analyzer.models.code_model import Code
from analyzer.serializers.code_serializer import CodeSerializer


class CodeView(APIView):
    def post(self, request):
        # Receber e processar o código
        content = request.data.get('content')
        origin = request.data.get('origin')
        
        # Criar o código no banco
        code = Code.objects.create(content=content, origin=origin)

        # Análise de Complexidade com Radon
        complexity = radon_complexity.cc_visit(content)
        number_lines = len(content.splitlines())
        comments = sum([1 for line in content.splitlines() if line.strip().startswith('#')])

        # Criar a análise no banco
        analysis = Analysis.objects.create(
            code=code,
            complexity=complexity,
            number_lines=number_lines,
            comments=comments
        )

        # Retornar os dados da análise
        return Response(CodeSerializer(code).data, status=status.HTTP_201_CREATED)
