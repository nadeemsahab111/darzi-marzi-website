import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Colors replacement
# Gold -> Mulberry
content = content.replace('#D4AF37', '#cc007e')
content = content.replace('#d4af37', '#cc007e')
# secondary gold -> Peach
content = content.replace('#f2ca50', '#ffbd59')

# 2. Drop shadows (old gold was rgb(212,175,55), now Mulberry rgb(204,0,126) or Peach rgb(255,189,89))
content = content.replace('212,175,55', '204,0,126')

# 3. Dark to Light theme replacements
# text colors
content = content.replace('text-white', 'text-black')
content = content.replace('text-gray-200', 'text-gray-700')
content = content.replace('text-gray-300', 'text-gray-600')

# background colors
content = content.replace('bg-black', 'bg-white')
content = content.replace('background-color: #000000', 'background-color: #ffffff')
content = content.replace('bg-[#1A1A1A]', 'bg-[#F8F6F0]')
content = content.replace('bg-[#121212]', 'bg-[#F0EEE6]')
content = content.replace('bg-[#262626]', 'bg-[#FAFAFA]')
content = content.replace('bg-[#0d0d0d]', 'bg-[#ffffff]')

# border colors
content = content.replace('border-[#2C2C2C]', 'border-[#E5E5E5]')
content = content.replace('border-[#333]', 'border-[#CCCCCC]')
content = content.replace('text-[#2C2C2C]', 'text-[#CCCCCC]')

# html class
content = content.replace('<html class="dark"', '<html class="light"')

# specific fixes for visibility on white background
# "selection:text-black" -> "selection:text-white"
content = content.replace('selection:text-black', 'selection:text-white')
content = content.replace('text-[#F8F6F0]', 'text-[#1A1A1A]') # icons that were light are now dark

# 4. Introduce shiny luxurious touch by making text gradients where applicable
# For example, the title DARZI MARZI
content = re.sub(
    r'<span class="text-\[#cc007e\]">MARZI</span>',
    r'<span class="bg-gradient-to-r from-[#cc007e] to-[#ffbd59] text-transparent bg-clip-text">MARZI</span>',
    content
)

# And other highlighted text
content = re.sub(
    r'<span class="text-\[#cc007e\]([^>]*)>([^<]+)</span>',
    r'<span class="bg-gradient-to-r from-[#cc007e] to-[#ffbd59] text-transparent bg-clip-text\1>\2</span>',
    content
)

# Fix some buttons that were bg-black hover:text-black, now should be bg-white hover:text-white
content = content.replace('hover:text-black', 'hover:text-white')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html theme to Light Mode with Mulberry & Peach.")
