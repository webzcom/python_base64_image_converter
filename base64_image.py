import base64
from PIL import Image
import io

fileName = "sams_club_240x240.png"
imageType = "PNG"

def image_to_base64(image_path):
    # Open the image
    with Image.open(image_path) as image:
        # Convert the image to RGB format (to ensure compatibility)
        if imageType == 'PNG':
            img_converted = image.convert('RGBA')
            alpha = image.getchannel('A')
            img_converted.putalpha(alpha)
        else:
            img_converted = image.convert('RGB')
        # Create a bytes buffer for the image
        buffer = io.BytesIO()
        # Save the image to the buffer
        #img_converted.save(buffer, format='PNG')  # You can change JPEG to PNG depending on the format you need
        img_converted.save(buffer, format=imageType)

        # Convert binary data to base64-encoded string
        b64_string = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return b64_string

# Example usage
image_path = fileName  # Replace with your image path
base64_string = image_to_base64(image_path)

# Saving the base64 string to a text file
with open(fileName + '-output_base64.txt', 'w') as file:
    file.write(base64_string)

print("Base64 string saved to output_base64.txt")
