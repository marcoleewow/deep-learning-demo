import argparse


class Options():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="parser for PyTorch-Style-Transfer")

        # demo
        self.parser.add_argument("--style-folder", type=str, default="images/",
                                 help="path to style-folder")
        self.parser.add_argument("--style-size", type=int, default=512,
                                 help="size of style-image, default is the original size of style image")
        self.parser.add_argument("--cuda", type=int, default=0,
                                 help="set it to 1 for running on GPU, 0 for CPU")
        self.parser.add_argument("--record", type=int, default=0,
                                 help="set it to 1 for recording into video file")
        self.parser.add_argument("--model", type=str, default='models/21styles.model',
                                 help="saved model to be used for stylizing the image")
        self.parser.add_argument("--ngf", type=int, default=128,
                                 help="number of generator filter channels, default 128")
        self.parser.add_argument("--demo-size", type=int, default=480,
                                 help="demo window height, default 480")

    def parse(self):
        return self.parser.parse_args()