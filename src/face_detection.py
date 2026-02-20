import dlib
import face_recognition

class FaceDetection:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()

    def detect_faces(self, image):
        # Convert the image to a format suitable for face detection
        rgb_image = face_recognition.load_image_file(image)
        # Detect faces in the image
        faces = self.detector(rgb_image)
        return faces

    def draw_faces(self, image, faces):
        # This method will allow drawing rectangles around detected faces
        import cv2
        for face in faces:
            x, y, w, h = (face.left(), face.top(), face.width(), face.height())
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return image
