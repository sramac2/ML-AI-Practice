class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def shout(self):
        print('custom exception: ', self.msg)


try:
    raise CustomException('sdaddddad')
except CustomException as e:
    print(e.shout())
