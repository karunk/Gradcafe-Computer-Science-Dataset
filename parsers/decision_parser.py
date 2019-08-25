from datetime import datetime

REJECTED = "Rejected"
ACCEPTED = "Accepted"


class DecisionParser(object):

    def __init__(self, raw_row):
        self.raw_row = raw_row

    def parse_decision(self):
        data = self.raw_row.find_all(True, {'class': ['tcol3']})[0].getText()
        if ACCEPTED in data:
            return ACCEPTED
        elif REJECTED in data:
            return REJECTED
        else:
            return "Others"

    def parse_decision_date(self):
        date = self.raw_row.find_all(True, {'class': ['tcol3']})[0].getText().strip().split('on')[-1].split(' ')
        date = date[1]+" "+date[2]+" "+date[3]
        date = datetime.strptime(date, '%d %b %Y').strftime('%Y-%m-%d')
        return date

