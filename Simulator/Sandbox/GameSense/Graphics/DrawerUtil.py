
import os
import pygame

class DrawerUtil:

    @staticmethod
    def get_image_dir():
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ImageData")
    # def get_image_dir

    @staticmethod
    def create_image(image_name):
        return pygame.image.load(os.path.join(DrawerUtil.get_image_dir(), image_name)).convert_alpha()
    # create_image

    @staticmethod
    def calc_half_size(image):
        return (image.get_width()/2, image.get_height()/2)
    # calc_half_size

    @staticmethod
    def get_priority_from_setting(draw_setting):
        return draw_setting["Priority"] if draw_setting.get("Priority") else 0
    # def get_priority_from_setting
