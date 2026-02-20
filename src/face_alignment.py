import cv2
import numpy as np

class FaceAligner:
    def __init__(self, desired_face_width=256):
        self.desired_face_width = desired_face_width

    def align(self, image, face_landmarks):
        # Assuming face_landmarks is a dictionary with 'left_eye' and 'right_eye'
        left_eye = face_landmarks['left_eye']
        right_eye = face_landmarks['right_eye']
        
        # Calculate the angle between the eyes
        eye_center = ((left_eye[0] + right_eye[0]) // 2, (left_eye[1] + right_eye[1]) // 2)
        dy = right_eye[1] - left_eye[1]
        dx = right_eye[0] - left_eye[0]
        angle = np.degrees(np.arctan2(dy, dx))

        # Calculate the desired right eye x-coordinate assuming a fixed distance
        desired_right_eye_x = 1.0 - 0.35  # 0.35 is a common proportion
        desired_face_height = 256
        desired_eye_width = desired_right_eye_x * self.desired_face_width

        # Calculate scale
        dist = np.sqrt((dx ** 2) + (dy ** 2))
        desired_dist = desired_eye_width - face_landmarks['eye_distance']
        scale = desired_dist / dist

        # Get the rotation matrix
        M = cv2.getRotationMatrix2D(eye_center, angle, scale)
        M[0, 2] += (desired_face_width / 2) - eye_center[0]
        M[1, 2] += (desired_face_height / 2) - eye_center[1]

        # Apply the affine transformation
        aligned_face = cv2.warpAffine(image, M, (self.desired_face_width, desired_face_height))
        return aligned_face

# Example usage
if __name__ == '__main__':
    # Load image
    image = cv2.imread('face.jpg')
    face_landmarks = {'left_eye': (30, 30), 'right_eye': (60, 30), 'eye_distance': 30}
    aligner = FaceAligner()
    aligned_face = aligner.align(image, face_landmarks)
    cv2.imwrite('aligned_face.jpg', aligned_face)