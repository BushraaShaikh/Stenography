# Stenography

Title:Secure Data Hiding in Images Using Steganography

Project Overview:
This project demonstrates the use of steganography to securely hide a secret message within an image. It allows users to encode and decode messages using image pixels. The project also incorporates a password protection feature for added security.

Technologies Used:
1.Python: Programming language used for the implementation.
2.OpenCV (cv2): Library for reading and writing images.
3.OS: Module for system operations (opening images automatically).

Features:
1.Hide a secret message within an image.
2.Retrieve the hidden message through decryption.
3.Password protection for message decryption.
4.Support for printable English characters (ASCII 32-126).

How It Works:
1.Encoding: The secret message is encoded in the pixel values of the image. The message is hidden by replacing the pixel color values with the ASCII values of the characters.
2.Decoding: The message is retrieved by reading the pixel values and converting them back to characters.
3.Password Protection: A passcode is required to decrypt the hidden message, ensuring security.

Setup and Installation:
1.Clone or download the repository.
2.Install the necessary libraries:
bash
pip install opencv-python
3.Ensure the image (mypics.jpg) is located in the appropriate directory or update the path in the script.

Usage
1.Run the script.
2.Input the secret message you want to hide.
3.Set a passcode for the message.
4.The modified image with the hidden message will be saved.
5.To retrieve the hidden message, enter the passcode during decryption.

Example
bash
Enter the secret message to hide: Hello Everyone
Enter your passcode: 123
Enter passcode for decryption: 123
Decrypted message: Hello Everyone

Contributor:
Bushraa Shaikh


