class Father:
    def __init__(self, name):
        self.name = name


class Son(Father):
    def __init__(self, name, hobby):
        super(Son, self).__init__(name)
        self.hobby = hobby


if __name__ == '__main__':
    jacob = Son('jacob', 'badminton')
    print('name::{}, hobby::{}'.format(jacob.name, jacob.hobby))