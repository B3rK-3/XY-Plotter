# XY Plotter

This is a Python project developed for the Robotics Club's XY Plotter Robot. Follow this guide to build and run your own version.

---

## Guide

### Installation

1. Clone the repository:
   git clone https://github.com/B3rK-3/XY-Plotter.git

2. Navigate to the project directory:
   cd XY-Plotter

3. Install the required dependencies:
   pip install -r requirements.txt

---

### Running the Project

1. Start the backend:
   python backend.py

2. The interface will open in your browser using Eel and HTML/CSS, allowing image uploads and process initiation.

---

### Project Workflow

1. Web UI and Backend Communication:
   - The backend communicates with the web UI through Eel.
   - When the "Trace Image" command is triggered, the backend:
     - Copies the uploaded image to ./web/upload_img.
     - Allows the UI to render the uploaded image.

2. Image Processing:
   - The backend invokes trace_edge.py, which:
     - Traces the edges of the uploaded image.
     - Exports the processed image to ./web/export_img.

3. Drawing Process:
   - When the "Draw" process is started:
     - trace_edge.py converts black pixels into points (ignoring white pixels).
     - Calls motorController.py to:
       - Generate motor instructions.
       - Guide the robot to trace the image.

---

Happy Plotting!

