class Colors:
    BACKGROUND = (0, 0, 0)
    RED = (255, 51, 51)
    ORANGE = (255, 153, 51)
    YELLOW = (255, 255, 51)
    GREEN = (102, 255, 178)
    BLUE = (51, 51, 255)
    PINK = (255, 51, 153)
    GREY = (160, 160, 160)

    @classmethod
    def get_colors(cls):
        return [cls.BACKGROUND, cls.RED, cls.ORANGE, cls.YELLOW, cls.GREEN, cls.BLUE, cls.PINK, cls.GREY]