
import random
ran = random.randrange(350)

# reproductor de musica tiene que tener instalado el reproducctor vlc
# import vlc
# p = vlc.MediaPlayer("music.mp3")
# p.play()
# p.stop()
from tkinter import*
tk =Tk()
posx=350
canvas =Canvas(tk,width=500,height=500)

def movertri(event):
    global posx
    if event.keysym == 'Up':
        canvas.move(3,0,-3)
    elif event.keysym == 'Down':
        canvas.move(3,0,3)
    elif event.keysym == 'Left':
        canvas.move(3,-3,0)
        posx = posx - 3
        if posx <= 50:
            text = canvas.create_text(80, 40, text=('GOLLLLL'), fill="red", font=("Helvectica", "16"))
            print('GOLLLL')
        print(posx)
    else:
        canvas.move(3,3,0)
        posx = posx + 3
        print(posx)

# canvas.bind_all('<KeyPress-Up>', movertri)
# canvas.bind_all('<KeyPress-Down>', movertri)
canvas.bind_all('<KeyPress-Left>', movertri)
canvas.bind_all('<KeyPress-Right>', movertri)
canvas.pack()
my_image1 =PhotoImage(file="ima3.gif")
canvas.create_image(0,0,ancho =NW,image= my_image1)
my_image2 =PhotoImage(file="ima1.gif")
canvas.create_image(0,0,ancho =NW,image= my_image2)
my_image3 =PhotoImage(file="ima2.gif")
canvas.create_image(350,50,ancho =NW,image= my_image3)
tk.mainloop()
