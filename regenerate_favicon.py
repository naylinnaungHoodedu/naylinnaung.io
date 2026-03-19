from PIL import Image
import os

source_path = r"C:/Users/user/.gemini/antigravity/brain/7eaa7909-9618-4dbe-8cd1-05d97aba62ad/uploaded_image_1766000885399.jpg"
dest_dir = r"c:/Users/user/Downloads/Alam/nay_linn_aung_profile/assets/images"
dest_path = os.path.join(dest_dir, "favicon.png")

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

try:
    print(f"Opening source: {source_path}")
    img = Image.open(source_path)
    print(f"Source format: {img.format}, Size: {img.size}, Mode: {img.mode}")
    
    # create a square crop (center)
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    
    img = img.crop((left, top, right, bottom))
    img = img.resize((64, 64), Image.Resampling.LANCZOS)
    
    # Force save as standard PNG
    img.save(dest_path, format="PNG", optimize=True)
    print(f"Successfully created favicon at {dest_path}")
    
    # Verify save
    with Image.open(dest_path) as saved:
        print(f"Verified saved file: {saved.format}, {saved.size}")

except Exception as e:
    print(f"Error creating favicon: {e}")
