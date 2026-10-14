import re
import pathlib

TEACHING_MARKERS = ("[!LEARN]", "[!TIP]", "[!TEACH]")
CALLOUT_RE = re.compile(r"^>\s*\[!(\w+)\]")
BRACKET_PLACEHOLDER = re.compile(r"(?<!\[)\[([^\]\n]+)\](?!\])")


def _strip_code_and_inline(text):
    body = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]+`", "", body)


def _bracket_placeholder_errors(body, relpath, *, in_teaching_callout=False):
    """Return errors for unfilled [placeholder] brackets in body text."""
    errors = []

    for m in BRACKET_PLACEHOLDER.finditer(body):
        content = m.group(1)
        end_idx = m.end()

        rest = body[end_idx:]
        if rest.startswith("(") or rest.startswith("[") or rest.startswith(":"):
            continue

        stripped = content.strip()
        if stripped in ("", "x", "/", "o", "v", "-"):
            continue
        if len(stripped) == 1 and not stripped.isalnum():
            continue
        if stripped.isdigit():
            continue
        if stripped.startswith("!"):
            continue
        if stripped.startswith("PRUNED:"):
            continue

        line_start = body.rfind("\n", 0, m.start()) + 1
        line_end = body.find("\n", m.start())
        if line_end == -1:
            line_end = len(body)
        line = body[line_start:line_end].strip()
        if line.startswith(("tags:", "audience:", "categories:", "yaml:")):
            continue

        end_frontmatter = body.find("\n---", 4)
        is_yaml_like = relpath.endswith((".yaml", ".yml")) or (
            end_frontmatter != -1 and m.start() < end_frontmatter
        )
        if is_yaml_like:
            if " " not in stripped and "..." not in stripped:
                continue

        if in_teaching_callout:
            errors.append("artifact placeholder inside teaching callout: '[{}]'".format(content))
        else:
            errors.append("contains unfilled placeholder: '[{}]'".format(content))

    return errors


def _is_teaching_callout_line(line):
    m = CALLOUT_RE.match(line)
    if not m:
        return False
    marker = "[!{}]".format(m.group(1).upper())
    return marker in TEACHING_MARKERS


def _is_dual_purpose_md(relpath):
    """Dual-purpose files per ADR-006 (instruction + reader artifact)."""
    parts = pathlib.Path(relpath).parts
    if "_templates" in parts:
        return False
    if any(p in parts for p in ("00-start-here", "decisions", "sessions")):
        return False

    posix = str(relpath).replace("\\", "/")
    if posix.startswith("01-understand/"):
        return True
    if "02-design/layers/" in posix:
        return True
    if posix.startswith("03-plan/"):
        return True
    if "/tasks/" in posix:
        return True
    return False


def _extract_teaching_callout_text(text):
    """Collect inner text from [!LEARN]/[!TIP]/[!TEACH] callouts (ADR-006)."""
    chunks = []
    inside_fence = False
    in_callout = False
    callout_lines = []

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            inside_fence = not inside_fence
            if in_callout:
                in_callout = False
                callout_lines = []
            continue
        if inside_fence:
            continue

        if _is_teaching_callout_line(line):
            if in_callout and callout_lines:
                chunks.append("\n".join(callout_lines))
            in_callout = True
            callout_lines = [line[2:].lstrip() if line.startswith("> ") else line]
            continue

        if in_callout:
            if line.startswith(">"):
                callout_lines.append(line[2:].lstrip() if len(line) > 1 else "")
            else:
                chunks.append("\n".join(callout_lines))
                in_callout = False
                callout_lines = []

    if in_callout and callout_lines:
        chunks.append("\n".join(callout_lines))

    return "\n\n".join(chunks)


def check_placeholders(text, relpath):
    """Flags unfilled placeholders in template-derived files (tasks, decisions, agents).

    Avoids false positives on links, checkboxes, citation numbers, and YAML lists.
    Skips Obsidian callout markers in the outer scan.
    """
    path_parts = pathlib.Path(relpath).parts
    if "_templates" in path_parts:
        return []

    is_task = "tasks" in path_parts
    is_decision = "decisions" in path_parts
    is_agent = "agents" in path_parts and any(
        relpath.endswith(ext) for ext in (".yaml", ".yml")
    )

    if not (is_task or is_decision or is_agent):
        return []

    body = _strip_code_and_inline(text)
    errors = []

    if re.search(r"\bTask\s+NN\b", body, re.I):
        errors.append("contains unfilled task number placeholder 'Task NN'")
    if re.search(r"\btask:\s+NN\b", body, re.I):
        errors.append("contains unfilled task number placeholder 'task: NN'")
    if re.search(r"\bADR-NNN?\b", body, re.I):
        errors.append("contains unfilled ADR number placeholder 'ADR-NNN'")

    errors.extend(_bracket_placeholder_errors(body, relpath))
    return errors


def check_teaching_callout_placeholders(text, relpath):
    """ADR-006 Phase 3: reader-fillable [placeholders] inside teaching callouts."""
    if not relpath.endswith(".md"):
        return []
    if not _is_dual_purpose_md(relpath):
        return []

    teaching = _extract_teaching_callout_text(text)
    if not teaching:
        return []

    body = _strip_code_and_inline(teaching)
    return _bracket_placeholder_errors(body, relpath, in_teaching_callout=True)
