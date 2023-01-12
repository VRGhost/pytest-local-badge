"""Main plugin module"""
import pathlib

import pytest


def pytest_addoption(parser):
    group = parser.getgroup("local_badge")
    group.addoption(
        "--no-local-badge",
        action="store_false",
        default=True,
        dest="pytest_local_badge_enabled",
    )
    group.addoption(
        "--badge-output-dir",
        action="store",
        default=None,
    )


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(early_config, parser, args):
    options = early_config.known_args_namespace
    print(f"{early_config.known_args_namespace.pytest_local_badge_enabled=}")
    if (
        early_config.known_args_namespace.pytest_local_badge_enabled
        and early_config.known_args_namespace.badge_output_dir
    ):
        plugin = LocalBadgePlugin(options)
        early_config.pluginmanager.register(plugin, "_local_badge")


class PytestLocalBadgeError(Exception):
    """A generic pytest_local_badge exception."""


class LocalBadgePlugin:
    """Generate local SVG badges."""

    options = None
    out_dir: pathlib.Path

    def __init__(self, options):
        self.options = options
        self.out_dir = pathlib.Path(options.badge_output_dir)
        if not self.out_dir.is_dir():
            raise PytestLocalBadgeError(
                f"Badge output dir {self.out_dir} ({self.out_dir.resolve()}) does not exist or is not a directory"
            )

    def pytest_sessionfinish(self, session, exitstatus):
        print("SESSION FINISH")
