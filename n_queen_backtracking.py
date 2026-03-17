import os
import time
import sys

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk mencetak papan catur ke layar
def print_board(board, n, current_row=-1, current_col=-1, action=""):
    clear_screen()
    print(f"=== N-Queen Problem (Ukuran Papan: {n}x{n}) ===")
    print(f"Langkah: {action}\n")
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                # Tandai Ratu dengan 'Q'
                print(" Q ", end="")
            else:
                # Tandai kotak kosong
                print(" . ", end="")
        print() # Newline setiap baris
    print("\nKeterangan:")
    print("Q = Ratu (Queen)")
    print(". = Kotak Kosong")
    print("\nTekan Ctrl+C untuk menghentikan proses otomatis.")
    time.sleep(0.8) # Jeda agar proses terlihat (visualisasi)

# Fungsi untuk memeriksa apakah ratu aman ditempatkan di board[row][col]
def is_safe(board, row, col, n):
    # Cek baris horizontal di sebelah kiri
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Cek diagonal atas kiri
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Cek diagonal bawah kiri
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Fungsi utama backtracking
def solve_nq_util(board, col, n):
    # Base Case: Jika semua ratu sudah ditempatkan
    if col >= n:
        return True

    # Coba tempatkan ratu di setiap baris satu per satu (incremental)
    for i in range(n):
        # Visualisasi mencoba menempatkan
        # Kita tidak mengubah papan utama dulu, tapi bisa ditampilkan di log jika perlu
        
        if is_safe(board, i, col, n):
            # Jika aman, tempatkan ratu
            board[i][col] = 1
            print_board(board, n, i, col, f"Menempatkan Ratu di Baris {i+1}, Kolom {col+1}")

            # Rekursif untuk menempatkan ratu di kolom selanjutnya
            if solve_nq_util(board, col + 1, n):
                return True

            # Jika menempatkan ratu di kolom selanjutnya tidak menghasilkan solusi,
            # maka BACKTRACK (hapus ratu)
            board[i][col] = 0
            print_board(board, n, i, col, f"BACKTRACK! Hapus Ratu di Baris {i+1}, Kolom {col+1}")

    return False

# Fungsi wrapper
def solve_nq(n):
    # Inisialisasi papan 0 (kosong)
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    clear_screen()
    print("Memulai proses pencarian solusi...")
    time.sleep(1)

    if not solve_nq_util(board, 0, n):
        print("Solusi tidak ditemukan")
        return False

    print_board(board, n, action="SOLUSI DITEMUKAN!")
    return True

# Main Program
if __name__ == "__main__":
    try:
        n_input = int(input("Masukkan ukuran papan catur (N): "))
        if n_input < 1:
            print("Ukuran harus lebih dari 0")
        else:
            solve_nq(n_input)
    except ValueError:
        print("Input harus berupa angka!")