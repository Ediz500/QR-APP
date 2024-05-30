import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk
from qrcode_generator import generate_qr_code

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x500")

        self.data_label = tk.Label(root, text="Enter data:")
        self.data_label.pack()
        self.data_entry = tk.Entry(root)
        self.data_entry.pack()

        self.file_label = tk.Label(root, text="Enter file name to save:")
        self.file_label.pack()
        self.file_entry = tk.Entry(root)
        self.file_entry.pack()

        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()

        self.qr_code_label = tk.Label(root)
        self.qr_code_label.pack()

    def generate_qr_code(self):
        data = self.data_entry.get()
        file_name = self.file_entry.get()

        try:
            file_path = generate_qr_code(data, file_name)
            img = ImageTk.PhotoImage(file=file_path)
            self.qr_code_label.configure(image=img)
            self.qr_code_label.image = img
            messagebox.showinfo("QR Code Generated", f"{file_name} file created successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
