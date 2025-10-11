import argparse
import pytesseract
from PIL import Image
import gtts

def image_to_audio(image_path, output_audio_path="hello.mp3"):
    """
    Converts the text from an image to an audio file.

    Args:
        image_path (str): The path to the input image file.
        output_audio_path (str, optional): The path to save the output audio file.
                                           Defaults to "hello.mp3".
    """
    try:
        # Open the image file
        img = Image.open(image_path)

        # Convert the image to grayscale for better text recognition
        result = pytesseract.image_to_string(img.convert('L'))

        # Generate the audio file from the extracted text
        tts = gtts.gTTS(result)
        tts.save(output_audio_path)

        print(f"Successfully converted image to audio: {output_audio_path}")

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text from an image to an audio file.")
    parser.add_argument("image_path", help="The path to the input image file.")
    parser.add_argument("--output_path", default="hello.mp3", help="The path to save the output audio file (default: hello.mp3).")

    args = parser.parse_args()

    image_to_audio(args.image_path, args.output_path)