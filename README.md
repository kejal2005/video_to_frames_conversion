# 🎞️ Video Frame Extractor

A simple Python script to extract frames from a video at a specific rate and save them as image files using OpenCV.

## 📌 Features

- 🎥 Extracts frames from video files (e.g., `.mp4`)
- 🖼️ Saves frames as `.jpg` images
- ⏱️ Customizable extraction rate (frames per second)
- 📂 Automatically creates output directory if it doesn't exist

---

## 📁 Folder Structure

project/
│
├── video_input/
│ └── video.mp4 # Input video file
│
├── video_output/ # Extracted frames will be saved here
│
└── main.py # Python script to run


---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- OpenCV

Install the required dependency:

```bash
pip install opencv-python

⚙️ Usage
Place your video file inside the video_input/ directory.

Run the Python script.
python main.py
Extracted frames will be saved in the video_output/ folder.

🎯 Customize Frame Extraction Rate
You can change how many frames per second to extract by modifying:

video_to_frames(video_path, output_folder, fps_to_extract=2)  # 2 frames per second

🧠 How It Works
Loads video using OpenCV.

Retrieves video FPS (frames per second).

Calculates interval based on desired extraction FPS.

Saves selected frames as .jpg images.

video_output/
├── frame_0000.jpg
├── frame_0001.jpg
├── frame_0002.jpg
└── ...

📃 License
This project is licensed under the MIT License.


💡 Created with ❤️ using Python and OpenCV

Just copy and paste this into a `README.md` file in your GitHub repository. Let me know if you'd like badges or enhancements like GIF demos!

