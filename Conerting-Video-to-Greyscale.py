import cv2

# Function to convert a video from RGB to grayscale
def convert_video_to_grayscale(input_path, output_path):
    # Open the video file
    video = cv2.VideoCapture(input_path)

    # Get the video's frames per second (fps)
    fps = video.get(cv2.CAP_PROP_FPS)

    # Get the video's width and height
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a VideoWriter object to save the grayscale video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' codec as fallback
    grayscale_video = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

    # Read and convert each frame to grayscale
    while True:
        ret, frame = video.read()

        if not ret:
            break

        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Write the grayscale frame to the output video file
        grayscale_video.write(grayscale_frame)

        cv2.imshow('Grayscale Video', grayscale_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and writer objects
    video.release()
    grayscale_video.release()
    cv2.destroyAllWindows()

# User inputs
input_path = input("Enter the path to the input video file: ")
output_path = input("Enter the path to save the grayscale video file: ")

# Convert the video from RGB to grayscale
convert_video_to_grayscale(input_path, output_path)
