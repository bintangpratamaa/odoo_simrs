# ODOO SIMRS ADDONS
Sistem Informasi Rumah Sakit  

## ketentuan
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

## contoh docker compose untuk postgresql
```
services:
  db:
    container_name: devodoo17_postgres16
    image: postgres:16-alpine
    restart: no
    ports:
      - 5432:5432
    volumes:
      - ./varlibpostgresqldata:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=qwertyu
      - POSTGRES_DB=postgres
```

## contoh config
```
[options]
addons_path = .\odoo\addons,.\odoo_simrs
db_password = xxx
db_user = odoo17
db_port = 5432
data_dir = .\data
```

## how to run from source in windows
```
1. install python 3
2. install wkhtmltopdf
3. install visual studio build tools
4. git clone odoo
5. buat virtual env
6. install python package requirement dari python virtual env
7. jalankan odoo dari python virtual env
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