import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd

# Load your Shinchan image
img = mpimg.imread("image.jpeg")  

# Convert to numpy array
img_array = np.array(img)

# Create a pandas DataFrame with pixel data
pixels = pd.DataFrame(
    img_array.reshape(-1, img_array.shape[-1]),
    columns=["R", "G", "B", "A"] if img_array.shape[-1] == 4 else ["R", "G", "B"]
)

print("Image shape:", img_array.shape)
print(pixels.head())

# Display Shinchan pixel-perfect
plt.figure(figsize=(6,6))
plt.imshow(img_array)
plt.axis("off")
plt.title("Pixel-perfect Shinchan")
plt.show()
