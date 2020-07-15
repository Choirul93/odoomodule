# -*- coding: utf-8 -*-
{
    'name': "ca_hr_attendance",

    'summary': """
       Track employee attendance""",

    'description': """
        Track employee attendance by coordinate and image
    """,

    'author': "choir.arifin@gmail.com",
    'website': "https://choirular.wordpress.com/",
    'category': 'Human Resources',
    'version': '0.1',
    'depends': ['base','hr_attendance'],

    'data': [
        'views/ca_hr_attendance_view.xml'
    ],
    'demo': [
        #'demo/demo.xml',
    ],
}