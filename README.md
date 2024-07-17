# ODOO SIMRS ADDONS
Sistem Informasi Rumah Sakit

## note
```
#create virtual env
python -m venv vxz

#update pip on windows
.\vxz\Scripts\python.exe -m pip install --upgrade pip

#install requirement on windows
.\vxz\Scripts\pip.exe install -r .\odoo\requirements.txt

#run
.\vxz\Scripts\python.exe .\odoo\odoo-bin -c .\konfig_rs.conf -u rs --dev all

#install
.\vxz\Scripts\python.exe .\odoo\odoo-bin -c .\konfig_rs.conf -d sf01 -i rs --stop-after-init

```