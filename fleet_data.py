def fleet_data(path):
    """
    Converts txt file of fleet data into a formatted python list object

    :param path: Path of fleet txt file
    :return: List of formatted data of type matrix/nested list
    """
    # DANGER: THIS SPECIFIC DATA FILE IS UTF-16 FORMATTED FOR SOME REASON!!!
    # TODO: ADD HANDLING FOR UTF 8 i.e THE PROPER WAY TO FORMAT TEXT FILES
    final_output = []
    f = open(path, "r+", encoding="utf-16")  # add handling for utf 8
    for i in f:
        final_output.append(i.strip().split(","))
    f.close()
    return final_output
    # funny codegolfed one-line version
    # return [i.strip().split(",") for i in open(path, "r+", encoding="utf-16")]


# RIP version using 'with' :(
#     final_output = []
#     with open(path, "r+", encoding="utf-16") as f:  # add handling for utf 8
#         for i in f:
#             final_output.append(i.strip().split(","))
#         return final_output
