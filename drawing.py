from swampy.World import World

world = World()

canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150,-100], [150, 100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')
world.mainloop()

c = canvas
r = canvas.rectangle

def draw_rectangle(c, r):
    print draw_rectangle()
