import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace gold #D4AF37 with Mulberry #cc007e and Peach #ffbd59
# We will replace all text-[#D4AF37] with Peach #ffbd59 except some important headings where we use gradients
# But the easiest way to give a shiny premium touch is to replace the Gold hex with Peach
content = content.replace('#D4AF37', '#ffbd59')
content = content.replace('#d4af37', '#ffbd59')

# Replace secondary gold #f2ca50 with Mulberry #cc007e
content = content.replace('#f2ca50', '#cc007e')

# Update specific gradients to be shiny (Mulberry to Peach)
# Find: bg-gradient-to-r from-[#D4AF37] to-[#f2ca50] (which is now from-[#ffbd59] to-[#cc007e])
# Actually we can just update any linear-gradient or bg-gradient
content = content.replace('linear-gradient(90deg, #ffbd59, #cc007e)', 'linear-gradient(90deg, #cc007e, #ffbd59)')
content = content.replace('from-[#ffbd59] to-transparent', 'from-[#cc007e] to-transparent')

# Let's replace some text-[#ffbd59] with a gradient class in the hero
content = re.sub(
    r'<span class="text-\[#ffbd59\]([^>]*)>([^<]+)</span>',
    r'<span class="bg-gradient-to-r from-[#cc007e] to-[#ffbd59] text-transparent bg-clip-text\1>\2</span>',
    content
)

# And the title
content = content.replace(
    'text-white drop-shadow-[0_0_25px_rgba(212,175,55,0.2)]',
    'text-white drop-shadow-[0_0_25px_rgba(204,0,126,0.5)]'
)
# Update drop-shadows colors from old gold rgb(212,175,55) to Mulberry rgb(204,0,126) or Peach rgb(255,189,89)
content = content.replace('rgba(212,175,55', 'rgba(255,189,89')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html theme.")
