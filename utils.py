 

from typing import List

import cv2
import numpy as np
from object_detector import Detection

_MARGIN = 10  # pixels
_ROW_SIZE = 10  # pixels
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_TEXT_COLOR = (100, 80, 255)  # blue 
color=np.random.uniform(0,255,size=(2,3))
dict_lables={"vis":0,"ecrou":1}


def visualize(
    image: np.ndarray,
    detections: List[Detection],
) -> np.ndarray:
  """Draws bounding boxes on the input image and return it.
    
  Args:
    image: The input RGB image.
    detections: The list of all "Detection" entities to be visualize.

  Returns:
    Image with bounding boxes.
  """
    
  for detection in detections:
    
    category = detection.categories[0]
    class_name = category.label
    # Draw bounding_box
    start_point = detection.bounding_box.left, detection.bounding_box.top
    end_point = detection.bounding_box.right, detection.bounding_box.bottom
    #cv2.rectangle(image, start_point, end_point, _TEXT_COLOR, 3)
    cv2.rectangle(image, start_point, end_point, color[int(dict_lables[class_name])], 1)

    # Draw label and score
    probability = round(category.score, 2)
    result_text = class_name + ' (' + str(probability) + ')'
    text_location = (_MARGIN + detection.bounding_box.left,
                     _MARGIN + _ROW_SIZE + detection.bounding_box.top)
    location_text=(start_point[0]+5,start_point[1]-5)
    cv2.putText(image, result_text, location_text, cv2.FONT_HERSHEY_PLAIN,
                _FONT_SIZE,color[int(dict_lables[class_name])], _FONT_THICKNESS)

  return image
