import tkinter as tk
from tkinter import ttk

def setup_gui(root, load_file, plot_data):
    frame = ttk.Frame(root)
    frame.pack(pady=20)

    # Widgets
    file_button = ttk.Button(frame, text="Select CSV File", command=load_file)
    file_button.grid(row=0, column=0, padx=10, pady=10)

    file_label = ttk.Label(frame, text="No file selected.")
    file_label.grid(row=0, column=1, padx=10, pady=10)

    # Dropdowns for column selection and chart type
    x_column = tk.StringVar()
    y_column = tk.StringVar()
    chart_type_var = tk.StringVar()

    x_column_dropdown = ttk.OptionMenu(frame, x_column, "")
    x_column_dropdown.grid(row=1, column=0, padx=10, pady=10)

    y_column_dropdown = ttk.OptionMenu(frame, y_column, "")
    y_column_dropdown.grid(row=1, column=1, padx=10, pady=10)

    chart_type_dropdown = ttk.OptionMenu(frame, chart_type_var, "Line", "Bar", "Scatter")
    chart_type_dropdown.grid(row=1, column=2, padx=10, pady=10)

    plot_button = ttk.Button(frame, text="Plot Data", command=plot_data)
    plot_button.grid(row=2, column=0, columnspan=3, pady=10)

    schema_label = ttk.Label(root, text="")
    schema_label.pack(pady=5)

    row_count_label = ttk.Label(root, text="")
    row_count_label.pack(pady=5)

    preview_label = ttk.Label(root, text="", justify="left")
    preview_label.pack(pady=5)

    return frame, file_label, x_column, y_column, chart_type_var, x_column_dropdown, y_column_dropdown, chart_type_dropdown
