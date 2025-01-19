import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gui_setup import setup_gui
from data_processing import load_file, plot_data, update_dropdowns

# GUI Setup
root = tk.Tk()
root.title("Data Insights Explorer")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=10)
style.configure("TLabel", font=("Helvetica", 10), padding=10)
style.configure("TFrame", background="#f0f0f0")

frame, file_label, x_column, y_column, chart_type_var, x_column_dropdown, y_column_dropdown, chart_type_dropdown = setup_gui(root, load_file, plot_data)

# Pass the necessary variables to the data_processing functions
load_file.file_label = file_label
load_file.update_dropdowns = update_dropdowns
plot_data.root = root
plot_data.x_column = x_column
plot_data.y_column = y_column
plot_data.chart_type_var = chart_type_var
update_dropdowns.x_column = x_column
update_dropdowns.y_column = y_column
update_dropdowns.x_column_dropdown = x_column_dropdown
update_dropdowns.y_column_dropdown = y_column_dropdown

root.mainloop()
