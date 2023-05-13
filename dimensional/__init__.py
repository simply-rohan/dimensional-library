import pygame
import math

class Camera:
    FOCAL_LENGTH = 1
    def __init__(self, objs: list = [], position: pygame.Vector3 = None, forward: pygame.Vector = None):
        """_summary_

        Args:
            objs (list, optional): A pointer to a list containing all `Models`. Defaults to [].
            position (pygame.Vector3, optional): A vector representing the camera's physical position. Defaults to 0, 0, 0.
            forward (pygame.Vector, optional): A vector pointing to the forward facing direction. Defaults to 0, 0, 0.
        """
        self.objs = objs
        
        self.position = position if position is not None else pygame.Vector3(0, 0, 0)
        self.forward = forward if forward is not None else pygame.Vector3(0, 0, 0)
        
    def _project(self, point):
        x, y, z = point
        return x * (self.FOCAL_LENGTH/z), y * (self.FOCAL_LENGTH/z)

    def render(self, screen):
        """
        """
        faces = []
        for obj in self.objs:
            for face in self.faces:
                f = []
                _, _, z = zip(*face) 
                for point in face:
                    p = pygame.Vector3(point)
                    # Transforms
                    # Locally
                    p += obj.position
                    p.rotate_ip(obj.rotation)
                    
                    # Camera
                    p += self.position
                    p.rotate_ip(self.forward)
                    f.append(p)
                faces.append((f, obj.color, min(z)))
        
                    
        # TODO: Z-Sort 

        for face, color, _ in faces:           
            projected_points = [self._project(p) for p in face]
            pygame.draw.polygon(screen, color, projected_points, 2)


class Model:
    def __init__(self, faces, scale) -> None:
        self.raw_faces = faces

        self.faces = [
            [[axis * scale for axis in vertex] for vertex in face]
            for face in self.raw_faces
        ]

        self.position = [0, 0, 0]
        self.rotation = [0, 0, 0]

        self.color = (200, 125, 130)