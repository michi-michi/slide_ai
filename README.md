# Slide AI

A Python application that leverages ChatGPT to generate slide content. This project provides a CLI to request slide outlines from OpenAI and export them in Markdown format.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your OpenAI API key via the `OPENAI_API_KEY` environment variable.

## Usage

Generate slides for a topic:

```bash
python -m slide_ai "Your topic here" --slides 5 --output slides.md
```

