import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    pixel_index = 0
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '11111111'  # Thêm dấu kết thúc thông điệp

    # BAI 5: DUNG DONG BAO MAT
    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            if data_index < len(binary_message):
                pixel[0] = pixel[0] & ~1 | int(binary_message[data_index])  # Kênh đỏ
                data_index += 1
            if data_index < len(binary_message):
                pixel[1] = pixel[1] & ~1 | int(binary_message[data_index])  # Kênh xanh
                data_index += 1
            if data_index < len(binary_message):
                pixel[2] = pixel[2] & ~1 | int(binary_message[data_index])  # Kênh xanh lá
                data_index += 1
            img.putpixel((col, row), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = "encoded_image.png"
    img.save(encoded_image_path)
    print("Steganography completed. Encoded image saved as:", encoded_image_path)

def main():
    if len(sys.argv) == 3:
        image_path = sys.argv[1]
        message = sys.argv[2]
        encode_image(image_path, message)
    else:
        print("Usage: python encrypt.py <image_path> <message>")
        print("Example: python encrypt.py image.png Hello")

if __name__ == "__main__":
    main()