import typing
import pathlib

import genbadge
import pytest


class BadgeBase:
    """Base class for badge generators."""

    output_file_name = "UNKNOWN.svg"
    output_dir: pathlib.Path

    def __init__(self, output_dir: pathlib.Path, options):
        self.options = options
        self.output_dir = output_dir
        assert self.output_dir.is_dir(), self.output_dir

    @property
    def full_output_file_name(self):
        return (self.output_dir / self.output_file_name).resolve()

    @classmethod
    def pytest_addoption(cls, option_group, my_prefix: str):
        option_group.addoption(
            f"--local-badge-{my_prefix}-file-name",
            default=cls.output_file_name,
            help="Desired output file name",
        )

    def get_colour(self, success_pct: typing.Optional[float]):
        if success_pct is None:
            out = "lightgrey"
        elif success_pct >= 0.99:
            out = "brightgreen"
        elif success_pct >= 0.87:
            out = "green"
        elif success_pct >= 0.75:
            out = "yellowgreen"
        elif success_pct >= 0.5:
            out = "yellow"
        elif success_pct >= 0.3:
            out = "orange"
        else:
            out = "red"
        return out

    def on_sessionfinish(self, session, exitstatus):
        raise NotImplementedError(self.__class__.__name__)


class TestSuccess(BadgeBase):
    """Test success badge"""

    output_file_name = "tests.svg"

    def on_sessionfinish(self, session: pytest.Session, exitstatus: int):
        tests_success = exitstatus == 0
        total_tests = session.testscollected
        failed_tests = session.testsfailed
        succeeded_tests = total_tests - failed_tests
        if failed_tests == 0:
            right_text = f"{total_tests}"
        else:
            right_text = f"{succeeded_tests}/{total_tests}"
        genbadge.Badge(
            left_txt="tests",
            right_txt=right_text,
            color=self.get_colour(
                ((total_tests - failed_tests) / total_tests) * tests_success
            ),
        ).write_to(self.full_output_file_name, use_shields=False)