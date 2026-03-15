# Smart Cam Recorder

[cite_start]My simple video recorder using OpenCV[cite: 29]. This program captures webcam footage and allows users to record videos with an optional real-time image filter.

## 🛠 Features & Controls
* [cite_start]**Preview & Record Mode**: Press the `Space` bar to toggle between previewing the camera feed and recording the video[cite: 15, 17].
* [cite_start]**Recording Indicator**: A red circle appears in the top right corner of the screen while recording is active[cite: 16].
* [cite_start]**Grayscale Filter (Extra Feature)**: Press the `g` key to apply or remove a black-and-white filter in real-time[cite: 25].
* [cite_start]**Custom Video Settings (Extra Feature)**: Recorded videos are automatically saved with a timestamped filename using the `mp4v` codec (FourCC) at 20 FPS[cite: 24].
* [cite_start]**Exit**: Press the `ESC` key to close the application safely[cite: 18].

## 💻 Requirements
* Python 3.x
* OpenCV (`pip install opencv-python`)

## 🚀 How to Run
1. Clone this repository to your local machine.
2. Run the script: `python <your_python_file_name>.py`
3. Use the keyboard controls (`Space`, `g`, `ESC`) to interact with the recorder.

## 📸 Demo
![Execution Screenshot](./screenshot.jpg) 
*(Note: Ensure your webcam feed and the red recording indicator are visible in this screenshot)*
