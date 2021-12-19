def read_input(filename):
    with open(filename, "r") as f:
        return f.read().strip()


def solution(bit_string, startbit):
    # Solution by 'ai_prof'
    # https://topaz.github.io/paste/#XQAAAQAMBwAAAAAAAAAxHMAC0B2Tuh+Zc7rcnUmLYPQvNsm4Tg4i3Zjx2q0nDfSbeEz3deAe3DypB+rhSDyH0m+Kv7tpnOVvFjs43k2hXGyyF/u5PnCx9/MR2UouZnZsl1Fvf5kjeG4kH+D5e9tT6UwvsL2h1WJ3G/6unBKk7qJxlmqmBAfpC3krCj8l88/MjzqjXQVtmwwYN6Kq5/OKQvoJMdXZKdsKPZOnVxHMMD2qB1Ck2NZIq2r+ZHQIWBjnj/2BVUA6u4c67BjiSlLMNQXagsy9+wllPDINTujXIkgLo/3hmApsn7/E04vXucfWYdhDWh8f+Ovkp91w6Wj6lmS3kcmoVgLcBdflDoi7EWnA5bc3cOjSaJ9zMEIcu2BRDtehR8Mz0T65fxSkMtfp9sjkQ9/t0kMcIJMxAdy9sFKFLIO3VM0X24f51aAsfnkUvmC/9c1J8bCsx6gs6qtFEiSJ94aZ7nRfy1m7YG+eR4BycNihtQxXyAHL0mw4bEMstvaCGrZCxt285XbpkWnNYKoF5nTZ7Qfh/JBT65019W7DNMIQJAEBkaxsIBCdsV+xLBSaR+ZbkN54HB13Z69MROYoZwwkazNGSuAScmUFpZs96Z6BfwWITtDLwKeAE0CBIedtWAlc0RJRkHh9z+rIgnanFKU/FiVUyoMAB40xnv6sUty11jWCyRTqDX3H8lNlEvukHsy1JCUiBzGontCjV6WzcDdN2wh4n83SclzuWUprbaeZgwxzPRHPzgTa3uh81QGLAD4TMw8gYZyBfAMmz6NI/P+4YpGw

    index = startbit
    total_version = int(bit_string[index:index+3], 2)
    packet_type_id = int(bit_string[index+3:index+6], 2)
    index += 6

    # If literal value
    if packet_type_id == 4:
        while True:
            index += 5
            # Last packet
            if bit_string[index-5] == '0':
                break
    # If operator (type 1)
    elif bit_string[index] == '0':
        end_index = index + 16 + int(bit_string[index+1:index+16], 2)
        index += 16
        while index < end_index:
            index, v = solution(bit_string, index)
            total_version += v
    # Operator (type 2)
    else:
        np = int(bit_string[index+1:index+12], 2)
        index += 12
        for _ in range(np):
            index, v = solution(bit_string, index)
            total_version += v
    return index, total_version


def main():
    hex_msg = read_input("input.txt")
    bits = "".join(format(int(char, 16), '04b') for char in hex_msg)
    print("Total of version numbers:", solution(bits, 0)[1])


if __name__ == '__main__':
    main()
