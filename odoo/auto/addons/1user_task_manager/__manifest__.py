{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Un módulo creado en forma de practica para aprender Odoo',
    'description': 'Este módulo es creado por el grupo c.',
    'author': 'Grupo C',
    'category': 'Tools',
    'depends': ['base'],  
    'data': [
        #'security/estate_property_security.xml',
        'security/real_estate_res_groups.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],
    'installable': True,
    'application': False,
}