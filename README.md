## FractureDetector

FractureDetector is a CNN model that checks if a X-Ray image shows a fracture.

Additionally it also classifies a detected fracture(if any) into the following categories:

- Avulsion fracture,
- Comminuted fracture,
- Fracture Dislocation,
- Greenstick fracture,
- Hairline Fracture,
- Healthy Bone,
- Impacted fracture,
- Longitudinal fracture,
- Oblique fracture,
- Pathological fracture,
- Spiral Fracture.

## Installation

1) To get started clone this github repo

`git clone https://github.com/rohraharjas/fracturedetector.git`


2) Install dependencies: Create a virtual environment and run the setup.py script by

`pip install -e .`

3) Train the model: Run the notebook at `fracturedetector/fracture_detector/Model.ipynb`

4) Start the API service at app.py by running

`uvicorn app:app --reload`

## API Usage

The service exposes the following endpoints. All endpoints accept a single file upload (multipart/form-data) named file.

`POST /predict`

Description: Returns the predicted category for the uploaded X-ray.
Response example:
```json
{
  "prediction": "Oblique fracture"
}
```

`POST /has-fracture`
Description: Checks whether the X-ray contains a fracture.
Response:

```json
{
    "has_fracture": true
}
```

`POST /fracture-type`
Description: Returns the type of fracture if detected, otherwise an empty string.
Response:
```json
{
    "fracture_type": "Hairline Fracture"
}
```

> **Disclaimer:** This project is for research/demonstration only. **Not for clinical use.** Do not use predictions from this model as medical advice — always consult a licensed healthcare professional.
