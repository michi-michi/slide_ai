"""Command line interface for slide generation."""

import argparse
from pathlib import Path

from .generator import generate_slides


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate slides via OpenAI")
    parser.add_argument("topic", help="Topic for the slides")
    parser.add_argument("--slides", type=int, default=5, help="Number of slides")
    parser.add_argument(
        "--output", type=Path, default=Path("slides.md"), help="Output Markdown file"
    )

    args = parser.parse_args()

    slides = generate_slides(args.topic, n_slides=args.slides)
    content = "\n\n---\n\n".join(slides)
    args.output.write_text(content, encoding="utf-8")
    print(f"Slides written to {args.output}")


if __name__ == "__main__":
    main()
