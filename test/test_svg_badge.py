import pytest

import pytest_local_badge.svg_badge as svg_badge


@pytest.mark.parametrize(
    "inp, exp_out",
    [
        ("", 0),
        (None, 0),
        ("123", 22.5),
    ],
)
def test_text_length(inp, exp_out):
    assert svg_badge.text_length(inp) == exp_out


@pytest.mark.parametrize("left_text", [None, "", "hello world"])
@pytest.mark.parametrize("right_text", [None, "", "hello world"])
@pytest.mark.parametrize("colour", [None, "", "#fff", "lightgreenm"])
def test_render_no_exceptions(mocker, left_text, right_text, colour):
    fobj = mocker.MagicMock(name="mock-fobj")
    svg_badge.render(fobj, left_text, right_text, colour)
    fobj.write.assert_called_once()
