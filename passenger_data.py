def passenger_data(path):
    """
    Converts txt file of passenger data into a formatted python list object

    :param path: Path of passenger txt file
    :return: List of formatted data of type matrix/nested list
    """
    final_output = []
    f = open(path, "r+", encoding="utf-8")
    for i in f:
        final_output.append(i.strip().split(","))
    f.close()
    return final_output
    # funny codegolfed one-line version
    # return [i.strip().split(",") for i in open(path, "r+", encoding="utf-8")]

    # final_output = []
    # with open(path, "r+", encoding="utf-8") as f:
    #     for i in f:
    #         final_output.append(i.strip().split(","))
    #     return final_output
