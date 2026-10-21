# 1. Meng-import module tkinter
import tkinter as tk

# 2. Inisialisasi window utama (root)
root = tk.Tk()

# 3. Mengatur judul jendela aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan")

# 4. Mengatur dimensi ukuran window
root.geometry("400x520")

# 5. Mengunci ukuran window agar tidak bisa di-resize
root.resizable(False, False)

# 6. Menambahkan label judul utama di bagian atas
label_judul = tk.Label(
    root, 
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Arial", 14, "bold")
)
label_judul.pack(pady=10)

# 7. Membuat kontainer (Frame) untuk mengelompokkan form input
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=5)

# 8. Mendefinisikan list daftar 10 mata pelajaran
mata_pelajaran = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sosiologi", "Geografi", "Sejarah"
]

# 9. Menginisialisasi list kosong untuk menampung widget entry
entries = []
