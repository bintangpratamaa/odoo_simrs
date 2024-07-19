# Dev

## Master Data

### rs_obat

```
rs_agama
name, urutan

rs_jenis_kelamin
name, urutan, inacbg_gender, bpjs_gender

rs_goldar
name, urutan

rs_stat_kawin
name, urutan

rs_obat :
name, description, harga_beli, harga_jual, satuan, cacah_yang_dicover_bpjs_per_kunjungan, aturan, kfa_code

rs_partner :
keterangan :
buat field2 tambahan di rs_partner untuk menyimpan data pasien
flag_pasien=true
field :
name, description, address, nomor_rm, kk, nik, kis, no_hp, rs_jenis_kelamin_id, rs_goldar_id, 
tempat_lahir, tanggal_lahir, rs_stat_kawin_id, rs_agama_id, pendidikan, pekerjaan, suku, address_pos, flag_pasien

rs_poli :
name, description, bpjs_ref_poli_kode, bpjs_ref_poli_kode_subspesialis, antrian_dibuka_h_minus, antrian_ditutup_h_minus

rs_prosedur :
name, prosedur_kode

rs_kelas
name, urutan

rs_bed 
name, rs_kelas_id, flag_aktif

```