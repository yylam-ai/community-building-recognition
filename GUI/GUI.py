from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import pickle
import cv2
import numpy as np
from sklearn import svm

root = Tk()
root.title("Community Building Recognition System")
root.resizable(width=True, height=True)

#Open function
def open_file():
    global image_label
    global my_image
    global img_data
    global button_run

    image_label = Label(image="", padx=200, pady=50)
    root.filename = filedialog.askopenfilename(initialdir="GUI/test_dataset",title="Select an Image", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    image = Image.open(root.filename)
    image = image.resize((192, 64))
    my_image = ImageTk.PhotoImage(image)

    #Read image as vector
    with open(root.filename, 'rb') as file:
        img = cv2.imread(root.filename, 0)
        img = cv2.resize(img,(192,64))
        img_data = np.reshape(img, (1, img.shape[0]*img.shape[1]))

    button_run = Button(text='Run', command=run, fg='orange', state=NORMAL)
    image_label = Label(image=my_image, padx=200, pady=50)
  
    image_label.grid(column=0, row=0, columnspan=3)
    button_run.grid(column=1, row=2)


#Run function
def run():
    global prediction_label

  
    #LDA
    with open('building_lda', 'rb') as f:
        lda = pickle.load(f)
            
    lda_img_data = lda.transform(img_data)

    #SVM
    with open('building_svm', 'rb') as i:
        model = pickle.load(i)

    prediction = model.predict(lda_img_data)
    prediction = int(prediction)

    predicted_class=dict([(1,"Fire Station"), (2,"Hospital"), (3,"Police Station")])

    prediction_label = Label(text="This is a " + predicted_class[prediction], padx=100, pady=20, font=("Times", 15))
    prediction_label.grid(column=1, row=1)
   

#Label
image_label = Label(text="Select an Image", padx=200, pady=50, borderwidth=2, relief="solid")
prediction_label = Label(text="",padx=200, pady=20)    

#Button
button_open = Button(text='Open', command=open_file, fg='blue')
button_run = Button(text='Run', command=run, fg='orange', state=DISABLED)
button_exit = Button(text='Exit', command= root.quit, fg="red")

#Position
image_label.grid(column=0, row=0, columnspan=3)
prediction_label.grid(column=1, row=1)
button_open.grid(column=0, row=2)
button_run.grid(column=1, row=2)
button_exit.grid(column=2, row=2)

root.mainloop()