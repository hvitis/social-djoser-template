from social_core.backends.google import BaseGoogleOAuth2API
from social_core.backends.oauth import BaseOAuth2
from django.http import JsonResponse
from django.views import View

class ObtainUserFromGoogle(View):

    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        print(json_obj)
        return JsonResponse(json_obj)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context

class CustomBaseOAuth(BaseOAuth2):
    def extra_data(self, user, uid, response, details=None, *args, **kwargs):
        """Return access_token, token_type, and extra defined names to store in
            extra_data field"""
        data = super(BaseOAuth2, self).extra_data(user, uid, response,
                                                  details=details,
                                                  *args, **kwargs)
        data['token_type'] = response.get('token_type') or \
            kwargs.get('token_type')
        data['picture'] = response.get('picture') or \
            kwargs.get('picture')

        data['uuid'] = str(user.unique_id.hex)
        print(""" 
        User's UUID : {} 

        """.format(str(user.unique_id.hex)))
        return data


class CustomGoogleOAuth2(BaseGoogleOAuth2API, CustomBaseOAuth):
    name = 'google-oauth2'
    # permission_classes = [permissions.AllowAny]
    REDIRECT_STATE = False
    AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/auth'
    # ACCESS_TOKEN_URL = 'https://oauth2.googleapis.com/token'
    ACCESS_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
    ACCESS_TOKEN_METHOD = 'POST'
    REVOKE_TOKEN_URL = 'https://accounts.google.com/o/oauth2/revoke'
    REVOKE_TOKEN_METHOD = 'GET'
    # The order of the default scope is important
    DEFAULT_SCOPE = ['openid', 'email', 'profile']
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token', True),
        ('expires_in', 'expires'),
        ('token_type', 'token_type', True),
        ('picture', 'picture'),
        ('uuid', 'uuid'),
    ]

 
   

    def get_user_details(self, response):
        """Return user details from Google API account"""
        if 'email' in response:
            email = response['email']
        else:
            email = ''

        name, given_name, family_name = (
            response.get('name', ''),
            response.get('given_name', ''),
            response.get('family_name', ''),
        )
        print("""
        {}

        """.format(response))
        for key, value in response.items():
            print(key, value)
        fullname, first_name, last_name = self.get_user_names(
            name, given_name, family_name
        )
        return {'username': email.split('@', 1)[0],
                'email': email,
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name}

   
