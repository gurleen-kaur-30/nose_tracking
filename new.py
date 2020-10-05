import cv2
import imutils
import time
from imutils.video import VideoStream
from imutils.video import FPS

tracker = cv2.TrackerCSRT_create()

vs = VideoStream(src=0).start()
time.sleep(1.0)

initBB = None

while True:
    print("ok")
    
    frame = vs.read()

    if frame is None:
        break

    frame  = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]
    if initBB is not None:
	# grab the new bounding box coordinates of the object
        (success, box) = tracker.update(frame)

		# check to see if the tracking was a success
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h),
				(0, 255, 0), 2)

		# update the FPS counter
        fps.update()
        fps.stop()

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
		# select the bounding box of the object we want to track (make
		# sure you press ENTER or SPACE after selecting the ROI)
        initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)


	# start OpenCV object tracker using the supplied bounding box
	# coordinates, then start the FPS throughput estimator as well
        tracker.init(frame, initBB)
        fps = FPS().start()

    elif key == ord("q"):
        break

cv2.destroyAllWindows()
