
# Consensus-QA: Multi-LLM Fact-Checker & QA Assistant

## Description  
**Consensus-QA** is a tool that lets you ask factual questions and get answers synthesized from multiple large language models (LLMs).  
Instead of relying on a single LLM, it queries several models — then aggregates, reviews, and consolidates their outputs to aim for more accurate, reliable answers. The output is “committee-backed”, helping reduce hallucinations or model-specific biases.

This project builds on two key technologies / ideas:  
- **LiteLLM** — an open-source LLM gateway / proxy that lets you access and manage many different LLM providers (OpenAI, Anthropic, Groq, Gemini, etc.) via a unified interface. :contentReference[oaicite:2]{index=2}  
- **LLM Council** — an orchestration / consensus framework that lets multiple models independently answer a user’s question, then peer-review one another and finally elect a “chairman” model to produce a final, synthesized response. :contentReference[oaicite:3]{index=3}

By combining LiteLLM’s multi-provider support with LLM Council’s multi-model synthesis, Consensus-QA aims to deliver factual answers with higher reliability and transparency.

## Features  
- Query multiple LLMs (via LiteLLM) with a single user prompt.  
- Collect independent answers from each model.  
- Use LLM Council logic (peer-review + synthesis) to combine responses into a single consolidated answer.  
- Optionally output **raw responses from all models** + **consensus summary** (agreement level, flagged disagreements).  
- Easy to extend: add new models/providers, adjust consensus logic, or integrate into larger applications.  

## Getting Started  

### Prerequisites  
- A working Python environment (Python 3.10+ recommended)  
- API keys / credentials for one or more LLM providers supported by LiteLLM (OpenAI, Anthropic, Groq, Gemini, etc.)  
- LiteLLM installed (or proxy server deployed) so that you can access different LLM providers via a unified API. :contentReference[oaicite:4]{index=4}  

### Installation & Setup  
```bash
git clone https://github.com/aakriti1318/AI
cd Advanced-LLM-Projects/LLMCouncil_Litellm
pip install -r requirements.txt   # includes liteLLM, other dependencies
cp .env.example .env              # store your API keys / config here
````

### Usage

```bash
python app.py
# Enter a factual question when prompted — the tool returns a consensus-backed answer + raw model outputs.
```

## Example

```
Ask a factual question: What are Chanakya’s principles?  
→ [Consensus-backed answer summarizing principles, confidence notes, and possible disagreements among models]
```

You can also inspect all individual model responses and see where models agreed or diverged.

## Why / When to Use It

* When you need more **robust factual answers**, especially for knowledge-heavy or ambiguous queries.
* To compare how different LLMs answer the same question, see where they converge/diverge.
* As a component for building more reliable, transparent LLM-powered applications (e.g. research assistants, fact checkers, educational tools).

## Contributing

If you wish to contribute:

* Add support for additional LLM providers (via LiteLLM)
* Improve consensus logic (voting, ranking, uncertainty estimation)
* Add logging, evaluation harness, or benchmarking
* Build a web UI / frontend for easier use

## References & Credits

* LiteLLM — open-source LLM gateway / proxy, enabling unified API access to 100+ LLM providers. ([litellm.ai][1])
* LLM Council — multi-model consensus framework where multiple LLMs answer, peer-review, and synthesize a final answer. ([GitHub][2])
