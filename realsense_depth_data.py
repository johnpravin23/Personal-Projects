import cv2
import pyrealsense2 as rs
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1280, 480))

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

pipeline.start(config)


try:
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()
        if not color_frame or not depth_frame:
            continue

        # Print width and height data for color frame        
        color_width = color_frame.get_width()
        color_height = color_frame.get_height()
        print(f"Color Frame - Width: {color_width}, Height: {color_height}")
        
        # Print width and height data for depth frame
        depth_width = depth_frame.get_width()
        depth_height = depth_frame.get_height()
        print(f"Depth Frame - Width: {depth_width}, Height: {depth_height}")

        # Convert the frames from realsense camera to frames cv2 can understand
        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())

        gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        gray_3_channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.05), cv2.COLORMAP_JET)

        # Stack the two images together
        images = np.hstack((gray_3_channel, depth_colormap))

        cv2.imshow('RealSense (Color left, Depth right)', images)
        out.write(images)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    out.release()
    cv2.destroyAllWindows()