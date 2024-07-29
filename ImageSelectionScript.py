
import cv2
import os

# Create a directory for incorrect images
selected_dir = "MooVita0327selectedPart2selected"
os.makedirs(selected_dir, exist_ok=True)

# Read all image filenames from a folder (you can adapt this part)
image_folder = "/Users/law25/PycharmProjects/fyp/MooVita Datasets/MooVita0327Part2"
image_filenames = [filename for filename in os.listdir(image_folder) if filename.lower().endswith((".jpg", ".png"))]

# Initialize counters
total_images = len(image_filenames)
selected_images = 0
selected_filenames = []

for filename in image_filenames:
    img_path = os.path.join(image_folder, filename)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Could not read image: {filename}")
        continue

    # Display the image and prompt for agreement
    cv2.imshow("Image", img)
    key = cv2.waitKey(0) & 0xFF

    if key == ord(" "):  # Reject
        continue
    elif key == 13:  # Select
        selected_images += 1
        selected_filenames.append(filename)
        # Move the image to the "Selected" folder
        os.rename(img_path, os.path.join(selected_dir, filename))
    else:
        print("Press 'enter' for select or ' ' for reject.")


# Display summary
print(f"Total images: {total_images}")
print(f"Selected images: {selected_images}")
print(f"Selected images saved in: {os.path.abspath(selected_dir)}")