# REG cash power services
REG cash power services provision system

<br>

# API DOC

Endpoint: 127.0.0.1:8000/api/ <br>
headers: { <br>
    &nbsp; &nbsp; "Content-Type": "application/json", <br>
   &nbsp; &nbsp; "Authoriaztion": "Token token" <br>
}

<br>

# # Users 

users/ <br>
Allow [GET, POST]

body: { <br>
    "first_name": "Akm", <br>
    "last_name": "Msc", <br>
    "password": "Password", <br>
    "username": "akm", <br>
    "email": "akm@gmail.com",   <br>
    "id_card_number": null, <br>
    "is_superuser": true, // for only superusers. default is false<br>
    "is_staff": true, // for is allowed to access admin portal <br>
    "is_admin": false, // change to true if s/he is admin <br>
    "groups": [], <br>
    "user_permissions": [], <br>
    "last_login": null <br>
  }


# Single user

/user/{id} <br>
Allowed: [GET, PUT, PATCH, DELETE]

body: { <br>
    "id": 1,
    "first_name": "Akm", <br>
    "last_name": "Msc", <br>
    "password": "Password", <br>
    "username": "akm", <br>
    "email": "akm@gmail.com",   <br>
    "id_card_number": null, <br>
    "is_superuser": true, <br>
    "is_staff": true, <br>
    "is_admin": false, <br>
    "groups": [], <br>
    "user_permissions": [], <br>
    "last_login": null <br>
  }



# Requests

to: requests/ <br>
Allowed requests: [GET, POST]

body: {  <br>
    "client": 2,  <br>
    "requested_service": "Replacement",  <br>
    "province": "west",  <br>
    "district": "KA",  <br>
    "sector": "ru",  <br>
    "cell": "gi",  <br>
    "village": "ki",  <br>
    "street_number": "123",  <br>
    "house_number": "12" <br>
  }

