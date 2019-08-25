import csv


class CsvMaker(object):
    def make(self, data_dict):
        """

        :type data_dict: {
            'date': '2019-08-24',
            'university': Florida Gulf Coast University',
            'program': 'Computer Science',
            'decision': True
        }
        """
        keys = data_dict[0].keys()
        with open('gradcafe.csv', 'wb') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data_dict)