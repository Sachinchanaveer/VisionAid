import RPi.GPIO as G
import time, threading, subprocess, cv2
from picamera2 import Picamera2
from ultralytics import YOLO

TRIG, ECHO, LED, BUZZER = 23, 24, 17, 27
G.setmode(G.BCM)
for p, mode in [(TRIG,G.OUT),(ECHO,G.IN),(LED,G.OUT),(BUZZER,G.OUT)]:
    G.setup(p, mode)

G.output(TRIG, 0)
buzz = G.PWM(BUZZER, 2000)
buzz.start(0)

distance = 999
stop = threading.Event()

def sensor():
    global distance
    while not stop.is_set():
        G.output(TRIG, 1)
        time.sleep(0.00001)
        G.output(TRIG, 0)

        end = time.monotonic() + 0.03
        while G.input(ECHO) == 0 and time.monotonic() < end:
            pass

        if G.input(ECHO):
            start = time.monotonic()
            while G.input(ECHO) and time.monotonic()-start < 0.03:
                pass
            distance = (time.monotonic()-start) * 17150
        else:
            distance = 999

        near = distance < 20
        G.output(LED, near)
        buzz.ChangeDutyCycle(50 if near else 0)
        time.sleep(0.05)

cam = None
try:
    threading.Thread(target=sensor, daemon=True).start()

    cam = Picamera2()
    cam.configure(cam.create_preview_configuration(
        main={"size": (640, 480), "format": "RGB888"}))
    cam.start()

    model = YOLO("yolo26n.pt")
    last, spoken = "", 0

    while True:
        frame = cam.capture_array()
        result = model.predict(frame, imgsz=320, conf=0.5,
                               verbose=False)[0]

        key, message = "", ""
        if distance < 20:
            key = "obstacle"
            message = f"Obstacle at {int(distance)} centimeters"
        elif len(result.boxes):
            i = int(result.boxes.conf.argmax().item())
            key = str(model.names[int(result.boxes.cls[i].item())])
            message = key + " detected"

        now = time.monotonic()
        if key and (key != last or now-spoken > 4):
            subprocess.run(["espeak-ng", "-s", "145", message],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            spoken = time.monotonic()

        last = key
        cv2.imshow("Smart Blind Stick", result.plot())
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    pass
finally:
    stop.set()
    if cam:
        cam.stop()
    buzz.stop()
    G.cleanup()
    cv2.destroyAllWindows()