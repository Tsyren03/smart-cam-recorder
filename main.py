import cv2
import datetime

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20.0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = None

recording = False
apply_grayscale = False
apply_flip = False
apply_invert = False

print("Controls: [Space]: Record/Stop | [g]: Grayscale | [f]: Flip | [i]: Invert | [ESC]: Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip video horizontally
    if apply_flip:
        frame = cv2.flip(frame, 1)

    # Grayscale filter
    if apply_grayscale:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Convert back to BGR so the red UI circle remains red
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    # Invert colors (Negative)
    if apply_invert:
        frame = cv2.bitwise_not(frame)

    # Save video when in Record mode
    if recording:
        if out is None:
            filename = f"record_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
            out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
        out.write(frame)

    display_frame = frame.copy()

    if recording:
        cv2.circle(display_frame, (width - 30, 30), 10, (0, 0, 255), -1)

    cv2.imshow('Video Recorder', display_frame)

    # Keyboard input handling
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == 32:
        recording = not recording
        if not recording and out is not None:
            out.release()
            out = None
    elif key == ord('g'):
        apply_grayscale = not apply_grayscale
    elif key == ord('f'):
        apply_flip = not apply_flip
    elif key == ord('i'):
        apply_invert = not apply_invert

cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()