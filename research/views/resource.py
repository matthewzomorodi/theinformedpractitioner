from django.shortcuts import render

def handleRequest(request, resource_id=None):

    context = {
        'index_title': 'Resource Page'
    }

    if resource_id:
        # Handle existing resource
        print("resource_id=" + str(resource_id))

        if request.method == 'GET':
            # Return instance of specified resource
            print("request.GET=" + str(request.GET))

        elif request.method == 'POST':
            # Update existing resource
            print("request.POST=" + str(request.POST))

    else:
        # Handle new resource
        if request.method == 'GET':
            # Return empty form for creating new resource
            print("request.GET=" + str(request.GET))
            
        elif request.method == 'POST':
            # Create new resource from form data
            print("request.POST=" + str(request.POST))
    
    return render(request, 'research/index.html', context)