def passenger_data(path):
    """
    Converts txt file of passenger data into a formatted python list object

    :param path: Path of passenger txt file
    :return: List of formatted data of type matrix/nested list
    """
    final_output = []
    f = open(path, "r+", encoding="utf-8")
    for i in f:
        j = i.strip().split(",")
        formatted_row = []
        for k in j:
            try:
                value = float(k)
            except ValueError:
                value = str(k)
            formatted_row.append(value)
        final_output.append(formatted_row)
    f.close()
    return final_output
    # funny codegolfed one-line version
    # return [i.strip().split(",") for i in open(path, "r+", encoding="utf-8")]


if __name__ == "__main__":
    print(passenger_data("passenger_data_v1.txt"))
    print(passenger_data("passenger_data_v2.txt"))
    print(passenger_data("passenger_data_v3.txt"))