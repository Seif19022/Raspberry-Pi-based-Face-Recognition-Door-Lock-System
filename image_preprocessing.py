import os
import cv2

# Path to the directory containing your image files
dataset_dir = r"C:\Users\sseno\OneDrive\Documents\FYP\Dataset"

# Create a new directory within the project directory to store preprocessed images
output_dir = os.path.join(r"C:\Users\sseno\OneDrive\Documents\FYP", "Preprocessed")
os.makedirs(output_dir, exist_ok=True)

print(f"Output directory: {output_dir}")

# List all files in the directory
files = os.listdir(dataset_dir)
print(f"Found {len(files)} files in dataset directory.")

# Iterate over each file
for file_name in files:
    # Check if the file is an image file (you may need to adjust this based on your file extensions)
    if file_name.endswith(('.jpg', '.jpeg', '.png')):
        print(f"Processing file: {file_name}")
        # Construct the full path to the image file
        file_path = os.path.join(dataset_dir, file_name)
        
        # Read the image
        image = cv2.imread(file_path)
        
        # Resize the image to 128x128 pixels
        resized_image = cv2.resize(image, (128, 128))
        
        # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        
        # Normalize pixel values to [0, 1]
        normalized_image = grayscale_image / 255.0
        
        # Construct the output file path within the Preprocessed directory
        output_file_path = os.path.join(output_dir, file_name)
        
        # Save the preprocessed image
        success = cv2.imwrite(output_file_path, (normalized_image * 255).astype('uint8'))
        if success:
            print(f"Saved processed file: {output_file_path}")
        else:
            print(f"Failed to save processed file: {output_file_path}")

print("Preprocessing complete.")
