
from scipy.stats import norm
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk

root =tk.Tk()
#root.configure(bg=  '00fa2b')

image = Image.open("chuki.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()
label.place(x=0, y=0, relwidth=1, relheight=1)

root.resizable(False, False) 
img = tk.PhotoImage(file = 'iconoCETI.png')
root.iconphoto(False, img)
root.title('Doggy analysis')

window_height = 600
window_width = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def graphAgesDog():
    #doggy_info = pd.read_csv('testDoggyInfo.csv')

    doggy_info = pd.read_csv('data_13feb_perros.csv')
    x = np.array(doggy_info['edad'])

    # Calculate the mean and standard deviation for each variable
    x_mean, x_std = np.mean(x), np.std(x)

    # Define the x and y values for the normal distribution curves
    x_values = np.linspace(x_mean - 3*x_std, x_mean + 3*x_std, 100)

    # Calculate the probability density functions for the normal distribution curves
    x_pdf = norm.pdf(x_values, loc=x_mean, scale=x_std)

    # Create a bar histogram with normal distribution curves
    fig, ax = plt.subplots()
    ax.hist(x, alpha=0.5, label='Ages frecuency', bins=20, density=True)
    ax.plot(x_values, x_pdf, 'r', label='Ages distribuition')
    ax.legend()

    # Add titles and axis labels to the figure
    ax.set_title('Bar Histogram with Normal Distribution Curves')
    ax.set_xlabel('Ages Dog')
    ax.set_ylabel('Frequency normilized')

    # Show the figure
    plt.show()


def graphRacesDog():
    # Load data from CSV file
    #data = pd.read_csv("testDoggyInfo.csv")

    data = pd.read_csv("data_13feb_perros.csv")

    # Get the dog races and their frequencies
    races, counts = np.unique(data["raza"], return_counts=True)

    # Create a bar plot
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.bar(races, counts)

    # Set the plot title and labels
    ax.set_title("Dog Races")
    ax.set_xlabel("Race Dog")
    ax.set_ylabel("Counting")

    # Display the plot
    plt.show()


buttonAgesDogs = tk.Button(root, text = "Dog ages information", command=graphAgesDog, font=('Arial', 16))
buttonAgesDogs.config(fg='blue', bg='white')
buttonAgesDogs.config(bd=2)
buttonAgesDogs.pack(padx=10, pady=2)

buttonRacesDogs = tk.Button(root, text = "Dog races information", command=graphRacesDog, font=('Arial', 16))
buttonRacesDogs.config(fg='blue', bg='white')
buttonRacesDogs.config(bd=2)
buttonRacesDogs.pack(padx=10, pady=2)

root.mainloop()

