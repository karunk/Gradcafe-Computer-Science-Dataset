class CommentParser(object):

    def __init__(self, row):
        self.raw_row = row

    def parse_comment(self):
        return self.raw_row.find_all(True, {'class': ['tcol6']})[0].getText()
