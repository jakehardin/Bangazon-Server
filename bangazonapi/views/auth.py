from bangazonapi.models import Seller
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    seller = Seller.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if seller is not None:
        data = {
            'id': seller.id,
            'uid': seller.uid,
            # 'customer_id': seller.bio,
            'name': seller.id,
            'profile_image_url': seller.uid,
            # 'email': seller.bio
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the levelupapi_gamer table
    seller = Seller.objects.create(
        # name=request.data['name'],
        uid=request.data['uid']
    )

    # Return the gamer info to the client
    data = {
        'id': seller.id,
        'uid': seller.uid,
        'customer_id': seller.id,
        'name': seller.name,
        # 'profile_image_url': seller.image,
        'email': seller.email
    }
    return Response(data)
