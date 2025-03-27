import cv2

# Path to your image file (adjust as needed)
image_path = "CERTIFICATE_ADVANCED.png"

# Load the image
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found.")
    exit()

# Get original dimensions
orig_height, orig_width = image.shape[:2]

# Set maximum window size (you can adjust these as needed)
max_width = 1200
max_height = 800

# Compute scale factor: scale down if image is larger than max dimensions
scale = min(max_width / orig_width, max_height / orig_height, 1.0)

# Resize the image for display if necessary
if scale < 1.0:
    disp_width = int(orig_width * scale)
    disp_height = int(orig_height * scale)
    display_image = cv2.resize(image, (disp_width, disp_height))
else:
    display_image = image.copy()
    disp_width, disp_height = orig_width, orig_height

# Create a window that can be resized
cv2.namedWindow("Image Coordinates", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image Coordinates", disp_width, disp_height)

def mouse_callback(event, x, y, flags, param):
    # We use the original image and then show coordinates computed from the scale factor
    # Copy the displayed image so we don't draw multiple texts
    temp_image = display_image.copy()
    
    if event == cv2.EVENT_MOUSEMOVE:
        # Calculate the corresponding original image coordinates
        orig_x = int(x / scale)
        orig_y = int(y / scale)
        # Compose the text showing both displayed and original coordinates if desired
        text = f"Disp: ({x}, {y}) | Orig: ({orig_x}, {orig_y})"
        # Put the text on the image near the cursor (adjust offsets as necessary)
        cv2.putText(temp_image, text, (x + 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        # Show the updated image with coordinates
        cv2.imshow("Image Coordinates", temp_image)
        # Optionally, print coordinates to the console
        print(text, end='\r')

# Set the mouse callback function
cv2.setMouseCallback("Image Coordinates", mouse_callback)

print("Move your mouse over the image window to see coordinates. Press 'q' to exit.")

while True:
    cv2.imshow("Image Coordinates", display_image)
    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
