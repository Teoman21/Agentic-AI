# Agentic AI — Fall 2026 (Northeastern, Khoury College)

Prof. Caglar Yildirim, PhD · Course site: <https://agenticllms.github.io/>

Single reference for this workspace: course links, environment, API keys, and
commands. Last synced with the course site **2026-09-18**.

---

## 1. Course site endpoints

Every page that exists on the site (verified 2026-09-18 — these five are the
complete set; `week2b.html` is an empty stub, everything else 404s):

| Page | URL |
|---|---|
| Home / schedule | <https://agenticllms.github.io/index.html> |
| Research Resources (final project) | <https://agenticllms.github.io/research.html> |
| Week 1 · Setup | <https://agenticllms.github.io/week1.html> |
| Week 2a · Run a local LLM | <https://agenticllms.github.io/week2a.html> |
| Week 2b · Environment Setup | <https://agenticllms.github.io/week2b-setup.html> |

Lecture code repo: <https://github.com/agenticllms/lecture-files>

Class meets **Tuesday and Friday**.

## 2. Schedule, readings, and docs

Core reading per session is shown in **bold** on the site; both are listed here.

| Wk | Date | Topic | Papers | Framework docs |
|---|---|---|---|---|
| 1 | F 9/11 | Introduction to Agentic AI | [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) · [Rise and Potential of LLM Agents](https://arxiv.org/abs/2309.07864) | [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents) · [Philosophy](https://docs.langchain.com/oss/python/langchain/philosophy) |
| 2 | T 9/15 | LLM Foundations | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) · [Improving Language Understanding](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | [3Blue1Brown: LLMs visualized](https://www.youtube.com/watch?v=wjZofJX0v4M) (recommended) · [Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) |
| 2 | F 9/18 | LLM Foundations | [InstructGPT](https://arxiv.org/abs/2203.02155) · [Chain-of-Thought](https://arxiv.org/abs/2201.11903) | [Models](https://docs.langchain.com/oss/python/langchain/models) · [Messages](https://docs.langchain.com/oss/python/langchain/messages) · [Structured output](https://docs.langchain.com/oss/python/langchain/structured-output) |
| 3 | T 9/22 | Simple Agent Architecture | [Toolformer](https://arxiv.org/abs/2302.04761) · [MRKL](https://arxiv.org/abs/2205.00445) | [Tools](https://docs.langchain.com/oss/python/langchain/tools) |
| 3 | F 9/25 | Tool-Calling | [ReAct](https://arxiv.org/abs/2210.03629) · [What Are Tools Anyway?](https://arxiv.org/abs/2403.15452) | [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) · [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) · [Agents](https://docs.langchain.com/oss/python/langchain/agents) |

Schedule on the site currently stops at Week 3.

## 3. Reused reference pages

Links worth keeping open while working, beyond the assigned readings.

| What | URL |
|---|---|
| `create_agent` API reference | <https://reference.langchain.com/python/langchain/agents/factory/create_agent> |
| `TavilySearch` API reference | <https://reference.langchain.com/python/langchain-tavily/tavily_search/TavilySearch> |
| LangChain Ollama integration | <https://docs.langchain.com/oss/python/integrations/chat/ollama> |
| Local Ollama server (must be running) | <http://localhost:11434> |
| Python primer (Week 1, Colab) | <https://colab.research.google.com/drive/1s60I7NQiTpOWg2tK-KmFyiC8ZAY24lo7?usp=sharing> |
| Official Python tutorial (ch. 3–5) | <https://docs.python.org/3/tutorial/> |
| wttr.in weather API (W02b.2 exercise) | <https://wttr.in/Boston?format=j1> |
| uv docs | <https://docs.astral.sh/uv/> |
| Ollama model library | <https://ollama.com/library> |

### Final project research venues

From [research.html](https://agenticllms.github.io/research.html). Framing the
site insists on: **mechanism → experimental manipulation → measured behavior.**
"An application domain alone is not a research contribution."

NeurIPS · [ICLR / OpenReview](https://openreview.net/) · ICML ·
[ACL Anthology](https://aclanthology.org/) · COLM ·
[arXiv cs.CL](https://arxiv.org/list/cs.CL/recent) ·
[arXiv cs.AI](https://arxiv.org/list/cs.AI/recent) ·
[Semantic Scholar](https://www.semanticscholar.org/) ·
[Google Scholar](https://scholar.google.com/)

Workshop papers are called out as the best fit for semester-scale ideas.
Five suggested directions: benchmarking/evaluation, fine-tuning small models,
AI safety & security, tool use & MCP, memory & context.

---

## 4. API keys

Keys live in `.env` at the project root (git-ignored — **never commit it**).
Template is `lecture-files/example.env`.

| Key | Required | Cost | Get it at |
|---|---|---|---|
| `GOOGLE_API_KEY` | yes | free tier | <https://aistudio.google.com/apikey> |
| `TAVILY_API_KEY` | yes | free tier | <https://app.tavily.com/> |
| `OPENAI_API_KEY` | optional | **paid** | <https://platform.openai.com/api-keys> |
| `ANTHROPIC_API_KEY` | optional | **paid** | <https://console.anthropic.com/settings/keys> |

Both required keys are genuinely free and need no credit card:

- **Tavily** — 1,000 credits/month, "no credit card required." Exhausting them
  stops requests until the 1st of the month; it does not auto-upgrade or bill.
- **Google Gemini** — `gemini-3.5-flash-lite` is free of charge in/out. You stay
  on the free tier as long as you never link a billing account; linking one moves
  you to paid Tier 1. Free-tier content **is used by Google to improve their
  models**, so don't paste anything private. Free rate limits are per-account and
  shown at <https://aistudio.google.com/rate-limit>; exceeding them returns `429`,
  not a charge.

The two optional keys have no free API tier. Leave them as placeholders —
`verify_setup.py` reports them as warnings, not failures. Every notebook cell
that uses them has a Gemini or Ollama alternative.

**Zero-cost fallback:** the local Ollama models need no key, no account, and no
network. Swap any model cell for `ChatOllama(model="qwen3.5:4b", reasoning=False)`.

---

## 5. Workspace layout

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

**Folder naming:** `W<week><session>` — zero-padded week, letter per class
meeting. `W02b` = week 2, second meeting (F 9/18). There is no `W02a` folder;
that session was the Ollama install and had no notebooks. The second dot-number
in a filename (`W02b.1_...`) is the notebook's order within the day.

## 6. Commands

```bash
# environment health check — expect 23 passed once keys are in
uv run python scripts/verify_setup.py

# start a new session's files (pulls lecture-files first, then copies)
./scripts/new-week.sh W03a

# local models
brew services start ollama     # or: ollama serve
ollama list                    # what's downloaded
ollama ps                      # what's loaded in RAM
ollama run qwen3.5:4b          # interactive chat, /bye to exit
```

In VS Code, open a notebook and pick the **Agentic AI (.venv 3.13)** kernel.

### Course rules

- Use `uv pip install`, never bare `pip`.
- `lecture-files/` is read-only. Work in the copied folder (`W02b/`, not
  `lecture-files/W02b/`). Running a notebook writes outputs into the repo, which
  blocks the next `git pull`; fix with `git restore .` inside `lecture-files`.
  `new-week.sh` does this automatically.
- Never commit `.env`.

## 7. Local models

Ollama serves an OpenAI-style API at <http://localhost:11434>.

| Model | Size | Why |
|---|---|---|
| `qwen3.5:4b` | 3.4 GB | what the W02b notebooks use in `ChatOllama` |
| `qwen3.5:9b` | 6.6 GB | course default for a 16 GB machine |
| `qwen2.5:0.5b` | 397 MB | instruction-tuned, for the base-vs-instruct demo |
| `qwen2.5:0.5b-base` | 397 MB | raw pretrained, same demo |

Course sizing guidance: `2b` small/fast, `4b` needs 8 GB RAM, `9b` needs 16 GB,
`27b` needs 32 GB+.

## 8. Known issues in the lecture notebooks

- `W02b.1` cell 45 calls `pprint("\nstop reason:", r.response_metadata.get(...))`.
  `pprint`'s second positional arg is a stream, so this raises `AttributeError`.
  Use a plain `print`, or split into two statements.
- `W02b.2` cells 43 and 55 reference a tool named `days_until`, but the tool
  defined in cell 37 is `count_days_until_given_date`. Rename one or the other.
- `#TODO` cells are in-class exercises, intentionally left blank:
  `W02b.1` cells 9, 14, 49 · `W02b.2` cells 13, 18, 34, 63.
