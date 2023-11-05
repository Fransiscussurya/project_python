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





