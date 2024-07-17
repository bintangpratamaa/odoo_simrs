{
    'name': 'SIM RS',
    'author': "UIINET and Friends",
    'website': "https://gpu.co.id",
    'summary': 'Sistem Informasi Rumah Sakit',
    'version': '1.0',
    'application': True,
    'category': 'Productivity',
    'license': 'Other',
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/sfx_jenis_obat.csv',
        'views/rs_poli_views.xml',
        #'views/sf_solvent_views.xml',
        #'views/sf_drug_views.xml',
        #'views/sf_drug_bud_views.xml',
        'views/menus.xml',
    ],

}