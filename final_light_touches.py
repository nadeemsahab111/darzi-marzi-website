import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any remaining dark gradients from black
content = content.replace('from-black/50 via-black/20 to-[#1A1A1A]', 'from-white/70 via-white/40 to-[#F8F6F0]')
content = content.replace('from-black/50', 'from-white/50')
content = content.replace('via-black/20', 'via-white/20')
content = content.replace('to-black', 'to-white')
content = content.replace('from-[#1A1A1A]', 'from-[#F8F6F0]')

# Replace black drop shadow to shiny pink drop shadow
content = content.replace('drop-shadow-[0_0_10px_rgba(0,0,0,1)]', 'drop-shadow-[0_0_15px_rgba(204,0,126,0.3)]')

# Text changes: any remaining text-white to text-black if it's on a light background (but leave hover:text-white alone)
# Let's fix specific lines instead of blind replace.
content = content.replace('bg-[#1A1A1A]', 'bg-[#F8F6F0]')

# Remove black background for icon buttons in footer
content = content.replace('bg-black/20', 'bg-white/50')
content = content.replace('bg-[#0d0d0d]', 'bg-[#ffffff]')
content = content.replace('text-[#1A1A1A]', 'text-black')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied final luxurious light mode touches.")
