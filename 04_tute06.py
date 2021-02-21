from tkinter import *
from PIL import Image, ImageTk

root =  Tk()

root.geometry('745x444')

root.title("Paritosh's GUI")


# Importent lebal option

# text - adds the text
# bd - background
# fg - foreground
# 1. font=("comicsansms",19, "bold")
# 2. font = "comicsansms 19 bold"
# font - set the font
# padx - x pading
# pady - y pading
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE


title_label = Label(text= '''
Albert Einstein (/ˈaɪnstaɪn/ EYEN-styne;[4] German: [ˈalbɛʁt ˈʔaɪnʃtaɪn]
 (About this soundlisten); 14 March 1879 – 18 April 1955) was a German-born 
 theoretical physicist[5] who developed the theory of relativity, one
  of the two pillars of modern physics (alongside quantum mechanics).
  [3][6] His work is also known for its influence on the philosophy 
  of science.[7][8] He is best known to the general public for his
   mass–energy equivalence formula E = mc2, which has been dubbed
    "the world's most famous equation".[9] He received the 1921
     Nobel Prize in Physics "for his services to theoretical physics
     , and especially for his discovery of the law of the photoelectric
      effect",[10] a pivotal step in the development of quantum theory.

''', bg ='red', fg = "white", padx = 13,
 pady = 44, font = "comicsansms 9 bold",
 borderwidth = 3, relief = SUNKEN
)



# Importent pack option
# anchor = nw 
# side = top, bottom, left, right
# fill
# padx
# pxdy



# title_label.pack(side = BOTTOM, anchor = 'sw', fill=X, fill=Y)
title_label.pack(side = LEFT,  fill=Y, padx=34, pady=34)



root.mainloop()
