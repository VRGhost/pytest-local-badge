"""Main plugin module"""

def pytest_addoption(parser):
    group = parser.getgroup("local_badge")
    group.addoption(
        "--output-dir",
        action="store",
        dest="out_dir",
        default=None,
    )

def pytest_sessionfinish(session, exitstatus):
    print("HELLO WORLD", session)