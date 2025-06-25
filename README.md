# Drowsiness Detector

This project is a drowsiness detection application that utilizes a webcam to monitor the user's alertness. It analyzes the webcam feed to determine if the user is drowsy and triggers an alert if drowsiness is detected.

## Project Structure

```
drowsiness-detector
├── src
│   ├── main.py          # Entry point of the application
│   ├── detector.py      # Drowsiness detection logic
│   ├── camera.py        # Webcam management
│   └── utils.py         # Utility functions
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/drowsiness-detector.git
   cd drowsiness-detector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Ensure that your webcam is connected and accessible. The application will start monitoring your drowsiness levels.

## Functionality

- **Webcam Feed**: The application captures video from the webcam.
- **Drowsiness Detection**: It analyzes the captured frames to detect signs of drowsiness.
- **Alerts**: If drowsiness is detected, the application will trigger an alert to notify the user.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.