# 🎞️ Video Frame Extractor  
A lightweight Python script to extract frames from a video file at a specified rate using OpenCV.

## ✨ Features  
- 📹 Extracts frames from `.mp4` and other supported video formats  
- 🖼️ Saves frames as high-quality `.jpg` images  
- ⚙️ Customizable frame extraction rate (e.g., 2 frames per second)  
- 📁 Automatically creates the output directory if it doesn't exist  

## 📂 Project Structure  
```

video-frame-extractor/
├── main.py                # Core script to extract frames
├── video\_input/           # Folder to store input video
│   └── video.mp4
├── video\_output/          # Folder where extracted frames will be saved
└── README.md              # Project documentation

````

## 🛠️ Requirements  
- Python 3.x  
- OpenCV  

Install dependencies using pip:  
```bash
pip install opencv-python
````

## 🚀 Usage

1. Place your input video (e.g., `video.mp4`) in the `video_input/` folder.
2. Run the script:

```bash
python main.py
```

3. Frames will be saved in the `video_output/` directory.

## 🎯 Customization

To change the frame extraction rate, modify the `fps_to_extract` parameter:

```python
video_to_frames(video_path, output_folder, fps_to_extract=2)
```

For example, setting `fps_to_extract=5` will extract 5 frames per second.

## 🧠 How It Works

* The script opens the video using OpenCV
* Calculates how frequently frames should be extracted based on the original video FPS
* Saves frames at regular intervals using `cv2.imwrite()`

## 🖼️ Sample Output

```
video_output/  
├── frame_0000.jpg  
├── frame_0001.jpg  
├── frame_0002.jpg  
└── ...
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

> Created with ❤️ by \Kejal Jain — Powered by Python & OpenCV

```


