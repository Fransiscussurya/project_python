# Project Python - Kasir Self Service 
## Background
Dalam rangka perbaikan proses bisnis, Andi ingin membuat sistem kasir “self-service” di supermarket miliknya. Salah satu tujuannya adalah agar customer dari luar kota dapat membeli barang di supermarketnya. Secara umum, system kasir pada supermarketnya adalah customer dapat secara mandiri melakukan input belanjaan berupa nama item, jumlah item, dan harga item yang ingin dibeli. Beberapa fitur perlu dikembangkan untuk menyempurnakan system kasir “self-service” ini. Oleh karena itu, Andi meminta tolong Programmer untuk membuat fitur-fitur agar system kasir tersebut berjalan dengan lancar.
## Feature Requirements
- Add item - fitur ini berfungsi untuk customer memasukkan belanjaannya. Parameter yang di-input adalah nama, qty (jumlah), dan harga barang.
- Update item - fitur ini berfungsi untuk mengubah data pesanan yang sudah di-input. Customer dapat mengubah nama item, jumlah item dan harga item yang telah di-input.
- Pembatalan item - Fitur ini berfungsi untuk membatalkan list belanjaan yang sudah di-input. Ada 2 jenis fitur yang dapat dipilih oleh customer.
    - Delete item		: berfungsi untuk membatalkan pesanan yang diinput dengan menghapus nama item (jumlah dan harga item akan otomatis terhapus).
    - Reset transaksi	: berfungsi untuk menghapus semua transaksi/list belanja yang telah di-input.
- Check order - fitur ini berfungsi untuk melakukan final check list belanjaan. Jika tidak ada kesalahan input (missal nama barang kosong atau terdapat angka), total list belanjaan akan ditampilkan. Jika ada kesalahan input, akan memberikan notif “terdapat kesalah input dan customer harus mengubah nama yang salah tersebut.
- Total price - Fitur ini berfungsi untuk menampilkan jumlah total harga belanjaan, diskon yang didapat, dan jumlah harga yang harus dibayarkan setelah dipotong diskon. Ketentuan diskon:
    - Belanjaan 200.000 – 300.000 mendapat diskon 5%.
    - Belanjaan 300.000 – 500.000 mendapat diskon 8%.
    - Belanjaan di atas 500.000 mendapat diskon 10%.
## Flow Chart
Flow chart jalannya proses kasir sesuai fitur yang dibuat dapat dilihat pada gambar di bawah ini
<img width="620" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/a4c68223-1600-4d7a-bba7-99a702a45446">
## Penjelasan Code
- **Script dan Pembuatan Class**

<img width="611" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/69117bf1-e7a2-4e9b-995c-9f4224793d1f">

- **Membuat fungsi add_item**

<img width="618" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/3da17811-05c8-4401-a7f1-b5200f602c67">

- **Membuat fungsi update_item_name**

<img width="446" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/628e468e-cc73-4bcd-a54c-d94523379a6d">

- **Membuat fungsi update_item_qty**

<img width="485" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/edd67aab-959b-4dda-a738-6432f926df70">

- **Membuat fungsi update_item_harga**

<img width="497" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/40722bae-433d-4fc2-b458-879dda49ef94">

- **Membuat fungsi delete_item dan reset_transaksi**

<img width="629" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/3cd231e1-e55f-4d3c-a488-345fb7c33cad">

- **Membuat fungsi check_order**

<img width="589" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/22b5d569-8ac8-4732-9ebf-6fb72951cb2e">

- **Membuat fungsi total_price**

<img width="590" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/950fbe70-4b6e-40c6-a3d2-bd2f9c0b11ac">

## Test Case
Test case dilakukan pada setiap fungsi yang dibuat
- **Test case fungsi add_item**

<img width="620" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/9e190d64-c655-44ba-a981-04ea4f1fcfc5">

- **Test case fungsi update_item_name**

<img width="589" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/bd2ba2c4-4654-45ff-838b-51a98eabd1eb">

- **Test case fungsi update_item_qty dan update_item_harga**

<img width="626" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/12b57341-6773-4e6d-a5a7-6768e100baca">

- **Test case fungsi delete_item dan reset_transaksi**

<img width="541" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/6443e0b3-31f8-4240-a348-20f0d63f8772">

- **Test case fungsi check_order**

<img width="544" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/de93fb4d-6556-4391-b8b1-c5fef2000964">

- **Test case fungsi total_price**

<img width="470" alt="image" src="https://github.com/Fransiscussurya/project_python/assets/143001399/024193cf-8a13-410e-803d-050a9395e4fe">

## Conclusion and Future Work
### Conclusion
Sistem kasir “self-service” dengan beberapa fiturnya telah berhasil dibuat dengan baik. Fitur yang dibuat adalah:
- Add item (nama, qty, harga): untuk memasukkan pesanan yang ingin dibeli.
- Update: item, qty, harga untuk mengubah nama, jumlah dan harga pesanan yang sudah di-input.
- Pembatalan: delete item dan reset transaksi: untuk menghapus 1 atau lebih pesanan yang sudah di-input atau seluruh transaksi.
- Check order: untuk final check pesanan.
- Total price: untuk menampilakan total harga, diskon, dan harga setelah diskon (harga yang harus dibayarkan).
### Future Work
Program dapat dibuat dengan 2 modular code sehingga lebih interaktif.



