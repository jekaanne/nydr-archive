import re
import os
import shutil

doc_path = '/Users/jessicamurray/.gemini/antigravity/brain/d1fef292-c77c-4572-ac0f-86566e11dd9a/.system_generated/steps/386/content.md'
base_dir = '/Users/jessicamurray/Documents/nydr-archive/nydr-archive/content/topics/disability-independence-day'

with open(doc_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

sections = []
current_section = None
current_content = []

# Some headings might have BOM or zero-width space, let's normalize
def clean_line(line):
    return line.strip().replace('\ufeff', '')

for line in lines:
    line_clean = clean_line(line)
    
    # Check for heading "1. introduction" etc
    match = re.match(r'^(\d+)\.\s+(.*)$', line_clean)
    if match:
        if current_section:
            sections.append({
                'title': current_section,
                'content': '\n'.join(current_content).strip()
            })
        current_section = match.group(2).strip()
        current_content = []
    elif line_clean.startswith('___'):
        break # stop processing at line ______________
    elif current_section:
        current_content.append(line_clean)

if current_section:
    sections.append({
        'title': current_section,
        'content': '\n'.join(current_content).strip()
    })

# Define a mapping for known folders
folder_map = {
    'introduction': 'didm-introduction'
}

for sec in sections:
    title = sec['title']
    title_lower = title.lower()
    
    # Create folder name
    folder_name = folder_map.get(title_lower, title_lower.replace(' ', '-'))
    
    # Remove any special chars if needed, though they are mostly alphabetic
    folder_name = re.sub(r'[^a-z0-9\-]', '', folder_name)
    
    dir_path = os.path.join(base_dir, folder_name)
    os.makedirs(dir_path, exist_ok=True)
    
    # Clean up notes like [a], [b] etc from content
    content_clean = re.sub(r'\[[a-z]+\]', '', sec['content'])
    
    file_path = os.path.join(dir_path, '_index.md')
    
    # Write to file with Hugo frontmatter
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: "{title.title()}"\n')
        f.write('layout: subtopic-gallery\n') # Assuming subtopic-gallery layout since it's a topic section
        f.write('---\n\n')
        f.write(content_clean + '\n')
        
    print(f"Created {file_path}")

