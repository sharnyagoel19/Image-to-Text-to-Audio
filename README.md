# Image-to-Text-to-Audio

This project is a command-line tool that converts the text from an image into an audio file. It uses Tesseract OCR to extract text from the image and Google Text-to-Speech (gTTS) to convert the text into speech.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3**: This project is written in Python and requires Python 3 to run.
- **Tesseract OCR**: This is required for text extraction from images.

You can install Tesseract OCR on Debian-based systems with the following command:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sharnyagoel19/Image-to-Text-to-Audio.git
   cd Image-to-Text-to-Audio
   ```

2. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the script, run the following command in your terminal, providing the path to the image you want to convert:

```bash
python image_to_audio.py <path_to_your_image>
```

By default, the output audio file will be saved as `hello.mp3` in the same directory.

### Optional Arguments

You can also specify a custom path for the output audio file using the `--output_path` argument:

```bash
python image_to_audio.py <path_to_your_image> --output_path <custom_output_name.mp3>
```

### Example

To convert the text from the included `Picture1.png` and save it as `output.mp3`:

```bash
python image_to_audio.py Picture1.png --output_path output.mp3
```

This will create an `output.mp3` file containing the spoken text from the image.