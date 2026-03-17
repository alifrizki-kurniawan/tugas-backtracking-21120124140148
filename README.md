# tugas-backtracking-21120124140148
Tugas Individu Algoritma Backtracking

# Tugas Individu Algoritma Backtracking: N-Queen Problem

**Nama:** Alif Rizki Kurniawan Hariadi
**NIM:** 21120124140148

## 📝 Deskripsi
Program ini mengimplementasikan algoritma **Backtracking** untuk menyelesaikan permasalahan **N-Queen**. Tujuannya adalah menempatkan N buah bidak ratu pada papan catur berukuran NxN sedemikian rupa sehingga tidak ada dua ratu yang saling menyerang (baris, kolom, maupun diagonal).

Program ini dilengkapi dengan visualisasi sederhana berbasis CLI (Command Line Interface) yang menunjukkan proses penempatan ratu dan proses *backtracking* (mundur) ketika menemui jalan buntu.

## 🛠️ Teknologi
- Bahasa Pemrograman: Python 3
- Library: Standar Library (os, time, sys) - *Tidak perlu instalasi tambahan*

## 🚀 Cara Menjalankan Program
1. Pastikan Python 3 sudah terinstal.
2. Download atau clone repository ini.
3. Jalankan perintah berikut di terminal:
   ```bash
   python n_queen_backtracking.py

## Flowchart
flowchart TD
    Start([Mulai]) --> Input[/Input N: Ukuran Papan/]
    Input --> Init[Inisialisasi Papan NxN dengan 0]
    Init --> CallFunc[Panggil Fungsi Solve col=0]

    subgraph Backtracking ["Proses Backtracking"]
        CallFunc --> CheckCol{Apakah col >= N ?}
        
        CheckCol -- Ya --> Found[Return True: Solusi Ditemukan]
        
        CheckCol -- Tidak --> LoopRow[Loop: Coba Baris i = 0 s/d N-1]
        
        LoopRow --> CheckSafe{Apakah Posisi i, col Aman?}
        
        CheckSafe -- Tidak --> NextRow[Lanjut ke Baris berikutnya]
        
        CheckSafe -- Ya --> PlaceQueen[Letakkan Ratu: board i, col = 1]
        PlaceQueen --> Visual1[Tampilkan Langkah]
        Visual1 --> Recurse[Rekursif: Solve col + 1]
        
        Recurse --> CheckResult{Apakah Return True?}
        
        CheckResult -- Ya --> ReturnTrue[Return True]
        
        CheckResult -- Tidak --> Backtrack[BACKTRACK: board i, col = 0]
        Backtrack --> Visual2[Tampilkan Backtracking]
        Visual2 --> NextRow
        
        NextRow --> CheckLoop{Apakah i < N ?}
        CheckLoop -- Ya --> LoopRow
        CheckLoop -- Tidak --> ReturnFalse[Return False: Gagal]
    end

    Found --> Print[Print Solusi Papan]
    ReturnTrue --> Print
    ReturnFalse --> Print
    Print --> End([Selesai])
