## FractureDetector Package

FractureDetector Package is a CNN model that checks if a X-Ray image shows a fracture.

Additionally it also classifies a detected fracture(if any) into the following categories:

Avulsion fracture,
Comminuted fracture,
Fracture Dislocation,
Greenstick fracture,
Hairline Fracture,
Healthy Bone,
Impacted fracture,
Longitudinal fracture,
Oblique fracture,
Pathological fracture,
Spiral Fracture.

## Installation

You can install FractureDetector from PyPi using pip or pip3 as

`pip install fracture_detector`

or

`pip3 install fracture_detector`

## Modules

The FractureDetector package contains 1 module(utils) that contains a class that contains the FractureDetector class.

`from fracture_detector import fracture_detector.utils.FractureDetector`

The Fracture detector class takes image object and checks it for any fractures.

`f_detector = FractureDetector(img)#img is the X-Ray image`

It returns a FractureDetector object.

## Attributes and Functions

1) FractureDetector.category: A string of the category of the X-Ray(Avulsion fracture, Comminuted fracture, Fracture Dislocation, Greenstick fracture, Hairline Fracture, Healthy Bone, Impacted fracture, Longitudinal fracture, Oblique fracture, Pathological fracture, Spiral Fracture.)

2) FractureDetector.hasFracture(): Returns a boolean value. True if X-Ray shows a fracture, False otherwise.

3) FractureDetector.fractureType(): Returns a string representing the type of Fracture.

If no fracture detected returns "".
