---
title: 'My First Time Using Neovim'
excerpt: ' All new technologies have a beginning, and here is mine. This markdown was done with neovim.'
coverImage: '/assets/blog/hello-world/thumbnail.png'
date: '2020-03-16T05:35:07.322Z'
author:
  name: Tools
  picture: '/assets/blog/authors/Tool.png'
ogImage:
  url: '/assets/blog/hello-world/thumbnail.png'
---

I have always been a fan of productivity, and Primeagen. I have always looked for ways to improve and my development experience more efficient and friendly, as such I landed onto NeoVim. I have tried out Nano, Vim, and Emacs and I have seen the many videos and friends customizing their nvim config. I felt if I were able to create an environment that I am more comfortable working in, I can go blazingly faster.

## Week 1

[![Using Neovim as a newbie](https://img.youtube.com/vi/cK2T1-Dd2Fk/0.jpg)](https://www.youtube.com/watch?v=cK2T1-Dd2Fk)


I have decided to download NeoVim from NeoVim.ion and went through the installation wizard. I then went to github to copy the clone of kickstart link here: https://github.com/nvim-lua/kickstart.nvim The above video is my first time using and recording my experience of editing and exploring some commands on neovim. Feels a lot like vim but better

## Week 2

Creating a compression algorithm

In summary, this code takes an HTML file, encodes its content into binary, compresses the binary data, writes the compressed binary data to a new HTML file, and prints a success message. The compression is done by replacing consecutive digits with a single digit followed by a count of consecutive digits. This process aims to reduce the size of the binary data.

We can do this multiple times to reduce the size of the file even further
```
def html_to_compressed_binary(file_path):
    with open(file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()  # Read the HTML content
    
    binary_data = ''.join(format(ord(char), '08b') for char in html_content)  # Encode HTML content to binary

    result = ""
    count = 1
    for i in range(len(binary_data) - 1):
        if binary_data[i] == binary_data[i + 1]:
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

    compressed_binary = ""
    for index, digit in enumerate(result):
        count = int(digit)
        if index % 2 == 0:
            compressed_binary += '0' * count
        else:
            compressed_binary += '1' * count

    byte_data = bytes(int(compressed_binary[i:i+8], 2) for i in range(0, len(compressed_binary), 8))
    with open("new.html", "wb") as file:
        file.write(byte_data)

    print("HTML file 'new.html' has been created successfully.")

file_path = 'index.html'
html_to_compressed_binary(file_path)
```

Of course this is just a simple compression algorithm but I feel that I can write python code decently fast in neovim now.