from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

# Allow frontend to communicate with backend
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory to serve images
app.mount("/static", StaticFiles(directory="C:/Users/User/Pictures/pesticide"), name="static")

# Load the trained model
MODEL = tf.keras.models.load_model("C:/Users/User/OneDrive/Documents/potato_disease_detection/model/potato_model7.h5")

# Define class names and recommendations
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
RECOMMENDATIONS = {
    "Early Blight": {
        "solution": "Use Mancozeb fungicide. Apply early in the morning.",
        "chemicals": [
            {
                "name": "Mancozeb",
                "dosage": "1.5g per liter of water",
                "procedure": "Spray on infected areas weekly for 2-3 weeks.",
                "image_url": "/static/Mancozeb.jpeg"  # Replace with actual image name
            }
        ]
    },
    "Late Blight": {
        "solution": "Use Chlorothalonil fungicide as a preventive measure.",
        "chemicals": [
            {
                "name": "Chlorothalonil",
                "dosage": "2g per liter of water",
                "procedure": "Spray thoroughly on leaves and stems after rain.",
                "image_url": "/static/Chlorothalonil.jpeg"  # Replace with actual image name
            }
        ]
    },
    "Healthy": {
        "solution": "No action required. Maintain regular crop monitoring.",
        "chemicals": []
    }
}

# Helper function to read and process the uploaded image
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    # Perform prediction
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    # Include recommendations in the response
    recommendations = RECOMMENDATIONS[predicted_class]

    return {
        "class": predicted_class,
        "confidence": float(confidence),
        "recommendation": recommendations
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

