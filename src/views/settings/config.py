# -*- coding: utf-8 -*-

import os

directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))[:-6]
path = os.path.join(directory, "assets", "account_image.png")

dct = {
    'login': 'admin',
    'password': 'admin',
    'name': 'bssdka',
    'profile_image': path,
    'user_activated': False,
}
