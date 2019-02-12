from django.http import HttpResponse
from django.http import JsonResponse
import json


def question1(request):
    with open("/home/mithu/work/project/project/project/question-answers.json") as file:
        d = json.load(file)
    selectedOption = request.GET.get("options", None)
    dNo = ""
    if selectedOption != None:
        selectedOption = selectedOption.lower()
        if selectedOption == "no":
            dNo = d["options"]["No"]
            response = JsonResponse(dNo, safe=False)
            #temporary: to avoid CORS Blocking (Security flaw!!)
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            response["Access-Control-Max-Age"] = "1000"
            response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            return response

    options1 = d["options"]
    keylist = d["options"].keys()
    dd = {
        "question": d["q1"],
        "options": keylist
    }
    response = JsonResponse(dd, safe=False)

    #temporary: to avoid CORS Blocking (Security flaw!!)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response



def question2(request):
    response = {}
    with open("/home/mithu/work/project/project/project/question-answers.json") as file:
        d = json.load(file)

        
    selectedOption = request.GET.get("options", None)
    
    dd = {}
    if selectedOption != None:
        selectedOption = selectedOption.lower()
        if selectedOption == "hamburger":
            dd = { "reply" : d["options"]["Yes"]["options"]["Hamburger"]["reply"]
            }
        elif selectedOption == "pop corn": 
            dd = { "reply" : d["options"]["Yes"]["options"]["Pop Corn"]["reply"]
            }
        elif selectedOption == "chicken":  
            dd = { "reply" : d["options"]["Yes"]["options"]["Chicken"]["reply"]
            }
    else:
        options1 = d["options"]
        keylist = d["options"]["Yes"]["options"].keys()
        dd = {
            "question": d["options"]["Yes"]["q2"],
            "options" : keylist
        }
        
    response = JsonResponse(dd, safe=False)
    #temporary: to avoid CORS Blocking (Security flaw!!)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


def pizzaSelection(request):
    with open("/home/mithu/work/project/project/project/question-answers.json") as file:
            d = json.load(file)
    
    selectedOption = request.GET.get("options", None)
    dd = {}
    if selectedOption != None:
        selectedOption = selectedOption.lower()
        if selectedOption == "yes":
            keylist = d["options"]["Yes"]["options"]["Pizza"]["options"].keys()
            dd = {
            "Reply": d["options"]["Yes"]["options"]["Pizza"]["options"]["Yes"],
            }
        elif selectedOption == "no":
            dd = {"Reply": d["options"]["Yes"]["options"]["Pizza"]["options"]["No"]
            }
    else:
        keylist = d["options"]["Yes"]["options"]["Pizza"]["options"].keys()
        
        dd = {
            "question": d["options"]["Yes"]["options"]["Pizza"]["question"],
            "options" : keylist
            }
    response = JsonResponse(dd, safe=False)
    #temporary: to avoid CORS Blocking (Security!!)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response