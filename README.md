# social_djoser_template

This is a template that shows how to implement google social OAuth2 with [Djoser library][1] (REST implementation of Django Authentication)

## Installation

For advanced users:

```bash
virtualenv venv_social_djoser_boilerplate
cd venv_social_djoser_boilerplate
git clone https://github.com/hvitis/social_djoser_boilerplate
cd social_djoser_boilerplate
pip install -r requirements.txt 
```

## Usage

1. Get OAuth2 keys
```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'YOUR_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY' 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YOUR_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET' 
```

2. Set up your OAuth2 redirect URLs in [google developers console][2]
3. Run the app
```bash
python manage.py migrate
python manage.py runserver
```

## Need Help ? 💁🏻‍♂️💁🏽‍♀️

1. [__Full newbie explanation__][0] on how to connect OAuth2 with django (using django_social) in this template.
2. Check POSTMAN tests in this repo to see how the requests work.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


[0]: https://hvitis.com/django-oauth-social-tutorial-how-to-implement-google-login-with-djoser
[1]: https://djoser.readthedocs.io/en/latest/social_endpoints.html
[2]: https://console.developers.google.com/