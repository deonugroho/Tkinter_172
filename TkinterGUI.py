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

# 10. Memulai perulangan dan membuat label nama mata pelajaran (kolom 0)
for i, mapel in enumerate(mata_pelajaran):
    lbl = tk.Label(frame_inputs, text=f"Nilai {mapel}:", width=20, anchor="w")
    lbl.grid(row=i, column=0, padx=5, pady=3, sticky="w")
    
    # 11. Membuat field entry input nilai, memasangnya pada grid (kolom 1), dan menyimpannya ke list
    entry = tk.Entry(frame_inputs, width=15)
    entry.grid(row=i, column=1, padx=5, pady=3)
    entries.append(entry)

# 12. Mendefinisikan fungsi logika untuk menampilkan hasil prediksi
def prediksi_prodi():
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")
