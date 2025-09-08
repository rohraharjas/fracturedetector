import numpy as np
import joblib 
from PIL import Image

categories = {0:'Avulsion fracture',
 1:'Comminuted fracture',
 2:'Fracture Dislocation',
 3:'Greenstick fracture',
 4:'Hairline Fracture',
 5:'Healthy Bone',
 6:'Impacted fracture',
 7:'Longitudinal fracture',
 8:'Oblique fracture',
 9:'Pathological fracture',
 10:'Spiral Fracture'}

class FractureDetector:
    def __init__(self, model_path="Model.pkl"):
        # Load the model once
        self.model = joblib.load(model_path)

    def preprocess(self, img: Image) -> np.ndarray:
        """Resize image to 256x256 RGB and flatten to model input shape."""
        img = img.convert("RGB").resize((256, 256))
        img_np = np.array(img, dtype=np.float32) / 255.0  # normalize
        img_np = img_np.flatten().reshape(1, -1)          # 1 sample
        return img_np

    def predict(self, img: Image) -> str:
        """Predict fracture category for a given image."""
        img_np = self.preprocess(img)
        prediction = self.model.predict(img_np)[0]
        category = categories[prediction]
        return category

    def hasFracture(self, img: Image) -> bool:
        return self.predict(img) != "Healthy Bone"

    def fractureType(self, img: Image) -> str:
        category = self.predict(img)
        return "" if category == "Healthy Bone" else category