from tkinter import filedialog, messagebox, _setit
import tkinter as tk
from pyspark.sql import SparkSession
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        load_file.file_label.config(text=f"File Selected: {file_path}")
        global file
        file = file_path
        load_file.update_dropdowns()

def plot_data():
    try:
        x_col = plot_data.x_column.get()
        y_col = plot_data.y_column.get()
        chart_type = plot_data.chart_type_var.get()
        
        if not x_col or not y_col or not chart_type:
            messagebox.showerror("Error", "Please select both X and Y columns and a chart type.")
            return
        
        spark = SparkSession.builder.appName("DataInsightsExplorer").getOrCreate()
        df = spark.read.csv(file, header=True, inferSchema=True)
        pandas_df = df.toPandas()
        
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        
        if chart_type == "Line":
            pandas_df.plot(kind='line', x=x_col, y=y_col, ax=ax)
        elif chart_type == "Bar":
            pandas_df.plot(kind='bar', x=x_col, y=y_col, ax=ax)
        elif chart_type == "Scatter":
            pandas_df.plot(kind='scatter', x=x_col, y=y_col, ax=ax)
        
        # Clear previous plot
        for widget in plot_data.root.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
        
        canvas = FigureCanvasTkAgg(fig, master=plot_data.root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_dropdowns():
    try:
        spark = SparkSession.builder.appName("DataInsightsExplorer").getOrCreate()
        df = spark.read.csv(file, header=True, inferSchema=True)
        columns = df.columns
        
        update_dropdowns.x_column.set('')
        update_dropdowns.y_column.set('')
        
        update_dropdowns.x_column_dropdown['menu'].delete(0, 'end')
        update_dropdowns.y_column_dropdown['menu'].delete(0, 'end')
        
        for col in columns:
            update_dropdowns.x_column_dropdown['menu'].add_command(label=col, command=tk._setit(update_dropdowns.x_column, col))
            update_dropdowns.y_column_dropdown['menu'].add_command(label=col, command=tk._setit(update_dropdowns.y_column, col))
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
