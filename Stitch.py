from PIL import Image
import os

tiles_x = 8
tiles_y = 8
full_width = 65536
full_height = 36864

input_dir = r".\Tiles"
Image.MAX_IMAGE_PIXELS = None

tile_w = full_width // tiles_x
tile_h = full_height // tiles_y

print("Reserving memory for the full image")
final_image = Image.new("RGBA", (full_width, full_height))

for y in range(tiles_y):
    for x in range(tiles_x):
        pil_y = (tiles_y - 1) - y
        img_path = os.path.join(input_dir, f"tile_{x}_{y}.png")

        if os.path.exists(img_path):
            tile = Image.open(img_path)
            paste_x = x * tile_w
            paste_y = pil_y * tile_h

            final_image.paste(tile, (paste_x, paste_y))
            print(f"Stitched tile_{x}_{y}")
            tile.close()
        else:
            print(f"WARNING: Missing tile_{x}_{y}.png")

output_path = os.path.join(input_dir, "Final_Stiched_Render.png")
print("Saving image file...")
final_image.save(output_path)
print(f"Saved to {output_path}")
