Learning how to build my own Claude Code.

Claude Code is an AI coding assistant that uses Large Language Models (LLMs) to understand code and perform actions through tool calls. In this repo, I build Claude Code from scratch by implementing an LLM-powered coding assistant.

This started as an attempt to the [Build Your own Claude Code Challenge](https://codecrafters.io/challenges/claude-code) by [CodeCrafters](https://codecrafters.io). I started this on April 7, 2026 and then I continued in my own direction after completing the first 6 stages on CodeCrafters.

### To run the app

Note: This section is for stages 2 and beyond.

1. Ensure you have `uv` installed locally.

```
pip install uv
```

2. Run `./your_program.sh -p {{PROMPT}}` to run your program, which is implemented in `app/main.py`.
   or
3. Run `uv run -m app.main -p {{PROMPT}}` replace the `{{PROMPT}}` with the command you want the assistant to execute

#### Commands support

- Read files
- Write to files
- Run Bash commands
