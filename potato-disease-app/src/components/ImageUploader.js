import React, { useState } from "react";
import { predictImage } from "../api";

const ImageUploader = ({ onUpload }) => {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleImageChange = (event) => {
    setSelectedImage(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (selectedImage) {
      const prediction = await predictImage(selectedImage);
      onUpload(URL.createObjectURL(selectedImage), prediction);
    }
  };

  return (
    <div className="image-uploader">
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleImageChange} />
        <button type="submit">Upload and Predict</button>
      </form>
    </div>
  );
};

export default ImageUploader;
