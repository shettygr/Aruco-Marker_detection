import cv2
import cv2.aruco as aruco
import time

def detect_aruco_marker():
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    aruco_params = aruco.DetectorParameters_create()

    cap = cv2.VideoCapture(0)
    marker_ids = [11, 13, 10, 25, 15, 16, 17, 18, 19]
    marker_labels = ["box1", "box2", "box3", "box4", "box5", "box6", "box7", "box8", "box9"]

    current_marker_index = 0
    start_time = 0
    display_time = 1

    while current_marker_index < len(marker_ids):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = aruco.detectMarkers(gray, aruco_dict, parameters=aruco_params)

        if ids is not None and len(ids) > 0:
            for i in range(len(ids)):
                if ids[i] == marker_ids[current_marker_index]:
                    aruco.drawDetectedMarkers(frame, corners, ids)

                    x = int(corners[i][0][0][0])
                    y = int(corners[i][0][0][1])
                    cv2.putText(frame, marker_labels[current_marker_index] + " detected", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                    start_time = time.time()
        elapsed_time = time.time() - start_time
        if elapsed_time > display_time:
            current_marker_index = (current_marker_index + 1) % len(marker_ids)
        cv2.imshow("ArUco Marker Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('h'):
            break
    cap.release()
    cv2.destroyAllWindows()

detect_aruco_marker()
