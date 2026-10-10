# AI-Assisted Smart Blind Stick

**Hackfest 2026 | Selected Problem Statement: 5A — Context-Aware Application Agent**

## 1. Project Overview

The AI-Assisted Smart Blind Stick is an assistive technology project designed to help visually impaired people navigate their surroundings more safely. It combines camera-based object detection, ultrasonic sensing, and audio alerts to provide environmental information in real time.

## 2. Problem Statement

Conventional walking sticks primarily help users identify physical obstacles through contact. They have limited ability to identify objects, estimate obstacle distance electronically, or provide contextual audio information about the surrounding environment.

Our project aims to address these limitations through an intelligent, sensor-assisted mobility system.

## 3. Proposed Solution

The proposed system uses a Raspberry Pi and camera to process visual information. Ultrasonic sensor provide additional environmental inputs. The system processes the available information and generates appropriate voice or buzzer alerts based on detected conditions.

## 4. Objectives

- Detect supported objects using computer vision.
- Identify nearby obstacles using distance sensing.
- Detect steps or ground-level changes where supported by the sensor configuration.
- Provide understandable audio alerts.
- Integrate multiple sensing modalities into a practical assistive prototype.

## 5. Key Features

- Camera-based object detection.
- Ultrasonic obstacle-distance measurement.
- Voice feedback and buzzer alerts.
- Real-time environmental assistance.
- Context-aware alert logic, where implemented.

## 6. Hardware Requirements

- Raspberry Pi.
- Compatible Raspberry Pi camera.
- Ultrasonic sensor.
- Buzzer.
- Speaker or other compatible audio output device.
- Connecting wires and suitable power supply.
- Smart stick structure for mounting the components.

## 7. Software and Technologies

- Python.
- YOLOv15n
- Raspberry Pi operating system.
- Computer vision and object detection.
- Raspberry Pi camera software and libraries.
- GPIO control for supported sensors.
- Audio or text-to-speech software, depending on the implementation.

## 8. System Workflow

1. The camera captures the surrounding scene.
2. The object-detection component processes visual information.
3. The ultrasonic sensor measures the distance to nearby obstacles.
4. The application processes the available sensor information.
5. The system provides an appropriate voice or buzzer alert.

## 9. Project Architecture

**Environmental Inputs → Camera and Sensors → Processing and Detection → Decision Logic → Voice/Buzzer Alerts → User**

## 10. Expected Outcomes

- A functional prototype integrating the selected sensors and camera.
- Detection of supported objects and nearby obstacles.
- Audio feedback for selected hazards.
- Demonstration of multimodal sensing for assistive mobility.
- A documented software implementation and testing process.

## 11. Testing and Evaluation

The prototype will be evaluated using predefined scenarios involving supported objects, nearby obstacles, sensor responses, audio alerts, response time, and false alerts.

## 12. Limitations and Safety

Detection performance may vary with lighting conditions, sensor placement, object type, and processing limitations. This prototype is intended as an assistive technology demonstration and must not replace a conventional white cane, guide dog, or established mobility assistance.

## 13. Future Enhancements

- Improved scene understanding.
- GPS-based location assistance.
- Emergency notification functionality.
- Mobile application integration.
- Personalized alerts and navigation assistance.

These features are future enhancements unless explicitly implemented in the current prototype.

## 14. Raspberry Pi System Dependencies

The application requires the following system components:

- Raspberry Pi OS with compatible Python support
- Picamera2 and Raspberry Pi camera support
- RPi.GPIO for ultrasonic sensor, LED and buzzer control
- eSpeak NG for voice announcements
- OpenCV support for displaying the detection window

On a compatible Raspberry Pi OS installation, system packages can be installed with:

```bash
sudo apt update
sudo apt install python3-picamera2 python3-rpi.gpio espeak-ng python3-opencv
```

The Ultralytics YOLO package and its compatible dependencies must also be installed in an appropriate Python environment.

## Running the Application

1. Connect the camera, ultrasonic sensor, LED and buzzer.
2. Confirm that the GPIO wiring matches the pin numbers in `main.py`.
3. Ensure the YOLO model file `yolo26n.pt` is available in the working directory, or configure the correct model path.
4. Install compatible software dependencies.
5. Run the Python application on the Raspberry Pi.

## Hardware Safety

The ultrasonic sensor's ECHO output must be compatible with the Raspberry Pi's 3.3 V GPIO input. Use an appropriate voltage divider or level shifter if the sensor outputs 5 V.


## 14. Team Details

**Team Name:** VisionAid

**Team Members:**
1. Member 1 — Akash Walad
2. Member 2 — Basuraj Shibaragatti
3. Member 3 — Manoj Rode
4. Member 4 — Sachin Chanaveer
5. Member 5 — Sahad kokatanur
6. Member 6 — Vrushabh kadam


## 15. Project Status

This repository contains the source code and documentation for the AI-Assisted Smart Blind Stick project. Features, dependencies, setup instructions, and test results should be updated to reflect the actual implementation.