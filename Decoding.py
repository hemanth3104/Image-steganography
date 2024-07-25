import cv2
import os
import hashlib

def load_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found. Check the file path and make sure the image exists.")
        exit()
    return img

def get_hashed_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.digest()

def create_ascii_dictionaries():
    d = {chr(i): i for i in range(256)}  # Character to ASCII
    c = {i: chr(i) for i in range(256)}  # ASCII to character
    return d, c

def decode_message(img, hashed_password):
    height, width, channels = img.shape
    _, c = create_ascii_dictionaries()

    n, m, z = 0, 0, 0  # Row index, Column index, Color channel index

    decoded_msg = ""
    while True:
        char_value = (int(img[n, m, z]) - hashed_password[len(decoded_msg) % len(hashed_password)]) % 256
        decoded_char = c[char_value]

        # Stop decoding if we encounter a non-printable character (or specify another stopping condition)
        if not (32 <= char_value <= 126):  # ASCII printable characters range from 32 to 126
            break

        decoded_msg += decoded_char

        m += 1
        if m >= width:
            m = 0
            n += 1

        if n >= height:
            break

        z = (z + 1) % 3

    return decoded_msg

def main():
    # Specify the path to the encoded image
    encoded_image_path = r"C:\Users\adida\OneDrive\Desktop\New folder (2)\encryptedImage.jpg"
    img = load_image(encoded_image_path)

    # Prompt the user to input the password for decoding
    password = input("Enter the passcode to decode the message: ")

    hashed_password = get_hashed_password(password)
    decoded_msg = decode_message(img, hashed_password)

    print(f"Decoded message: {decoded_msg}")

if __name__ == "__main__":
    main()
      
