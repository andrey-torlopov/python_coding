class ScreenConfig:
    def __init__(self,
                 width: int = 640,
                 height: int = 800,
                 title: str = "Tetris", fps: int = 60
                 ) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.fps = fps
        self.black = (43, 43, 43)
        self.background = (240, 240, 240)
        self.top_offset = 50

    @property
    def screen_size(self) -> tuple[int, int]:
        return (self.width, self.height)
