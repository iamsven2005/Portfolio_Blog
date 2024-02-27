def html_to_binary(file_path):
    with open(file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()  # Read the HTML content
    
    binary_data = ''.join(format(ord(char), '08b') for char in html_content)  # Encode HTML content to binary
    
    return binary_data


file_path = 'index.html' 
binary_content = html_to_binary(file_path) 
print(binary_content)

def binary_to_numbers(binary_string):
    result = ""
    count = 1
    for i in range(len(binary_string) - 1):
        if binary_string[i] == binary_string[i + 1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            else:
                result += "1"
            count = 1

    if count > 1:
        result += str(count)
    else:
        result += "1"
    return int(result)
binary_string = binary_content 
number = binary_to_numbers(binary_string)
print(number)

number = str(number)
concatenated_pattern = ""
for index, digit in enumerate(number):
    count = int(digit)
    if index % 2 == 0:
        concatenated_pattern += '0' * count
    else:
        concatenated_pattern += '1' * count
print(concatenated_pattern)

byte_data = bytes(int(concatenated_pattern[i:i+8], 2) for i in range(0, len(concatenated_pattern), 8))
with open("new.html", "wb") as file:
    file.write(byte_data)

print("HTML file 'new.html' has been created successfully.")

