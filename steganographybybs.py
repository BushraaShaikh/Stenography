import cv2
import os

# Read the image
image_path = "D:\Steganography Project\mypics.jpg"  # Adjust the image path
img = cv2.imread(image_path)

# Prompt the user for a secret message and a password
secret_message = input("Enter the secret message to hide (only English characters): ")
password_input = input("Enter your passcode: ")

# Create mappings for characters to integers and vice versa (restricting to printable ASCII characters)
char_to_int = {}
int_to_char = {}

# Limit to printable ASCII characters (32 to 126 for English)
for i in range(32, 127):
    char_to_int[chr(i)] = i
    int_to_char[i] = chr(i)

# Initialize variables to keep track of position in the image
x, y, color_channel = 0, 0, 0
msg_index = 0  # To track message position

# Hide the secret message in the image
for i in range(img.shape[0]):  # Loop through rows
    for j in range(img.shape[1]):  # Loop through columns
        if msg_index < len(secret_message):  # Still have message to hide
            char = secret_message[msg_index]
            if char in char_to_int:  # Only store printable characters
                img[i, j, color_channel] = char_to_int[char]
                msg_index += 1
                color_channel = (color_channel + 1) % 3  # Loop through RGB channels

# Save the modified image
cv2.imwrite("hidden_image.jpg", img)
os.system("start hidden_image.jpg")  # Opens the image automatically (Windows)

# Decrypt the message after the user provides the correct password
decrypted_message = ""
user_passcode = input("Enter passcode for decryption: ")

if password_input == user_passcode:
    msg_index = 0
    color_channel = 0  # Reset color channel to start with the first channel
    for i in range(img.shape[0]):  # Loop through rows
        for j in range(img.shape[1]):  # Loop through columns
            if msg_index < len(secret_message):  # Still have message to extract
                pixel_value = img[i, j, color_channel]
                if pixel_value in int_to_char:  # Only decode printable characters
                    decrypted_message += int_to_char[pixel_value]
                    msg_index += 1
                color_channel = (color_channel + 1) % 3  # Loop through RGB channels
    print("Decrypted message:", decrypted_message)
else:
    print("Authentication failed! Incorrect passcode.")
