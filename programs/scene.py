import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    # tree_center = scene_left + 500
    # tree_top = scene_top + 100
    # tree_height = 150
    # draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_sky(canvas, 0, 0)
    draw_cloud(canvas, 600, 70)
    draw_cloud(canvas, 300, 25)
    draw_cloud(canvas, 50, 60)
    draw_ground(canvas, 0, 300)
    draw_hay_bale(canvas, 400, 350)
    # draw_hay_bale(canvas, 400, 350)
    draw_hay_bale(canvas, 367, 435)
    draw_hay_bale(canvas, 600, 335)
    draw_hay_bale(canvas, 100, 435)
    draw_hay_bale(canvas, 100, 315)
    draw_picket(canvas, 50, 275)
    draw_picket(canvas, 100, 275)
    draw_picket(canvas, 150, 275)
    draw_picket(canvas, 200, 275)
    draw_picket(canvas, 250, 275)
    draw_picket(canvas, 300, 275)
    draw_picket(canvas, 350, 275)
    draw_picket(canvas, 400, 275)
    draw_picket(canvas, 450, 275)
    draw_picket(canvas, 500, 275)
    draw_picket(canvas, 550, 275)
    draw_picket(canvas, 600, 275)
    draw_picket(canvas, 650, 275)
    draw_picket(canvas, 700, 275)
    draw_picket(canvas, 750, 275)
    draw_wire(canvas, scene_left, scene_top, scene_right, scene_bottom,)
    # draw_grass(canvas, 0, 300, 15)

    

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_cloud(canvas, cloud_left, cloud_top):
    cloud_width = 100
    cloud_height = 100

    cloud_right = cloud_left + cloud_width + 100
    cloud_bottom = cloud_top + cloud_height

    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill='azure3', width=False)

def draw_sky(canvas, sky_left, sky_top):
    sky_width = 800 
    sky_height = 100
    sky_right = sky_left + sky_width
    sky_bottom = sky_top + sky_height

    canvas.create_rectangle(sky_left, sky_top, sky_right, sky_bottom, fill='skyblue2', width=False)

def draw_ground(canvas, ground_left, ground_top):
    ground_width = 800
    ground_heigth = 200
    ground_right = ground_left + ground_width
    ground_bottom = ground_top + ground_heigth

    canvas.create_rectangle(ground_left, ground_top, ground_right, ground_bottom, fill='burlywood4', width=False)

def draw_hay_bale(canvas, hay_bale_left, hay_bale_top):
    hay_bale_width = 75
    hay_bale_height = 50
    hay_bale_right = hay_bale_left + hay_bale_width
    hay_bale_bottom = hay_bale_top + hay_bale_height
    
    canvas.create_rectangle(hay_bale_left, hay_bale_top, hay_bale_right, hay_bale_bottom, fill='yellow2', width=True)

def draw_picket(canvas, picket_left, picket_top):
    picket_width = 10
    picket_height = 35
    picket_rigth = picket_left + picket_width
    picket_bottom = picket_top + picket_height

    canvas.create_line(picket_left, picket_top, picket_rigth, picket_bottom, fill='gray9', width= 2)

def draw_wire(canvas, left, top, rigth, bottom):
    canvas.create_line(0, 275, 800, 275)



# def draw_pine_tree(canvas, peak_x, peak_y, height):
#     """Draw a single pine tree.
#     Parameters
#         canvas: The tkinter canvas where this
#             function will draw a pine tree.
#         peak_x, peak_y: The x and y location in pixels where
#             this function will draw the top peak of a pine tree.
#         height: The height in pixels of the pine tree that
#             this function will draw.
#     Return: nothing
#     """
#     trunk_width = height / 10
#     trunk_height = height / 8
#     trunk_left = peak_x - trunk_width / 2
#     trunk_right = peak_x + trunk_width / 2
#     trunk_bottom = peak_y + height

#     skirt_width = height / 2
#     skirt_height = height - trunk_height
#     skirt_left = peak_x - skirt_width / 2
#     skirt_right = peak_x + skirt_width / 2
#     skirt_bottom = peak_y + skirt_height

#     # Draw the trunk of the pine tree.
#     canvas.create_rectangle(trunk_left, skirt_bottom,
#             trunk_right, trunk_bottom,
#             outline="gray20", width=1, fill="tan3")

#     # Draw the crown (also called skirt) of the pine tree.
#     canvas.create_polygon(peak_x, peak_y,
#             skirt_right, skirt_bottom,
#             skirt_left, skirt_bottom,
#             outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()