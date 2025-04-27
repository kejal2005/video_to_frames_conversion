import cv2
import os

# Function to extract frames from a video and save them as images
def video_to_frames(video_path, output_folder, fps_to_extract=2):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video is opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Get the FPS (frames per second) of the video
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video FPS: {video_fps}, Total Frames: {total_frames}")

    # Frame counter and extraction interval
    frame_count = 0
    saved_frame_count = 0
    extraction_interval = int(video_fps // fps_to_extract)

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop when video ends

        # Extract frames at the specified interval
        if frame_count % extraction_interval == 0:
            # Construct the frame filename
            frame_name = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")

            # Save the frame as an image
            cv2.imwrite(frame_name, frame)
            print(f"Saving {frame_name}")
            saved_frame_count += 1

        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Total {saved_frame_count} frames saved in {output_folder}")

# Example usage
video_path = 'video_input/video.mp4'  # Path to your video
output_folder = 'video_output'        # Path to save frames
video_to_frames(video_path, output_folder, fps_to_extract=2)  # Extract 2 frames per second