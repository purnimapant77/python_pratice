def run_length_encode(data):
    encoding = ""
    prev = data[0]
    count = 1
    for i in range(1,len(data)):
        if data[i] == prev:
            count += 1
        else:
            encoding += str(count) + prev
            prev = data[i]
            count = 1
    encoding += str(count) + prev
    return encoding

data = "PURNIMAPANT"
print("Original:", data)
print("Encoded:", run_length_encode(data))