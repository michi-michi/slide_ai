from types import SimpleNamespace
from unittest.mock import patch
import os

from slide_ai import generator


class DummyResponse:
    def __init__(self, content: str):
        self.choices = [
            type(
                "obj",
                (object,),
                {"message": type("msg", (object,), {"content": content})()},
            )
        ]


def fake_openai(return_content: str):
    return SimpleNamespace(
        ChatCompletion=SimpleNamespace(
            create=lambda **_: DummyResponse(return_content)
        )
    )


@patch.object(generator, "_load_openai")
def test_generate_slides(mock_load):
    mock_load.return_value = fake_openai("Slide 1\n---\nSlide 2")
    os.environ["OPENAI_API_KEY"] = "dummy"
    slides = generator.generate_slides("test", n_slides=2)
    assert slides == ["Slide 1", "Slide 2"]
