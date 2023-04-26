from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.shortcuts import render

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

