
# Image Selection Script
## Description
This project provides a script to manually select images from a specified folder. Users can view each image and decide whether to keep it or reject it. Selected images are moved to a designated directory and the total number of selected images will be displayed.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation
Install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows)


1. Create a new project:

![Screenshot (5)](https://github.com/user-attachments/assets/505ebcc0-a23f-41de-8e75-bd82759452ce)


2. Open settings and select "Python Intepreter" under your project. Click on the '+' sign and search for "opencv-python" to install the OpenCV package:

![Screenshot (2)](https://github.com/user-attachments/assets/1bc46e42-2b96-404d-8a32-f3347c3db87d)
![Screenshot (6)](https://github.com/user-attachments/assets/a913794f-e252-47f4-84ee-5599aa880fb0)
![Screenshot (7)](https://github.com/user-attachments/assets/18c56eba-8351-470a-b263-fdf4a6077608)

3. Create a new Python file:

![Screenshot (4)](https://github.com/user-attachments/assets/7344ef74-ca51-4d8e-be36-91933edf2906)

## Usage
To use the script, you need to provide the path to the folder containing images and specify the output folder for selected images.

    1. Update the image_folder and selected_dir variables in the script with the appropriate paths.
    2. Run the script:

### Example
Here is an example of how to use the script:

    import cv2
    import os

    # Create a directory for incorrect images
    selected_dir = "NameOfDirectory"
    os.makedirs(selected_dir, exist_ok=True)

    # Read all image filenames from a folder (you can adapt this part)
    image_folder = "/path/to/your/image/folder"
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

## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).



