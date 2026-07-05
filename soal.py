def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    # Get user input and check if it matches the correct option
    answer = input("Pilih jawaban yang benar (1/2/3/4): ")
    if answer.isdigit() and int(answer) == correct_option:
        print("Jawaban Anda benar!\n")
        return True
    else:
        print("Jawaban Anda salah.\n")
        return False

def main():
    # List of questions with their options and the correct answer index
    questions = [
        {
            "question": "Apa fungsi utama dari DNS (Domain Name System)?",
            "options": ["Mengubah alamat IP menjadi nama domain",
                        "Mengubah nama domain menjadi alamat IP",
                        "Mengatur kebijakan keamanan jaringan",
                        "Memindai port terbuka pada jaringan"],
            "correct_option": 2
        },
        {
            "question": "Perintah Nmap apa yang digunakan untuk melakukan pemindaian port secara default?",
            "options": ["nmap -sP", "nmap -sS", "nmap -sV", "nmap -A"],
            "correct_option": 2
        },
        {
            "question": "Perintah `nslookup` digunakan untuk:",
            "options": ["Melakukan traceroute pada jaringan",
                        "Melakukan lookup DNS untuk mendapatkan alamat IP dari domain",
                        "Melakukan scan port pada jaringan lokal",
                        "Mengubah nama host menjadi alamat MAC"],
            "correct_option": 2
        },
        {
            "question": "Apa keuntungan utama menggunakan DNS over HTTPS (DoH)?",
            "options": ["Meningkatkan kecepatan internet",
                        "Mengamankan pencarian DNS dari pengintaian pihak ketiga",
                        "Mengurangi latensi jaringan",
                        "Mempercepat pemindaian port"],
            "correct_option": 2
        },
        {
            "question": "Apa yang dikelola oleh Layer 4 pada model OSI?",
            "options": ["Routing paket di seluruh jaringan",
                        "Pengiriman dan penerimaan data antara perangkat melalui protokol transport",
                        "Enkripsi dan dekripsi data",
                        "Manajemen sesi komunikasi antara aplikasi"],
            "correct_option": 2
        },
        {
            "question": "Layer 7 pada model OSI dikenal sebagai:",
            "options": ["Network Layer", "Data Link Layer", "Transport Layer", "Application Layer"],
            "correct_option": 4
        },
        {
            "question": "Tahap pertama dalam proses Three-Way Handshake pada protokol TCP adalah:",
            "options": ["FIN", "SYN", "ACK", "PSH"],
            "correct_option": 2
        },
        {
            "question": "Query Shodan yang digunakan untuk mencari server web dengan port 80 yang terbuka adalah:",
            "options": ["port:22", "port:80", "ip:80", "ssl:80"],
            "correct_option": 2
        },
        {
            "question": "Perintah apa yang digunakan untuk berpindah direktori di Linux?",
            "options": ["ls", "cd", "mv", "pwd"],
            "correct_option": 2
        },
        {
            "question": "Apa singkatan dari DNS?",
            "options": ["Domain Name System", "Data Network Service", 
                        "Dynamic Network Service", "Domain Network System"],
            "correct_option": 1
        },
        # ===== INTERNET & NETWORKING BASIC (10 Soal) =====
        {
            "question": "Protokol apa yang digunakan untuk mengirim halaman web dari server ke browser?",
            "options": ["FTP", "SMTP", "HTTP/HTTPS", "SNMP"],
            "correct_option": 3
        },
        {
            "question": "Apa alamat IP yang digunakan untuk merujuk pada localhost?",
            "options": ["192.168.1.1", "10.0.0.1", "127.0.0.1", "0.0.0.0"],
            "correct_option": 3
        },
        {
            "question": "Fungsi utama dari router dalam jaringan adalah:",
            "options": ["Menghubungkan perangkat dalam satu jaringan lokal",
                        "Meneruskan paket data antar jaringan yang berbeda",
                        "Menyediakan koneksi internet nirkabel",
                        "Mengamankan jaringan dari serangan luar"],
            "correct_option": 2
        },
        {
            "question": "Protokol mana yang bersifat connection-oriented dan menjamin pengiriman data?",
            "options": ["UDP", "TCP", "IP", "ICMP"],
            "correct_option": 2
        },
        {
            "question": "Apa fungsi dari subnet mask?",
            "options": ["Menyembunyikan alamat IP perangkat",
                        "Menentukan bagian network dan host dari alamat IP",
                        "Mengenkripsi data yang dikirim melalui jaringan",
                        "Mengubah alamat IP menjadi alamat MAC"],
            "correct_option": 2
        },
        {
            "question": "Perintah `ping` digunakan untuk:",
            "options": ["Memindai port terbuka pada host",
                        "Menguji konektivitas antar perangkat dalam jaringan",
                        "Melacak rute paket ke host tujuan",
                        "Melihat konfigurasi IP perangkat"],
            "correct_option": 2
        },
        {
            "question": "Apa fungsi dari DHCP dalam jaringan?",
            "options": ["Mengamankan koneksi jaringan",
                        "Memberikan alamat IP secara otomatis ke perangkat",
                        "Mencatat semua aktivitas jaringan",
                        "Mempercepat transfer data"],
            "correct_option": 2
        },
        {
            "question": "Perbedaan utama antara IPv4 dan IPv6 adalah:",
            "options": ["IPv4 lebih cepat dari IPv6",
                        "IPv6 menggunakan alamat 128-bit sedangkan IPv4 32-bit",
                        "IPv6 hanya digunakan untuk jaringan lokal",
                        "IPv4 lebih aman dari IPv6"],
            "correct_option": 2
        },
        {
            "question": "Apa yang dimaksud dengan latency dalam jaringan?",
            "options": ["Jumlah data yang dapat ditransfer per detik",
                        "Waktu yang dibutuhkan data untuk berpindah dari sumber ke tujuan",
                        "Jumlah perangkat yang terhubung dalam jaringan",
                        "Tingkat keamanan koneksi jaringan"],
            "correct_option": 2
        },
        {
            "question": "Protokol UDP biasanya digunakan untuk aplikasi yang membutuhkan:",
            "options": ["Pengiriman data yang terjamin dan terurut",
                        "Kecepatan tinggi dan toleransi terhadap kehilangan data",
                        "Koneksi yang aman dan terenkripsi",
                        "Koneksi dua arah yang stabil"],
            "correct_option": 2
        },
        # ===== SECURITY FUNDAMENTALS (10 Soal) =====
        {
            "question": "Apa kepanjangan dari CIA dalam keamanan informasi?",
            "options": ["Confidentiality, Integrity, Availability",
                        "Control, Integration, Authentication",
                        "Cryptography, Identity, Access",
                        "Confidentiality, Internet, Application"],
            "correct_option": 1
        },
        {
            "question": "Jenis serangan yang memanfaatkan input dari pengguna untuk mengeksekusi perintah SQL berbahaya disebut:",
            "options": ["Cross-Site Scripting (XSS)", "SQL Injection", "CSRF", "Man-in-the-Middle"],
            "correct_option": 2
        },
        {
            "question": "Fungsi utama dari firewall adalah:",
            "options": ["Mempercepat koneksi internet",
                        "Mencegah akses tidak sah ke jaringan",
                        "Mengubah alamat IP perangkat",
                        "Menyediakan layanan DNS"],
            "correct_option": 2
        },
        {
            "question": "Apa perbedaan antara enkripsi simetris dan asimetris?",
            "options": ["Simetris lebih lambat dari asimetris",
                        "Simetris menggunakan satu kunci, asimetris menggunakan pasangan kunci publik dan privat",
                        "Asimetris lebih mudah diimplementasikan",
                        "Tidak ada perbedaan yang signifikan"],
            "correct_option": 2
        },
        {
            "question": "Serangan Cross-Site Scripting (XSS) bertujuan untuk:",
            "options": ["Mendapatkan akses ke database server",
                        "Menyisipkan script berbahaya ke halaman web yang dilihat pengguna lain",
                        "Membanjiri server dengan traffic palsu",
                        "Menebak kata sandi pengguna"],
            "correct_option": 2
        },
        {
            "question": "Apa yang dimaksud dengan hashing dalam keamanan?",
            "options": ["Proses mengenkripsi data agar bisa didekripsi kembali",
                        "Proses mengubah data menjadi string tetap yang tidak dapat dibalik",
                        "Proses mengompresi data untuk mempercepat transfer",
                        "Proses memvalidasi sertifikat digital"],
            "correct_option": 2
        },
        {
            "question": "Prinsip 'least privilege' dalam keamanan berarti:",
            "options": ["Semua pengguna memiliki hak akses yang sama",
                        "Pengguna hanya diberikan akses minimum yang diperlukan untuk tugasnya",
                        "Hanya administrator yang boleh mengakses sistem",
                        "Semua data harus dienkripsi"],
            "correct_option": 2
        },
        {
            "question": "Serangan Man-in-the-Middle (MitM) terjadi ketika:",
            "options": ["Server menerima terlalu banyak permintaan",
                        "Penyerang diam-diam menyadap dan memanipulasi komunikasi antara dua pihak",
                        "Pengguna kehilangan koneksi internet",
                        "Virus menginfeksi sistem operasi"],
            "correct_option": 2
        },
        {
            "question": "Apa tujuan dari autentikasi multi-faktor (MFA)?",
            "options": ["Mempermudah proses login pengguna",
                        "Menambahkan lapisan keamanan ekstra dengan memverifikasi beberapa bukti identitas",
                        "Mengganti kata sandi dengan biometrik",
                        "Mempercepat akses ke sistem"],
            "correct_option": 2
        },
        {
            "question": "Jenis serangan yang memanfaatkan session pengguna yang sah untuk melakukan tindakan tidak sah disebut:",
            "options": ["Cross-Site Scripting (XSS)", "SQL Injection", "Cross-Site Request Forgery (CSRF)", "Brute Force"],
            "correct_option": 3
        },
        # ===== WEB BASIC (10 Soal) =====
        {
            "question": "Apa fungsi utama dari HTML dalam pengembangan web?",
            "options": ["Mengatur tampilan visual halaman web",
                        "Mendefinisikan struktur dan konten halaman web",
                        "Menangani logika sisi server",
                        "Mengelola database website"],
            "correct_option": 2
        },
        {
            "question": "HTTP method apa yang digunakan untuk mengirim data ke server (misalnya saat mengisi form)?",
            "options": ["GET", "POST", "PUT", "DELETE"],
            "correct_option": 2
        },
        {
            "question": "Apa arti dari HTTP status code 404?",
            "options": ["Internal Server Error", "Not Found", "Forbidden", "OK"],
            "correct_option": 2
        },
        {
            "question": "Perbedaan utama antara cookie dan session adalah:",
            "options": ["Cookie disimpan di server, session disimpan di client",
                        "Cookie disimpan di client, session disimpan di server",
                        "Cookie dan session sama-sama disimpan di server",
                        "Cookie bersifat sementara, session bersifat permanen"],
            "correct_option": 2
        },
        {
            "question": "Apa fungsi dari CSS dalam pengembangan web?",
            "options": ["Menambahkan interaktivitas ke halaman web",
                        "Mendefinisikan struktur halaman web",
                        "Mengatur tampilan dan layout halaman web",
                        "Mengelola data pengguna"],
            "correct_option": 3
        },
        {
            "question": "Apa yang dimaksud dengan DOM (Document Object Model)?",
            "options": ["Database yang digunakan oleh website",
                        "Representasi terstruktur dari dokumen HTML yang dapat dimanipulasi oleh JavaScript",
                        "Protokol untuk mengirim data antar server",
                        "Framework untuk membangun aplikasi web"],
            "correct_option": 2
        },
        {
            "question": "Arsitektur REST API umumnya menggunakan format data:",
            "options": ["CSV", "XML dan JSON", "Binary", "Markdown"],
            "correct_option": 2
        },
        {
            "question": "Apa peran dari web server (seperti Apache atau Nginx)?",
            "options": ["Menampilkan halaman web di browser pengguna",
                        "Menerima permintaan HTTP dan mengirimkan konten web yang diminta",
                        "Mengelola database website",
                        "Mendesain tampilan antarmuka pengguna"],
            "correct_option": 2
        },
        {
            "question": "HTTP status code 500 menunjukkan:",
            "options": ["Halaman tidak ditemukan", "Permintaan berhasil diproses", "Terjadi kesalahan pada server", "Akses ditolak"],
            "correct_option": 3
        },
        {
            "question": "Apa yang dimaksud dengan client-server architecture?",
            "options": ["Arsitektur di mana semua perangkat berfungsi sebagai server",
                        "Model di mana client meminta layanan dan server menyediakan layanan tersebut",
                        "Arsitektur di mana tidak ada perangkat pusat",
                        "Model yang hanya digunakan untuk website statis"],
            "correct_option": 2
        },
    ]
    
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            score += 1
    
    print(f"Skor akhir Anda: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
