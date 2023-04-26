from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.shortcuts import render
import uuid
from django.http import JsonResponse
from gridfs import GridFS

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
# Select the database
db = client['mydatabase']
# Select the collection
col = db['mycollection']

def home_page(request):
    # return db.list_collection_names()
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        
        # Insert the file to the database
        file_id = col.insert_one({'filename': myfile.name, 'filedata': myfile.read()}).inserted_id

        # Generate a short link for the file
        short_link = 'http://example.com/files/' + str(file_id)

        return render(request, 'upload_success.html', {'short_link': short_link})
    return render(request, 'index.html')

def generate_short_link(request, file_id):
    # retrieve the file object from MongoDB using the appropriate query
    file = file.objects.get(id=file_id)
    
    # generate a unique short link for the file
    short_link = str(uuid.uuid4())
    
    # store the short link and the corresponding file information in a database
    short_link.objects.create(link=short_link, file=file)
    
    # construct the URL for the download link
    download_url = request.build_absolute_uri('/download/' + short_link)
    
    # return a JSON response with the download URL
    return JsonResponse({'download_url': download_url})

# # global var to store id of signedin user
# user = None 

# def download_file(request, file_id):
#     global user
#     # Connect to MongoDB and retrieve the GridFS object
#     fs = GridFS(db)

#     # Retrieve the file from GridFS using the given file ID
#     file = fs.get(file_id)

#     # Set the response headers to indicate that this is a file download
#     response = HttpResponse(file.read())
#     response['Content-Type'] = file.content_type
#     response['Content-Disposition'] = f'attachment; filename="{file.filename}"'
#     return response