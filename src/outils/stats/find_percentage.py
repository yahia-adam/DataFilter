"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""


# find_percentage function used to find the percentage number of bool fields in csv, json, xml and yaml files and
# returns 2 percentage values
def find_percentage(content):
    percentage_true = 0
    percentage_false = 0
    # if content is a list :
    if isinstance(content, list):
        # if content[0] is a list -> so it's a csv file
        if content and isinstance(content[0], list):
            headers = content[0]
            # print(headers)
            boolean_field_cpt = {header: {'True': 0, 'False': 0} for header in headers}
            # print(boolean_field_cpt)

            # count true / false for each field
            for row in content[1:]:
                for index, value in enumerate(row):
                    if value.lower() == 'true':
                        boolean_field_cpt[headers[index]]['True'] += 1
                    elif value.lower() == 'false':
                        boolean_field_cpt[headers[index]]['False'] += 1

            # print(boolean_field_cpt)

            # calcul des pourcentages
            for header, counts in boolean_field_cpt.items():
                total_count = counts['True'] + counts['False']
                if total_count != 0:
                    # print("hi")
                    percentage_true = (counts['True'] / total_count) * 100
                    percentage_false = (counts['False'] / total_count) * 100
                    break
                else:
                    percentage_true = 0
                    percentage_false = 0

        # if content[0] is a dictionary -> so it's a json file
        elif isinstance(content[0], dict):
            boolean_field_cpt = {}

            # count true / false for each field
            for item in content:
                for key, value in item.items():
                    if isinstance(value, bool):
                        if key not in boolean_field_cpt:
                            boolean_field_cpt[key] = {'True' : 0, 'False' : 0}
                        if value:
                            boolean_field_cpt[key]['True'] += 1
                        else:
                            boolean_field_cpt[key]['False'] += 1

            # calcul des pourcentages
            for fields, counts in boolean_field_cpt.items():
                total_count = counts['True'] + counts['False']
                if total_count != 0:
                    # print("hi")
                    percentage_true = (counts['True'] / total_count) * 100
                    percentage_false = (counts['False'] / total_count) * 100
                    break
                else:
                    percentage_true = 0
                    percentage_false = 0

    # fi content is a dictionary (for yaml file)
    elif isinstance(content, dict):
        boolean_field_cpt = {}

        # counting ture / false for each field
        for key, value in boolean_field_cpt.items():
            if isinstance(value, bool):
                boolean_field_cpt[key] = {'True' : 0, 'False' : 0}

                if value:
                    boolean_field_cpt[key]['True'] += 1
                else:
                    boolean_field_cpt[key]['False'] += 1

        for fields, counts in boolean_field_cpt.items():
            total_count = counts['True'] + counts['False']
            if total_count != 0:
                # print("hi")
                percentage_true = (counts['True'] / total_count) * 100
                percentage_false = (counts['False'] / total_count) * 100
                break
            else:
                percentage_true = 0
                percentage_false = 0

    return percentage_true, percentage_false


