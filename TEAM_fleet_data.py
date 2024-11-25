"""
Converts a txt file of fleet data into a sanitized python 2D list

Thurs44, DS Project 1
"""

def fleet_data(path):
    """
    Converts txt file of fleet data into a formatted python list object

    :param path: Path of fleet txt file
    :return: List of formatted data of type matrix/nested list
    """
    # DANGER: THIS SPECIFIC DATA FILE IS UTF-16 FORMATTED FOR SOME REASON!!!
    # TODO: ADD HANDLING FOR UTF 8 i.e THE PROPER WAY TO FORMAT TEXT FILES
        # done 👍
    def read_file(path, encoding):
        """
        Tests reading a file with a specified encoding

        :param path: Path of fleet txt file
        :param encoding: What encoding to use. Has to be here because, for some reason, the fleet_data is in UTF-16.
        :return: Either error or a 2D List of fleet data
        """
        final_output = []
        f = open(path, "r+", encoding=encoding)
        for i in f:
            row = i.strip().split(",")
            formatted_row = []
            for j in row:
                try:
                    # try to convert to float first
                    value = float(j)
                except ValueError:
                    # if fail, it's a string
                    value = str(j)
                formatted_row.append(value)
            final_output.append(formatted_row)
        f.close()
        return final_output

    try:
        final_output = read_file(path, "utf-8")
    except UnicodeDecodeError:
        final_output = read_file(path, "utf-16")

    return final_output
    # funny codegolfed one-line version
    # return [i.strip().split(",") for i in open(path, "r+", encoding="utf-16")]




if __name__ == "__main__":
    print(fleet_data("fleet_data.txt"))

# RIP version using 'with' :(
# you will be remembered...
#     final_output = []
#     with open(path, "r+", encoding="utf-16") as f:  # add handling for utf 8
#         for i in f:
#             final_output.append(i.strip().split(","))
#         return final_output
