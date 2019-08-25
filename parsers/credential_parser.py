AMERICAN = "American"
INTERNATIONAL_WITH_US_DEGREE = "International with US degree"
INTERNATIONAL_WITHOUT_US_DEGREE = "International without US degree"
OTHER = "Other"
UNKNOWN = "Unknown"


class CredentialParser(object):
    def __init__(self, raw_row):
        self.raw_row = raw_row

    def parse_applicant_status(self):
        status = self.raw_row.find_all(True, {'class': ['tcol4']})[0].getText()
        if status == 'A':
            return AMERICAN
        elif status == 'U':
            return INTERNATIONAL_WITH_US_DEGREE
        elif status == 'I':
            return INTERNATIONAL_WITHOUT_US_DEGREE
        elif status == '0':
            return OTHER
        else:
            return UNKNOWN

    def parse_cred_data(self):
        data = []
        for info in self.raw_row.find_all(True, {'class': ['extinfo']}):
            for _strong in info.find_all("strong"):
                data.append(_strong.next_sibling.lstrip(':').strip())
        return data

    def parse_gpa(self):
        data = self.parse_cred_data()
        if len(data) > 0:
            return data[0]
        else:
            return ""

    def parse_gre(self):
        data = self.parse_cred_data()
        if len(data) > 2:
            return data[1]
        else:
            return ""

    def parse_gre_verbal(self):
        data = self.parse_gre().split('/')
        if len(data) > 0:
            return data[0]
        else:
            return ""

    def parse_gre_quant(self):
        data = self.parse_gre().split('/')
        if len(data) > 1:
            return data[1]
        else:
            return ""

    def parse_gre_awa(self):
        data = self.parse_gre().split('/')
        if len(data) > 2:
            return data[2]
        else:
            return ""
