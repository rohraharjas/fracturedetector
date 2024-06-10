import numpy as np
import joblib 
from PIL import Image
model = joblib.load('Model.pkl')

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
    def __init__(self, img: Image):
        img_np = np.concatenate(img.numpy())
        self.category = categories[np.argmax(model.predict(img_np))]
    
    def hasFracture(self):
        return self.category != 'Healthy Bone'
    
    def fractureType(self):
        if(not self.hasFracture()):
            return ""
        return self.category