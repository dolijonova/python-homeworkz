from PIL import Image
import numpy as np

# Load the image using PIL
image_path = "images/birds.jpg"
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# 1. Flip the image horizontally and vertically
flipped_horizontal = np.fliplr(image_array)  # Flip left-to-right
flipped_vertical = np.flipud(image_array)   # Flip up-to-down

# 2. Add random noise to the image
noise = np.random.randint(-50, 50, image_array.shape, dtype=np.int16)  # Generate random noise
noisy_image = image_array + noise  # Add noise
noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)  # Clip values to 0-255 range

# 3. Brighten the channels by a fixed value (e.g., 40)
brightened_image = image_array + 40  # Increase brightness
brightened_image = np.clip(brightened_image, 0, 255).astype(np.uint8)  # Clip values to 0-255 range

# 4. Apply a mask to a rectangular region (e.g., 100x100 area in the center)
masked_image = image_array.copy()
height, width, _ = masked_image.shape
center_x, center_y = width // 2, height // 2
masked_image[center_y-50:center_y+50, center_x-50:center_x+50] = [0, 0, 0]  # Set pixels to black

# Save the modified images using PIL
Image.fromarray(flipped_horizontal).save("flipped_horizontal.jpg")
Image.fromarray(flipped_vertical).save("flipped_vertical.jpg")
Image.fromarray(noisy_image).save("noisy_image.jpg")
Image.fromarray(brightened_image).save("brightened_image.jpg")
Image.fromarray(masked_image).save("masked_image.jpg")

print("Image manipulations completed and saved.")