import json

with open("new_kv_map.json", "r") as kv_file:
    with open("imgur_report.csv", "r") as report_file:
        kv_data = json.loads(kv_file.read())
        line_number = 1
        for line in report_file.readlines()[1:]:
            # headers: timestamp, request_type, position, creative_type, kv_value
            # indexes: 0,         1,            2,        3,             4
            rows = [i.strip() for i in line.split(",")]
            creative_type = rows[3]
            if creative_type in kv_data:
                kv_value = rows[4]
                if kv_value not in kv_data[creative_type]:
                    print(f"{kv_value} was not present in the current kv mapping, creative_type: {creative_type}, line # {line_number}")
            line_number += 1
