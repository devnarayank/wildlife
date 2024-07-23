from django.shortcuts import render
from .models import AnimalObservation
import requests

def dashboard(request):
    api_data = fetch_from_rust_api()
    if api_data:
        # Process and save the data
        for item in api_data:
            AnimalObservation.objects.create(
                species=item['species'],
                location=item['location'],
                confidence=item['confidence']
            )
    
    latest_observations = AnimalObservation.objects.order_by('-timestamp')[:5]
    context = {
        'latest_observations': latest_observations,
    }
    return render(request, 'monitoring/dashboard.html', context)



def fetch_from_rust_api():
    # This is a placeholder. Replace with actual API endpoint
    api_url = "http://localhost:8000/api/observations"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None