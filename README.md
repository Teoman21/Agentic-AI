# Agentic AI — Course Workspace

Northeastern, Fall 2026. Setup follows the course site: <https://agenticllms.github.io/>
([Week 1](https://agenticllms.github.io/week1.html) ·
[Week 2a](https://agenticllms.github.io/week2a.html) ·
[Week 2b](https://agenticllms.github.io/week2b-setup.html) ·
[Research](https://agenticllms.github.io/research.html))

## Layout

```
Agentic-AI/
├── .venv/            Python 3.13 environment (uv, git-ignored)
├── .env              API keys (git-ignored — never commit)
├── .vscode/          interpreter + Jupyter root pinned to this folder
├── lecture-files/    the class repo, READ-ONLY (git-ignored, pull only)
│   └── W02b/
├── W02b/             your working copy — edit here
└── scripts/
    ├── verify_setup.py   environment health check
    └── new-week.sh       pull lecture-files + copy a session folder
```

## Daily use

```bash
# check everything is wired up
uv run python scripts/verify_setup.py

# start a new session's files (pulls lecture-files first)
./scripts/new-week.sh W03a
```

In VS Code, open a notebook and pick the **`.venv` (Python 3.13)** kernel.

## Rules from the course

- Use `uv pip install`, never bare `pip`.
- `lecture-files/` is read-only. Work in the copied folder (`W02b/`, not `lecture-files/W02b/`).
  If a pull is blocked by notebook outputs, `new-week.sh` runs `git restore .` for you.
- Never commit `.env`.

## Local models (Week 2a)

Ollama serves an OpenAI-style API at <http://localhost:11434>.

```bash
brew services start ollama     # or: ollama serve
ollama list                    # what's downloaded
ollama ps                      # what's loaded in RAM
ollama run qwen3.5:4b          # interactive chat, /bye to exit
```

Models pulled for this course:

| Model | Why |
|---|---|
| `qwen3.5:4b` | what the W02b notebooks use in `ChatOllama` |
| `qwen3.5:9b` | course default for a 16 GB machine |
| `qwen2.5:0.5b` | instruction-tuned, for the base-vs-instruct demo |
| `qwen2.5:0.5b-base` | raw pretrained, same demo |

## API keys

`.env` needs real values before the notebooks run:

| Key | Required | Get it at |
|---|---|---|
| `GOOGLE_API_KEY` | yes | <https://aistudio.google.com/apikey> |
| `TAVILY_API_KEY` | yes | <https://app.tavily.com/> |
| `OPENAI_API_KEY` | optional | <https://platform.openai.com/api-keys> |
| `ANTHROPIC_API_KEY` | optional | <https://console.anthropic.com/settings/keys> |
