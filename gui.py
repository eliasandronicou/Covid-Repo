import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from main import *



# δημιουργεία window
window = tk.Tk()
window.title('Menu')

image = Image.open("covid.jpg")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.pack()

title_label = tk.Label(window, text='Choose Graphs', font=('Arial', 16, 'bold'))
title_label.pack()

# δημιουργεία buttons

button1 = tk.Button(window, text='Months', command=lambda: plot_two_graphs(monthly_sum_b, monthly_sum_a, 'Month'))
button1.pack()

button2 = tk.Button(window, text='Countries', command=lambda: plot_two_graphs(country_sum_b, country_sum_a, 'Country'))
button2.pack()

button3 = tk.Button(window, text='Transport', command=lambda: plot_two_graphs(transport_sum_b, transport_sum_a, 'Transport_Mode'))
button3.pack()

button4 = tk.Button(window, text='Weekday', command=lambda: plot_two_graphs(weekday_sum_b, weekday_sum_a, 'Weekday'))
button4.pack()

button5 = tk.Button(window, text='Commodities', command=lambda: plot_two_graphs(commodity_sum_b, commodity_sum_a, 'Commodity'))
button5.pack()

button6 = tk.Button(window, text='Top 5 Months', command=lambda: plot_two_graphs(er_6_b, er_6_a, 'Month'))
button6.pack()

button7 = tk.Button(window, text='Top 5 Commodities per Country', command=lambda: plot_top_5_per_country(top_5_per_country_b,top_5_per_country_a))
button7.pack()

button8 = tk.Button(window, text='Top Day', command=lambda: plot_best_day_commodity(best_day_b, best_day_a))
button8.pack()

window.mainloop()
