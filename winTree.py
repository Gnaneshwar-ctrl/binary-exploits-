import os 
import argparse 

class directoryTraversal:
    def __init__(self):

        self.path = ''

    @staticmethod
    def getArgs():
        parser = argparse.ArgumentParser(description="scan all special files")
        parser.add_argument("path" , help="path of folder")

        return parser.parse_args()

    def scanPath(self):
        with os.scandir(self.path) as iterObj:
            for eachEntry in iterObj:
                print(eachEntry)
    
    def main(self):
        args = self.getArgs()
        self.path = args.path

        self.scanPath()


if __name__ == '__main__':
    instance = directoryTraversal()
    instance.main()