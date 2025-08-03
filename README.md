Network Anomaly Detection using Autoencoder
This project implements a simple anomaly detection mechanism using an autoencoder neural network to identify unusual patterns in network traffic data. It is suitable for unsupervised learning where only normal data is available during training.

Project Summary
An autoencoder is trained on preprocessed numeric network traffic features. Once trained, it reconstructs normal samples well but produces high reconstruction error for anomalous ones. This reconstruction error is used to flag anomalies.

File Structure
graphql
Copy
Edit
.
├── network_anomaly_finder.py   # Main script
├── network_data.csv            # Input CSV dataset (not included)
└── README.md                   # Project description
Features
Minimal dependencies and easy to run

Cleans dataset by removing non-numeric and irrelevant columns

Scales features using MinMaxScaler

Uses a simple 1-hidden-layer autoencoder

Detects anomalies based on reconstruction error using the 95th percentile threshold

Requirements
Install dependencies:

bash
Copy
Edit
pip install pandas numpy scikit-learn tensorflow
Input Data
The script expects a CSV file named network_data.csv. This should be placed in the same directory. The file must include mostly numeric columns.

Columns automatically dropped if present:

Label

Attempted Category

Timestamp

How to Run
Simply execute the script using:

bash
Copy
Edit
python network_anomaly_finder.py
The script will:

Load and clean the dataset

Normalize the features

Train the autoencoder

Compute reconstruction error

Identify anomalies based on thresholding

Output
The script prints:

Shape of data after cleaning

Training progress of the autoencoder

Indices of detected anomalies

Total number of anomalies found

How it Works
Drop non-numeric and non-relevant columns

Normalize all feature values between 0 and 1

Train a single-hidden-layer autoencoder on the scaled data

Predict reconstruction and compute MSE per sample

Set the anomaly threshold at the 95th percentile of MSE

Flag samples with MSE above this threshold

Future Improvements
Save and load trained model for reuse

Add graphical error distribution plot

Allow dynamic input filenames via command-line arguments

Extend to use time-series models (e.g., LSTM)

Author
Vinoth Kumar
GitHub: 59VINOTHKUMARKB
