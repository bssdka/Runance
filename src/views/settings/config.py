# -*- coding: utf-8 -*-

import os

directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))[:-6]
path = os.path.join(directory, "assets", "account_image.png")

dct = {
    
    "VERSION": 'Runance w1.02.04A',
    "profile_image": path,
    
    "admin": {
        "id": '1',
        "login": 'admin',
        "password": 'admin',
        "name": 'bssdka',
    },

    "user": {
        "id": '2',
        "login": 'user',
        "password": 'L340-LAPTOP',
        "name": 'user',
    },
}
