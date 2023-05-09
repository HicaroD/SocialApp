class PostEntity:
    pass


class PhotoPostEntity(PostEntity):
    def __init__(self, photo: str) -> None:
        self.photo = photo


class VideoPostEntity(PostEntity):
    def __init__(self, video: str) -> None:
        self.video = video


class TextPostEntity(PostEntity):
    def __init__(self, text: str) -> None:
        self.text = text
