import re

# Regex to match the word lifecycle(s)
LIFECYCLE_PAT = re.compile(r"\blifecycles?\b", re.I)
# Regex to check if the prefix ends with one of the qualifiers
QUALIFIER_PAT = re.compile(r"\b(product|user|feature|data|task)[\s-]*$", re.I)

def check_lifecycle_rules(text, path):
    """Enforces that 'lifecycle(s)' is always qualified with product/user/feature/data/task.
    
    Whitelists code fences, markdown links, wiki-links, ADR-004, and the glossary.
    """
    stem = path.stem.lower()
    if stem in ("adr-004-lifecycle-vocabulary", "glossary"):
        return []
        
    # Strip code fences, inline code, wiki-links, markdown links, reference links
    body = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    body = re.sub(r"`[^`\n]+`", "", body)
    body = re.sub(r"\[\[.*?\]\]", "", body)
    body = re.sub(r"\[.*?\]\(.*?\)", "", body)
    body = re.sub(r"\[.*?\]\[.*?\]", "", body)
    body = re.sub(r"\[.*?\]:", "", body)
    
    errors = []
    
    # We find all occurrences of the word "lifecycle(s)" in the stripped text
    for m in LIFECYCLE_PAT.finditer(body):
        # Extract substring before the match
        prefix = body[:m.start()]
        if not QUALIFIER_PAT.search(prefix):
            # Report the error with some surrounding context for clarity
            context_start = max(0, m.start() - 30)
            context_end = min(len(body), m.end() + 30)
            snippet = body[context_start:context_end].strip().replace('\n', ' ')
            errors.append("bare 'lifecycle' usage: '... {} ...' (must be qualified with product/user/feature/data/task)"
                          .format(snippet))
                          
    return errors
