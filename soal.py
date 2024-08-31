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
    ]
    
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            score += 1
    
    print(f"Skor akhir Anda: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
