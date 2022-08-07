from json import JSONDecodeError
from typing import TypedDict

import json
import uuid


# found_aps looks inside the data to determine if APS data is present within the dictionary
def found_aps(d: TypedDict) -> (bool, TypedDict):
    try:
        aps = d["imp"][0]["ext"]["aps"]
        if aps is not None:
            return True, aps
        return False, None
    except Exception as e:
        return False, None


# get_request_type looks inside the data to determine the type of request the publisher made to Nimbus
def get_request_type(d: TypedDict) -> str:
    if "banner" in d["imp"][0] and "video" in d["imp"][0]:
        return "static.video"
    elif "banner" in d["imp"][0]:
        return "static"
    elif "video" in d["imp"][0]:
        return "video"
    return "unknown"


# get_aps_creative_type looks inside the data to determine the type of ad APS returned to Nimbus
def get_aps_creative_type(d: TypedDict) -> str:
    for aps in d:
        if len(aps["amzn_vid"]) > 0:
            return "video"
    return "static"


# get_aps_kv looks inside the data to determine the price APS bid at
def get_aps_kv(d: TypedDict) -> str:
    for aps in d:
        if len(aps["amznslots"]) > 0:
            return aps["amznslots"][0]


# get_request_position looks inside the data to see the position name the publisher assigned to the request
def get_request_position(d: TypedDict) -> str:
    return d["imp"][0]["ext"]["position"]


with open("merged.csv", 'r') as f:
    target_text = "web: "
    request_set = set()

    # print out headers to copy and paste out of terminal as a csv
    print("timestamp,request_type,position,creative_type,kv_value")
    for line in f.readlines():
        # remove newlines from the end of the string as well as any spaces
        line = line.strip()
        start_position = line.find(target_text)
        if start_position > -1:
            # clean up the log data so that it is proper JSON again
            dirty_text = line[start_position + len(target_text):len(line) - 1]
            clean_text = dirty_text.replace('""', '"')
            # load in the raw log data
            try:
                log_data = json.loads(clean_text)
            except JSONDecodeError as e:
                print(clean_text)
                raise e

            # load in the raw request data which is still a string within the log data
            request_data = json.loads(log_data["request_body"])
            # remove duplicates from the data set
            requests_data_hash = uuid.uuid5(uuid.NAMESPACE_OID, log_data["request_body"])
            if requests_data_hash in request_set:
                continue
            request_set.add(requests_data_hash)

            # determine if the dictionary contains any APS data
            ok, aps_data = found_aps(request_data)
            if ok:
                # extract data from the request data and aps data
                time_stamp = log_data["ts"]
                request_type = get_request_type(request_data)
                position = get_request_position(request_data)

                creative_type = get_aps_creative_type(aps_data)
                kv_value = get_aps_kv(aps_data)

                print(f"{time_stamp}, {request_type}, {position}, {creative_type}, {kv_value}")
