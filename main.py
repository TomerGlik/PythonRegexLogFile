import re
from datetime import datetime

if __name__ == '__main__':
    log = open("exam.log")
    # content = log.read()
    print(open("exam.log").read().split("\n")[0].split("\t"))
    print(sum([1 for line in open("exam.log").read().split("\n") if line.split("\t")[1] == "ERROR"]))

    counter = 0
    for line in open("exam.log").read().split("\n"):
        possible_transaction = line.split("\t")[4]
        start = re.search("transaction \d+ begin", possible_transaction)
        if start:
            counter += 1
        end = re.search("end transaction \d+", possible_transaction)
        if end:
            counter += 1
    print(counter / 2)

    transaction_dict = {}
    for line in open("exam.log").read().split("\n"):
        possible_transaction = line.split("\t")[4]
        start = re.search("transaction (\d+) begin", possible_transaction)
        if start:
            transaction_dict[start.group(1)] = [
                datetime.strptime(line.split("\t")[0].replace("-", ""), '%d%m%Y %H:%M:%S.%f')]
        end = re.search("end transaction (\d+)", possible_transaction)
        if end:
            transaction_dict[end.group(1)].append(
                datetime.strptime(line.split("\t")[0].replace("-", ""), '%d%m%Y %H:%M:%S.%f'))
    sum = 0
    for transaction, details in transaction_dict.items():
        diff = details[1] - details[0]
        sum += diff.total_seconds()*1000
    sum/len(transaction_dict.items()) # this is the result

    # print(fastest_id)
    # sum([(details[1] - details[0]).total_seconds() * 1000 for _, details in transaction_dict.items()]) / len(
    #     transaction_dict.items())

    # date_time_obj = datetime.strptime(transaction_dict["17018"][0].replace("-",""), '%d%m%Y %H:%M:%S.%f')
