from siteplan.prompt_parser import parse_prompt


def test_parse_single_instruction():
    prompt = "place house 20x30 at 5,10"
    rects = parse_prompt(prompt)
    assert len(rects) == 1
    rect = rects[0]
    assert rect.x == 50 and rect.y == 100
    assert rect.width == 200 and rect.height == 300
