from datetime import datetime

from parsers.comment_parser import CommentParser
from parsers.credential_parser import CredentialParser
from parsers.decision_parser import DecisionParser
from parsers.program_parser import ProgramParser


class Parser:

    def __init__(self):
        self.parsed_data = []

    def parse(self, table):
        for row in table:
            program_parser = ProgramParser(row.find_all(True, {'class': ['tcol2']})[0].getText())
            decision_parser = DecisionParser(row)
            credential_parser = CredentialParser(row)
            comment_parser = CommentParser(row)
            try:
                parsed_row = {
                    'university': row.find_all(True, {'class': ['instcol']})[0].getText(),
                    'major': program_parser.get_program_name(),
                    'season': program_parser.get_session(),
                    'undergrad_gpa': credential_parser.parse_gpa(),
                    'gre_verbal': credential_parser.parse_gre_verbal(),
                    'gre_quant': credential_parser.parse_gre_quant(),
                    'gre_awa': credential_parser.parse_gre_awa(),
                    'degree': program_parser.get_course_type(),
                    'term_year': program_parser.get_term_year(),
                    'decision': decision_parser.parse_decision(),
                    'date_added': (
                        datetime.strptime(row.find_all(True, {'class': ['tcol5']})[0].getText(), '%d %b %Y').strftime(
                            '%Y-%m-%d')),
                    'date_of_result': decision_parser.parse_decision_date(),
                    'applicant_status': credential_parser.parse_applicant_status(),
                    'comment': comment_parser.parse_comment()
                }

                parsed_row = {k: self.__parse(v) for k, v in parsed_row.items()}
                self.parsed_data.append(parsed_row)
            except:
                continue
        return self.parsed_data

    @staticmethod
    def __parse(data):
        if data is None:
            return ""
        else:
            return data.encode('ascii', 'ignore').decode('ascii')
