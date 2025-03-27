from PIL import Image, ImageDraw, ImageFont
import os

def format_name(name):
    """
    Formats the name: if the full name is very long,
    use only the first name and the initial of the last name.
    """
    if len(name) > 15:
        parts = name.split()
        if len(parts) > 1:
            return f"{parts[0]} {parts[-1][0]}."
        return parts[0]
    return name

def generate_certificate(name, level):
    """
    Generates a certificate by placing the formatted name into the
    certificate template. Ensures the name is correctly centered inside
    the red-bordered text box.
    """
    name = format_name(name)
    
    # Choose the template based on level
    if level.lower() == 'elementary':
        template_path = "CERTIFICATE_ELEMENTARY.png"
    else:
        template_path = "CERTIFICATE_ADVANCED.png"
    
    font_path = "SFPRODISPLAYHEAVYITALIC.OTF"
    output_path = f"out/{name} - {level}.png"
    
    # Load the certificate image
    image = Image.open(template_path)
    W, H = image.size  # image width and height
    
    # Correcting given coordinates (from top-right assumption to top-left)
    x_left = 1530
    x_right = 3270
    y_top = 1400
    y_bottom = 1670
    text_box = (x_left, y_top, x_right, y_bottom)
    
    # Calculate the size of the text box
    box_width = x_right - x_left
    box_height = y_bottom - y_top
    
    # Determine font size dynamically (60% of the text box height)
    font_size = int(box_height * 0.6)
    font = ImageFont.truetype(font_path, font_size)
    
    draw = ImageDraw.Draw(image)
    
    # Measure text dimensions
    text_width, text_height = draw.textbbox((0, 0), name, font=font)[2:]
    
    # Calculate coordinates to center the text in the text box
    text_x = x_left + (box_width - text_width) / 2
    text_y = y_top + (box_height - text_height) / 2
    
    # Draw the text on the image (white color)
    draw.text((text_x, text_y), name, font=font, fill="white")
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    print(f"Certificate generated: {output_path}")
    return output_path

# Example usage:
if __name__ == '__main__':
    generate_certificate("Kartik Jain", "Advanced")
