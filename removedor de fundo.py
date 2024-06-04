from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def remove_background(input_path, output_path):
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        messagebox.showinfo("Sucesso", f"Imagem salva em: {output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao remover fundo: {e}")

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    return file_path

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    return file_path

def process_image():
    input_path = select_input_file()
    if not input_path:
        return

    output_path = select_output_file()
    if not output_path:
        return

    remove_background(input_path, output_path)

# Configuração da janela principal
root = tk.Tk()
root.title("Removedor de Fundo de Imagens")

tk.Button(root, text="Selecionar Imagem e Remover Fundo", command=process_image).pack(pady=20)

root.mainloop()
