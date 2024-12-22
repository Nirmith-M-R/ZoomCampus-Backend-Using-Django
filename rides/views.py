from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SignUP,Rider,ActiveUser,RiderAccept, RideStarted
import json
import datetime

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            # print(request.body)
            data = request.body.decode('utf-8')
            data = json.loads(data)
            # print(data)
            # Extract user details
            mail = data.get('mail').strip()
            password = data.get('password').strip()
            name = data.get('name').strip()
            phNo = data.get('phNo').strip()
            gender = data.get('gender').strip()
            program = data.get('program').strip()
            route = data.get('route', [])  # Default to an empty list if not provided

            # Validate mandatory fields
            if not (mail and password and name and phNo and gender and program):
                return JsonResponse({'error': 'All fields except route are required.'}, status=400)
            # print("here")
            # Create the user
            user = SignUP(
                mail=mail,
                password=password,
                name=name,
                phNo=phNo,
                gender=gender,
                program=program,
                route=route
            )
            user.save()

            # Return success response
            return JsonResponse({'success': f'User {user.name} added successfully!'}, status=200)

        except Exception as e:
            # Handle errors
            return JsonResponse({'error': str(e)}, status=500)

    # If the method is not POST
    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

@csrf_exempt
def login(request):
    if request.method=="POST":
        try:
            data = request.body.decode('utf-8')
            data = json.loads(data)
            mail = data.get("mail")
            password = data.get("password")
            user = SignUP.objects.get(mail=mail)
            if(password==user.password):
                return JsonResponse({"status":"Success"},status=200)
        except:
            return JsonResponse({"status":"Fail"},status=205)

@csrf_exempt
def activateRider(request):
    data = request.body.decode('utf-8')
    data = json.loads(data)
    print(data)
    mail = data.get('mail')
    ob = SignUP.objects.get(mail=mail)
    x = ActiveUser(mail=mail, name = ob.name,phNo = ob.phNo, gender=ob.gender, rating=ob.rating, route=ob.route,gate = data.get('gate'))
    x.save()
    return JsonResponse({"status":"Activated"}, status=200)
    
@csrf_exempt
def riderregistercheck(request):
    if request.method == "POST":
        # print("hi")
        try:
            data = request.body.decode('utf-8')
            # print(data)
            data = json.loads(data)
            # print("hello")
            print(data)
            mail = data.get('mail')
            # print(mail)
            data = Rider.objects.get(mail=mail)
            if(mail == data.mail):
                return JsonResponse({"Status":"Registered"}, status=200)                
        except:
            return JsonResponse({"Status":"Not Registered"}, status=205)
        
@csrf_exempt
def riderregister(request):
    if request.method == "POST":
        try:
            data = request.POST
            mail = data.get('mail')
            seats = data.get('seats')
            regno = data.get('regno')
            ob = Rider.objects.create(mail=mail, seats=seats, regNo = regno)
            return JsonResponse({"Status":"Registration Done"}, status = 200)
        except:
            return JsonResponse({"Status":"Error"}, status=205)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
        

@csrf_exempt
def request_ride(request):
    if request.method == "POST":
        # try:
        data = request.body.decode('utf-8')
        print(data)
        data = json.loads(data)
        mails = data.get("mail")
        print("HHH"+mails)
        print(type(mails))
        passenger = SignUP.objects.get(mail=mails)
        print("H1")
        # passenger.route = list(passenger.route)
        print("HI")
        passenger_route = passenger.route
        rider = ActiveUser.objects.all()
        print(type(passenger_route))
        print(passenger_route, passenger.route)
        riders = []
        print(rider)
        for i in range(len(rider)):
            # print(type(rider[i].route))
            flag = False
            if rider[i].mail == passenger.mail:
                continue
            rider[i].route = list(rider[i].route)
            print((rider[i].route), rider[i].mail)
            for j in range(len(passenger_route)-1,-1,-1):
                for n in range(len(rider[i].route)-1,-1,-1):
                    if passenger_route[j].lower() == rider[i].route[n].lower():
                        riders.append({"name":rider[i].name, "gender":rider[i].gender, "destination":passenger_route[j], })
                        flag = True
                        break
                if flag:
                    break
                    
        if riders==[]:
            return JsonResponse({"status":"No Riders"},status=205)
        return JsonResponse(riders,status=200, safe=False)
        # except:
        #     return JsonResponse({"status":"Rider not found"},status=205)
        

