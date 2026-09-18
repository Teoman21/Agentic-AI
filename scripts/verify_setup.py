"""Check that the course environment matches the Week 2b setup guide.

Run with:  uv run python scripts/verify_setup.py 
testing commmit name
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PASS, FAIL, WARN = "  ok  ", " FAIL ", " warn "
results: list[tuple[str, str]] = []


def check(label, ok, detail="", warn_only=False, hint=""):
    """detail always shows; hint shows only when the check did not pass."""
    tag = PASS if ok else (WARN if warn_only else FAIL)
    note = detail or (hint if not ok else "")
    results.append((tag, f"{label}{f' — {note}' if note else ''}"))
    return ok


def main():
    # 1. Python version
    v = sys.version_info
    check(f"Python {v.major}.{v.minor}.{v.micro}", (v.major, v.minor) == (3, 13),
          hint="expected 3.13 from `uv venv --python 3.13`")

    # 2. Running inside the project venv
    check("Running inside .venv", str(ROOT / ".venv") in sys.prefix,
          hint=f"sys.prefix={sys.prefix}")

    # 3. Required packages
    packages = [
        "langchain", "langchain_openai", "langchain_anthropic",
        "langchain_google_genai", "langchain_tavily", "langchain_ollama",
        "langgraph", "dotenv", "ipykernel", "requests", "gradio",
    ]
    for pkg in packages:
        try:
            __import__(pkg)
            check(f"import {pkg}", True)
        except Exception as e:
            check(f"import {pkg}", False, str(e)[:60])

    # 4. .env and API keys
    from dotenv import load_dotenv
    env_path = ROOT / ".env"
    if check(".env exists at project root", env_path.exists(),
             hint="cp lecture-files/example.env .env"):
        load_dotenv(env_path)

    placeholder = lambda s: (not s) or s.startswith("your_")
    for key, required in [("GOOGLE_API_KEY", True), ("TAVILY_API_KEY", True),
                          ("OPENAI_API_KEY", False), ("ANTHROPIC_API_KEY", False)]:
        val = os.getenv(key)
        ok = not placeholder(val)
        check(key, ok, "set" if ok else "",
              warn_only=not required,
              hint="still a placeholder — paste your real key into .env")

    # 5. Ollama server + models (Week 2a)
    try:
        import requests
        tags = requests.get("http://localhost:11434/api/tags", timeout=3).json()
        names = {m["name"] for m in tags.get("models", [])}
        check("Ollama serving on localhost:11434", True, f"{len(names)} model(s)")
        for want in ["qwen3.5:4b", "qwen3.5:9b", "qwen2.5:0.5b", "qwen2.5:0.5b-base"]:
            check(f"ollama model {want}", want in names,
                  warn_only=True, hint=f"not downloaded — run `ollama pull {want}`")
    except Exception as e:
        check("Ollama serving on localhost:11434", False, warn_only=True,
              hint=f"{type(e).__name__} — run `brew services start ollama`")

    # 6. Folder layout from the course README
    check("lecture-files/ cloned", (ROOT / "lecture-files").is_dir())
    check("W02b/ working copy", (ROOT / "W02b").is_dir(),
          hint="run `cp -r lecture-files/W02b W02b`")

    width = max(len(m) for _, m in results) + 2
    print("\nCourse environment check\n" + "=" * (width + 8))
    for tag, msg in results:
        print(f"[{tag}] {msg}")
    failed = sum(1 for t, _ in results if t == FAIL)
    warned = sum(1 for t, _ in results if t == WARN)
    print("=" * (width + 8))
    print(f"{len(results) - failed - warned} passed, {warned} warnings, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
