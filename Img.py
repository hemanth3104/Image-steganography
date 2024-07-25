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

def encode_message(img, msg, hashed_password):
    height, width, channels = img.shape
    d, _ = create_ascii_dictionaries()

    n, m, z = 0, 0, 0  # Row index, Column index, Color channel index

    for i in range(len(msg)):
        new_value = (int(img[n, m, z]) + d[msg[i]] + hashed_password[i % len(hashed_password)]) % 256
        img[n, m, z] = new_value

        m += 1
        if m >= width:
            m = 0
            n += 1

        if n >= height:
            print("Image too small to hold the entire message.")
            break

        z = (z + 1) % 3

def save_image(img, path):
    cv2.imwrite(path, img)

def main():
    # Specify the path to the input image
    image_path = r"C:\Users\adida\OneDrive\Desktop\New folder (2)\car.jpeg"
    img = load_image(image_path)

    # Prompt the user to input the secret message and password
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    hashed_password = get_hashed_password(password)
    encode_message(img, msg, hashed_password)

    encrypted_image_path = os.path.join(os.path.dirname(image_path), "encryptedImage.jpg")
    save_image(img, encrypted_image_path)

    # Open the newly saved encrypted image
    os.startfile(encrypted_image_path)
    print(f"Message has been encoded into '{encrypted_image_path}'.")

if __name__ == "__main__":
    main()
  