@csrf_exempt
def req_rider(request):
    if request.method == "POST":
        try:
            data = request.body.decode('utf-8')
            data = json.loads(data)
            mail = data.get("mail")
            ridermail = data.get('ridermail')
            rider = ActiveUser.objects.get(mail = ridermail)
            corider = SignUP.objects.get(mail=mail)
            RiderAccept.objects.create(corider_name=corider.name, corider_mail=mail, corider_gender=corider.gender, corider_phNo=corider.phNo, corider_gate=data.get("gate"),corider_dest=data.get("destination"),rider_mail=rider.mail)
        except:
            return JsonResponse({"status":"error"}, status =205)
        
@csrf_exempt
def rider_ride_req(request):
    if request.method == "POST":
        try:
            data = request.body.decode('utf-8')
            data = json.loads(data)
            print(data)
            mail = data.get("mail")
            print(mail)
            ride = RiderAccept.objects.get(rider_mail=mail)
            print(ride)
            return JsonResponse([{"gender":ride.corider_gender, "name":ride.corider_name, "phNo":ride.corider_phNo, "gate":ride.corider_gate, "destination":ride.corider_dest}], status=200, safe=False)
        except:
            return JsonResponse({"status":"No Ride"},status=205)
        
@csrf_exempt
def rider_accept_ride(request):
    if request.method=="POST":
        try:
            data = request.body.decode('utf-8')
            data = json.loads(data)
            rider_mail = data.get("rider_mail")
            rider = SignUP.objects.get(mail=rider_mail)
            corider_mail = data.get("corider_mail")
            corider = SignUP.objects.get(mail=corider_mail)
            RideStarted.objects.create(rider_mail=rider_mail, corider_mail=corider_mail, rider_phNo = rider.phNo, corider_phNo=corider.phNo)
            gate = RiderAccept.objects.get(rider_mail).corider_gate
            return JsonResponse({"status":"Ride Started", "rider_phNo":rider.phNo, "corider_phNo":corider.phNo, "gate":gate, "rating":rider.rating}, status = 200)
        except:
            return JsonResponse({"status":"error"},status=205)

@csrf_exempt
def ride_terminate(request):
    if request.method=="POST":
        try:
            data = request.body.decode('utf-8')
            data = json.loads(data)
            rider_mail = data.get("rider_mail")
            corider_mail = data.get("corider_mail")
            x = RiderAccept.objects.get(rider_mail=rider_mail)
            x.delete()
            rider = SignUP.objects.get(rider_mail)
            rider = rider.append(['Rider',corider_mail, datetime.datetime])
            return JsonResponse({"status":"Ride Completed"},status=200)
        except:
            return JsonResponse({"status":"error"},status=205)
        
@csrf_exempt
def getlocation(request):
    if request.method == "POST":
        try:
            # Parse JSON request body
            data = json.loads(request.body.decode('utf-8'))
            
            # Extract source, destination, and checkpoints
            source = data.get('source')  # Example: "1600 Amphitheatre Parkway, Mountain View, CA"
            destination = data.get('destination')  # Example: "1 Infinite Loop, Cupertino, CA"
            checkpoints = data.get('checkpoints')  # Example: ["Checkpoint1", "Checkpoint2"]
            
            # Validate data
            if not source or not destination:
                return JsonResponse({'error': 'Source and destination are required.'}, status=400)
            
            # Successful response
            return JsonResponse({
                'source': source,
                'destination': destination,
                'checkpoints': checkpoints,
                'message': 'Locations received successfully'
            }, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

