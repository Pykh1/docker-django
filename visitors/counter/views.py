from django.http import HttpResponse
import redis

# Connect to Redis
client = redis.StrictRedis(host='redis-server', port=6379, db=0)

def index(request):
    visits = client.get('visits')

    if visits is None:
        client.set('visits', 1)  # Initialize visits with 1 if not set
        visits = 1
    else:
        visits = int(visits)

    # Increment the visits
    client.set('visits', visits + 1)
    
    return HttpResponse(f'N of visits: {visits}')  # Display the previous visits count
