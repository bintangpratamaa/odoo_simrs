{
    'name': 'SIM RS',
    'author': "UIINET and Friends",
    'website': "https://gpu.co.id",
    'summary': 'Sistem Informasi Rumah Sakit',
    'version': '1.0',
    'application': True,
    'category': 'Productivity',
    'license': 'Other proprietary',
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/sfx_jenis_obat.csv',
        'views/rs_poli_views.xml',
        'views/rs_diagnosa_views.xml',
        'views/rs_grup_diagnosa_views.xml',
        'views/res_partner_pasien_views.xml',
        'views/rs_jenis_bayar_views.xml',
        'views/menus.xml',
    ],

}
