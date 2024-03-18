from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Nairobi'
    dest1.desc = 'The city under the sun'
    dest1.img = 'destination_1.jpg'
    dest1.price = '200'

    dest2 = Destination()
    dest2.name = 'Mombasa'
    dest2.desc = 'Nulla pretium tincidunt felis, nec.'
    dest2.img = 'destination_2.jpg'
    dest2.price = '400'


    dest3 = Destination()
    dest3.name = 'Kisumu'
    dest3.desc = 'Nulla pretium tincidunt felis, nec.'
    dest3.img = 'destination_3.jpg'
    dest3.price = '350'

    dests = [dest1,dest2,dest3]

    return render(request,'index.html',{'dests' : dests});
