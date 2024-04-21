from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
import subprocess



class CodeEditor(View):
    def get(self, request, *args, **kwargs):

        code = """
def sum_of_list(x):
  return sum(x)

    
print("Code Output")
print(sum_of_list([1,2,3,4,5]))"""
        context = {'page_title': 'Code Editor',
                   'question_title' : "This is question title",
                   'question_description' : 'Description',
            'python_code': code}
        return render(request,'code_editor/code_editor.html',context)



class CodeOutput(View):
    def post(self, request, *args, **kwargs):
        code_dict = json.loads(request.body)  
        code = code_dict.get('code', '')
        lang = code_dict.get('lang', '')
        # Right now only python is supported
        if lang!='Python':
            return HttpResponse('Only Python Language is supported At this Moment')
        output = self.run_code(code)
        print(output)
        return HttpResponse(output)

    
    def run_code(self, code):

        try:
            output = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, timeout=10)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
        # If there's an error, return the error message
            return str(e.output.decode('utf-8'))
        except subprocess.TimeoutExpired:
            # If the code execution times out, return an error message
            return 'Code execution timed out.'
        except Exception as e:
            # If any other exception occurs, return the exception message
            return str(e)
            



