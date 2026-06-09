# UAS

# PROJECT Implementasi Graph menjadi DSS GOJEK

# Alasan Mengapa Graph Cocok untuk DSS Gojek
Sistem Gojek terdiri dari titik penjemputan (origin), titik pengantaran (destination), dan persimpangan jalan. Hubungan antar lokasi ini memiliki beban (jarak/waktu/biaya). Struktur data linear seperti array atau linked list tidak mampu memetakan jaringan jalan yang bercabang, sehingga Graph adalah struktur data paling ideal.  

# Pemodelan Graph
Node (Vertex): Lokasi atau titik di peta (misal: Kantor, Mall, Perumahan, Restoran).  

Edge: Jalan yang menghubungkan antar lokasi. 

Jenis Graph: Weighted Directed Graph (Berbobot dan Berarah), karena jalanan di dunia nyata memiliki jarak tertentu dan ada sistem jalan satu arah.  

Bobot (Weight): Jarak (km) dan kemacetan (waktu tempuh dalam menit).  


