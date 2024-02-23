# -*- coding: utf-8 -*-

import os

directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))[:-6]
path = os.path.join(directory, "assets", "account_image.png")

dct = {
    
    "VERSION": 'Runance w1.02.04A',
    
    "admin": {
        "id": '1',
        "login": 'admin',
        "password": 'admin',
        "name": 'bssdka',
        "profile_image": path,
    },

    "user": {
        "id": '2',
        "login": 'userL340',
        "password": 'L340-LAPTOP',
        "name": 'user',
        "profile_image": path,
    },
}
