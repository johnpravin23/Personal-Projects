RealSense Camera Depth and Color Stream Capture

Project Description:

This project captures video from an Intel RealSense camera, processing both the color and depth streams. The color stream is converted to grayscale and then combined side by side with the depth stream, which is visualized using a color map. The combined stream is displayed in real-time and saved as an AVI file.

Prerequisites:

Python 3.x
OpenCV-Python
PyRealSense2
An Intel RealSense Camera

Installation:

Install Python 3.x from Python's official website.
Install the required Python packages:
    pip install opencv-python numpy pyrealsense2

Connect your Intel RealSense Camera to your computer.

Usage:

To run the script, navigate to the directory containing the script and execute:
    python3 realsense_depth_data.py

The script will start capturing frames from the RealSense camera. The color stream is displayed in grayscale, and the depth stream is visualized with a color map. Both streams are shown side by side in a single window and saved to an AVI file named output.avi.

Press 'q' to exit and stop the video capture.

Features:

Captures color and depth streams from the Intel RealSense camera.
Converts color stream to grayscale.
Applies a Jet color map to the depth stream for visualization.
Displays the combined grayscale and depth streams in real-time.
Saves the combined stream to an AVI file.# Personal-Projects
