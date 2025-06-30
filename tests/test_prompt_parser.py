from siteplan.prompt_parser import parse_prompt


def test_parse_single_instruction():
    prompt = "place house 20x30 at 5,10"
    placements = parse_prompt(prompt)
    assert len(placements) == 1
    p = placements[0]
    rect = p.rect
    assert rect.x == 50 and rect.y == 100
    assert rect.width == 200 and rect.height == 300
    assert p.facing is None
    assert p.setbacks == {}


def test_parse_with_options():
    prompt = "place house 10x10 at 0,0 facing east n setback 5 w setback 3"
    [p] = parse_prompt(prompt)
    assert p.facing == "east"
    assert p.setbacks["n"] == 5
    assert p.setbacks["w"] == 3
