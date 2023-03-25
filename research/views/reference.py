from django.shortcuts import render

def handleRequest(request, reference_id=None):

    context = {
        'index_title': 'Reference Page'
    }

    if reference_id:
        # Handle existing reference
        print("reference_id=" + str(reference_id))

        if request.method == 'GET':
            # Return instance of specified reference
            print("request.GET=" + str(request.GET))

        elif request.method == 'POST':
            # Update existing reference
            print("request.POST=" + str(request.POST))

    else:
        # Handle new reference
        if request.method == 'GET':
            # Return empty form for creating new reference
            print("request.GET=" + str(request.GET))
            
        elif request.method == 'POST':
            # Create new reference from form data
            print("request.POST=" + str(request.POST))
    
    return render(request, 'research/index.html', context)