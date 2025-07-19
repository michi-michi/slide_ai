"""Core slide generation functionality using OpenAI's ChatGPT API."""

from __future__ import annotations

import os
from typing import List


def _load_openai():
    """Import the OpenAI package lazily."""
    try:
        import openai  # type: ignore
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "openai package is required to use slide generation"
        ) from exc
    return openai



def generate_slides(topic: str, n_slides: int = 5) -> List[str]:
    """Generate slide contents using ChatGPT.

    Parameters
    ----------
    topic: str
        The topic for the slide deck.
    n_slides: int
        Number of slides to generate.

    Returns
    -------
    List[str]
        A list containing slide contents in Markdown format.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")

    openai = _load_openai()
    openai.api_key = api_key

    prompt = (
        f"Create {n_slides} slides about '{topic}'. "
        "Respond with each slide separated by '\n---\n'." 
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.choices[0].message.content
    slides = [slide.strip() for slide in text.split("\n---\n") if slide.strip()]
    return slides
