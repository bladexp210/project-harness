import re

def check_adr_patterns(text, is_template):
    """Flags pattern tables missing failure-condition ('when NOT to apply') column or values.
    
    Excludes template decision tables by focusing only on pattern recommendation tables.
    """
    # Find all tables
    tables = []
    current_table = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            current_table.append(line)
        else:
            if len(current_table) >= 2:
                tables.append(current_table)
            current_table = []
    if len(current_table) >= 2:
        tables.append(current_table)
        
    errors = []
    
    # Pattern/decision table identification
    pattern_headers = {'pick', 'strategy', 'pattern', 'recommendation', 'signal in your use cases'}
    failure_headers = {'when not to apply', 'failure condition', 'failure condition you accepted'}
    
    for table_lines in tables:
        # Header line
        header_line = table_lines[0]
        headers = [c.strip().lower() for c in header_line.split('|')[1:-1]]
        
        # Check if second line is a separator
        separator = table_lines[1]
        if not re.match(r"^\|[-:\s|]+\|$", separator.strip()):
            continue
            
        # Check if it's a pattern/decision table
        if not any(h in pattern_headers for h in headers):
            continue
            
        # Check if it has a failure condition column
        fc_col_idx = -1
        for idx, h in enumerate(headers):
            if h in failure_headers:
                fc_col_idx = idx
                break
                
        if fc_col_idx == -1:
            errors.append("decision table missing failure-condition / 'when NOT to apply' column")
            continue
            
        # Check each row (starting from index 2, which is the 3rd line of the table)
        for row_idx, line in enumerate(table_lines[2:], 3):
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if fc_col_idx >= len(cells):
                errors.append("decision table row {} is missing column values".format(row_idx))
                continue
                
            val = cells[fc_col_idx]
            if not val:
                errors.append("pattern row {} is missing its failure condition / 'when NOT to apply' value"
                              .format(row_idx))
            elif not is_template:
                # If not a template, check if it's a placeholder
                if re.match(r"^\[.*\]$", val) or re.match(r"^\s*\.\.\.\s*$", val):
                    errors.append("pattern row {} has placeholder failure condition: '{}'"
                                  .format(row_idx, val))
                    
    return errors
