from django.http import JsonResponse
import json

from django.shortcuts import get_object_or_404

from enroll.models import Registration


def post_req(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        R = Registration(
            name=body.get('name'),
            email=body.get('email'),
            mobile_no=body.get('mobile_no'),
            city=body.get('city')
        )
        R.save()

        return JsonResponse(
            {
                "message": "data uploaded succefully",
                "postgres": "please check you database for confirmation"
            }
        )


def get_req(request):
    if request.method == 'GET':
        list = []
        data = Registration.objects.all()
        for req_data in data:
            list.append(
                {
                    "id": req_data.id,
                    "name": req_data.name,
                    "email": req_data.email,
                    "mobile": req_data.mobile_no,
                    "city": req_data.city
                }
            )

        return JsonResponse(list)


def by_id(request, val):
    if request.method == 'GET':
        regi = get_object_or_404(Registration, pk=val)
        if regi:
            data = {
                "id": regi.id,
                "name": regi.name,
                "email": regi.email,
                "city": regi.city
            }

            return JsonResponse(data)

# def update(request):
#     if request.method == 'PUT':


# def get_req(request):
#     res = {
#         "status": True,
#         "message": "welcom to get api"
#     }
#     return JsonResponse(res)
#
#
# def post_req(request):
#     if request.method == 'POST':
#         res = {
#             "status": True,
#             "message": "welcom to post api"
#         }
#         return JsonResponse(res)
