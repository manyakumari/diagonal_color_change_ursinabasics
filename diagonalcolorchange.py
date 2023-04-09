from ursina import *

app = Ursina()

box1 = Entity(model = 'cube', scale = (2,2,2), position = (0,0,0), color = color.white)
def moveupr():
    box1.y += 50 *time.dt
    box1.x +=50 *time.dt
    box1.color = color.rgb(255,102,102)
def movedownr():
    box1.y -= 50 *time.dt
    box1.x+=50*time.dt
    box1.color = color.rgb(255,255,153)
def moveupl():
    box1.x-=50 *time.dt
    box1.y+=50*time.dt
    box1.color = color.rgb(0,204,102)
def movedownl():
    box1.x-=50 *time.dt
    box1.y-=50*time.dt
    box1.color = color.rgb(51,153,255)
    

buttonupr = Button(parent = scene, model = 'cube', scale = (1,1,1), color = color.red, on_click = moveupr, position = (2,2,0))
buttondownr = Button(parent = scene, model = 'cube', scale = (1,1,1), color = color.yellow, on_click = movedownr, position = (2,-2,0))
buttonupl = Button(parent = scene, model = 'cube', scale = (1,1,1), color = color.green, on_click = moveupl, position = (-2,2,0))
buttondownl = Button(parent = scene, model = 'cube', scale = (1,1,1), color = color.blue, on_click = movedownl, position = (-2,-2,0))


app.run()