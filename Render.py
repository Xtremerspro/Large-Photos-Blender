import bpy
import os

tiles_x = 8
tiles_y = 8
output_dir = r".\Tiles"

scene = bpy.context.scene
scene.render.use_border = True
scene.render.use_crop_to_border = True

for y in range(tiles_y):
    for x in range(tiles_x):
        scene.render.border_min_x = x / tiles_x
        scene.render.border_max_x = (x + 1) / tiles_x
        scene.render.border_min_y = y / tiles_y
        scene.render.border_max_y = (y + 1) / tiles_y

        filepath = os.path.join(output_dir, f"tile_{x}_{y}.png")
        scene.render.filepath = filepath

        if not os.path.exists(filepath):
            print(f"Rendering tile {x},{y}...")
            bpy.ops.render.render(write_still=True)
        else:
            print(f"Skipping tile {x},{y} (Already exists)")

scene.render.use_border = False
scene.render.use_crop_to_border = False
print("Render sequence complete")
