# ODOO SIMRS ADDONS
Sistem Informasi Rumah Sakit  

## qa
```
1. gunakan odoo versi 17.0
2. setiap tabel/model dikasih prefix rs_
3. ...
```

## todo
```
master data
- rs_poli
- rs_obat
- rs_pasien
```

## note
```
#create virtual env
python -m venv vxz

#update pip on windows
.\vxz\Scripts\python.exe -m pip install --upgrade pip

#install requirement on windows
.\vxz\Scripts\pip.exe install -r .\odoo\requirements.txt

#first time install
.\vxz\Scripts\python.exe .\odoo\odoo-bin -c .\konfig_rs.conf -d sf01 -i rs --stop-after-init

#run and update
.\vxz\Scripts\python.exe .\odoo\odoo-bin -c .\konfig_rs.conf -u rs --dev all

```