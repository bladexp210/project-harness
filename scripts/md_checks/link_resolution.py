import re
import pathlib

def check_links(text, note_index):
    """Checks that all [[wiki-links]] in the text resolve against the note_index.
    
    Skips code fences, inline code, parses aliases/headings, strips extensions, and handles paths.
    """
    # Strip code fences and inline backticks
    body = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    body = re.sub(r"`[^`\n]+`", "", body)
    
    errors = []
    # Find all [[wiki-links]]
    for match in re.finditer(r"\[\[([^\]]+)\]\]", body):
        content = match.group(1)
        # Parse target part before '|'
        target_part = content.split('|', 1)[0].strip()
        # Parse note part before '#'
        target_note_raw = target_part.split('#', 1)[0].strip()
        
        if not target_note_raw:
            # Internal link to heading in current file, always resolves in v1
            continue
            
        # Extract the stem (strips paths like ../xx/yy and extensions like .md)
        target_note_normalized = target_note_raw.replace('\\', '/')
        target_note_normalized = target_note_normalized.strip('/')
        
        # Get the stem
        target_note = pathlib.Path(target_note_normalized).stem
        
        # Skip placeholder links containing NNN, NN, or ...
        target_note_lower = target_note.lower()
        if 'nnn' in target_note_lower or 'nn' in target_note_lower or '...' in target_note_lower:
            continue
            
        if target_note_lower not in note_index:
            errors.append("broken wiki-link: [[{}]] (target stem '{}' not found)"
                          .format(content, target_note))
    return errors
