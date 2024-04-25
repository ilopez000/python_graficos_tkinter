import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Crear ventana principal de Tkinter
root = tk.Tk()
root.title("Gráfico de Ventas con Datos")

# Crear un Frame para el Treeview
frame_tree = tk.Frame(root)
frame_tree.pack(pady=10)

# Crear Treeview para mostrar datos
tree = ttk.Treeview(frame_tree, columns=("Producto", "Ventas"), show="headings")
tree.heading("Producto", text="Producto")
tree.heading("Ventas", text="Ventas")
tree.pack()

# Insertar datos de ejemplo en el Treeview
productos = ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E", "Producto F"]
ventas = [100, 150, 200, 120, 180, 250]

# Insertar los datos en el Treeview
for prod, venta in zip(productos, ventas):
    tree.insert("", "end", values=(prod, venta))

# Crear un Frame para el gráfico de tarta
frame_pie = tk.Frame(root)
frame_pie.pack(pady=10)

# Crear el gráfico de tarta
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(ventas, labels=productos, autopct='%1.1f%%')
ax_pie.set_title("Distribución de Ventas")

# Integrar el gráfico de tarta en Tkinter
canvas_pie = FigureCanvasTkAgg(fig_pie, master=frame_pie)
canvas_pie.get_tk_widget().pack()

# Crear un Frame para el gráfico de líneas
frame_line = tk.Frame(root)
frame_line.pack(pady=10)

# Crear el gráfico de líneas
fig_line, ax_line = plt.subplots()
ax_line.plot(productos, ventas, '-o', color='b', label='Ventas')
ax_line.set_title("Ventas por Producto")
ax_line.set_xlabel("Producto")
ax_line.set_ylabel("Ventas")
ax_line.legend()

# Integrar el gráfico de líneas en Tkinter
canvas_line = FigureCanvasTkAgg(fig_line, master=frame_line)
canvas_line.get_tk_widget().pack()

# Iniciar el bucle de Tkinter
root.mainloop()
