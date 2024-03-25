import tkinter as tk
import ttkbootstrap as ttk

def converter():
    milha_input = entrada_int.get()
    km_output = milha_input * 1.61
    output_string.set(km_output)

janela = ttk.Window(themename='darkly')
janela.title('Conversor mi → km')
janela.geometry('340x150')

titulo = ttk.Label(master=janela, text='Milhas para Quilômetros', font='Calibri 24 bold')
titulo.pack()

input_frame = ttk.Frame(master=janela)
entrada_int =  tk.IntVar()
entrada = ttk.Entry(master=input_frame, textvariable=entrada_int)
botao = ttk.Button(master=input_frame, text='converter', command=converter)
entrada.pack(side="left", padx=10)
botao.pack(side="left")
input_frame.pack(pady=10)

output_string = tk.StringVar()
output_label = ttk.Label(master=janela, font='Calibri 24', textvariable=output_string)
output_label.pack(pady=5)

janela.mainloop()
