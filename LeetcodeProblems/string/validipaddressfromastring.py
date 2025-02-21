# Input: “255678166”
# Output: [“25.56.78.166”, “255.6.78.166”, “255.67.8.166”, “255.67.81.66”]
# Explanation: These are the only valid possible IP addresses.

# Input: “25505011535”
# Output: []
# Explanation: We cannot generate a valid IP address with this string.

def restore_ip_addresses(s):
    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            result.append(".".join(path))
            return
        if len(path) >= 4:
            return

        for end in range(start + 1, min(start + 4, len(s) + 1)):  # 1 to 3 digit segments
            segment = s[start:end]
            if (len(segment) > 1 and segment[0] == "0") or int(segment) > 255:
                continue  # Skip invalid segments
            backtrack(end, path + [segment])

    result = []
    backtrack(0, [])
    return result

# Test cases
print(restore_ip_addresses("255678166"))  # Expected: ["25.56.78.166", "255.6.78.166", "255.67.8.166", "255.67.81.66"]
print(restore_ip_addresses("25505011535"))  # Expected: []
