# Potato Disease Detection App 🌱🛠️

This project focuses on detecting diseases in potato plants using a **deep learning model** and deploying the functionality through a **React-based web application**. The app is designed to help farmers identify common potato plant diseases such as Early Blight and Late Blight, or confirm the plant is healthy, by analyzing uploaded images.

---

## Table of Contents  
1. [Project Overview](#project-overview)  
2. [Requirements](#requirements)  
   - [Backend Requirements](#backend-requirements-model-training-and-prediction)  
   - [Frontend Requirements](#frontend-requirements-react-web-app)  
3. [Dataset](#dataset)  
4. [Model Architecture](#model-architecture)  
5. [Training the Model](#training-the-model)  
6. [Running the Project](#running-the-project)  
   - [Step 1: Start the Backend Server](#step-1-start-the-backend-server)  
   - [Step 2: Start the React Web App](#step-2-start-the-react-web-app)  
7. [React Web App](#react-web-app)  
8. [Acknowledgments](#acknowledgments)  

---

## Project Overview

This project is split into two parts:  

1. **Deep Learning Model**: A TensorFlow-based **Convolutional Neural Network (CNN)** is used to classify potato plant images into categories based on their health status or disease.  
2. **React Web App**: A user-friendly web application enables farmers to upload images of their plants, view predictions, and receive disease prevention recommendations.  

> The file **`potato7.py`** is responsible for generating and training the deep learning model, while **`mainfastapi.py`** creates a local server (using FastAPI) that the React app interacts with for making predictions.

---

## Requirements

### Backend Requirements (Model Training and Prediction)
- **Python 3.x**  
- **TensorFlow 2.x**  
- **Keras (bundled with TensorFlow)**  
- **NumPy**  
- **Matplotlib**  
- **PIL (Python Imaging Library)**  
- **Scikit-learn**  
- **FastAPI**  
- **Uvicorn**  

Install these dependencies using the following command:  
```bash
pip install tensorflow numpy matplotlib pillow scikit-learn fastapi uvicorn
Frontend Requirements (React Web App)
Node.js (16.x or higher recommended)
npm (bundled with Node.js)
React.js
Install React dependencies:

npm install
Dataset
The dataset includes labeled potato plant images divided into three primary categories:

Potato___Early_blight
Potato___Late_blight
Potato___Healthy
Each image is resized to 256x256 pixels for uniformity during preprocessing. Organize your dataset as follows:

dataset/
        Potato___Early_blight/
        Potato___Late_blight/
        Potato___Healthy/
   
Model Architecture
The deep learning model is built using a Convolutional Neural Network (CNN).

Rescaling: Normalizes pixel values to the range [0, 1].
Convolutional Layers: Extracts image features like edges, textures, etc.
Pooling Layers: Reduces spatial dimensions to focus on important features.
Flattening: Converts 2D data to 1D for the dense layers.
Dense Layers: Classifies the image into the appropriate category.
Training the Model
The model is generated and trained using the potato7.py file.

Steps:
Load and Augment Data: Use ImageDataGenerator to preprocess and augment the dataset.
Compile the Model: Use the Adam optimizer and categorical crossentropy loss.
Train the Model: Fit the model to the training data.
Run the following command to train the model and generate the .h5 file:

bash
python potato7.py
Running the Project
Step 1: Start the Backend Server
The mainfastapi.py file sets up a FastAPI server to serve the trained model for predictions. To run the backend server, use:

bash
python mainfastapi.py
By default, the server will start on http://localhost:8000. The React app communicates with this server to make predictions.

Step 2: Start the React Web App
Navigate to the project directory and install dependencies:
bash
npm install
Start the React development server:
bash
npm start
Open the app in your browser at http://localhost:3000.
React Web App
Features
Image Upload: Users can upload images of potato plants for disease classification.
Disease Predictions: Results are fetched from the FastAPI backend and displayed to the user.
Prevention Tips: Farmers receive disease-specific prevention and treatment recommendations.
The React app uses the FastAPI server to fetch predictions. Ensure that both the backend and frontend servers are running simultaneously.

Acknowledgments
TensorFlow & Keras: Used for building the deep learning model.
FastAPI: A lightweight framework for serving the model predictions.
React Documentation: Reference for developing the web application.
Potato Disease Dataset from kaggle: The dataset used for training and evaluating the model.
CodeBasics: Inspiration for the classification model architecture.

![image alt](https://github.com/Collins030/Potato-disease-detection-app/blob/main/earlyblightconf.png?raw=true)
