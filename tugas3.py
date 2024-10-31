import numpy as np
import imageio
import matplotlib.pyplot as plt

# Path ke file gambar
file_path = "C:\\Users\\muham\\Documents\\TUGAS KULIAH SEMESTER 5\\Pengolahan Citra Digital\\kampus.jpg"

try:
    # Membaca gambar
    image = imageio.imread(file_path)

    # Mengubah gambar menjadi grayscale
    grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

    # Menghitung histogram
    histogram, bin_edges = np.histogram(grayscale_image, bins=256, range=(0, 255))

    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.title("Histogram Gambar Grayscale")
    plt.xlabel("Intensitas Piksel")
    plt.ylabel("Jumlah Piksel")
    plt.xlim([0, 255])
    plt.plot(bin_edges[0:-1], histogram, color='black')
    plt.show()

except FileNotFoundError:
    print("Program gagal memuat file gambar dari path yang diberikan. Pastikan path yang digunakan benar dan file 'kampus.jpg' berada di lokasi tersebut.")
    print("Jika benar, coba cek kembali path apakah terdapat kesalahan ketik, seperti nama folder, dan pastikan ada backslash ganda (\\) atau tambahkan prefiks r pada string path untuk memastikan pembacaan dengan benar.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
