"""Install package."""

import os

import packaging.version
import setuptools


def get_version_num() -> str:
    input_ver = os.environ.get("RELEASE_VERSION", "0.0.0dev0")
    return str(packaging.version.parse(input_ver))


setuptools.setup(
    name="pytest-local-badge",
    version=get_version_num(),
    description="Generate local badges (shields) reporting your test suite status.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Plugins",
        "Framework :: Pytest",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="MIT",
    author="Ilja Orlovs",
    author_email="vrghost@gmail.com",
    url="https://github.com/VRGhost/pytest-local-badge",
    package_dir={"": "src"},
    zip_safe=False,
    include_package_data=True,
    packages=setuptools.find_packages(where="src"),
    entry_points={"pytest11": ["local_badge = pytest_local_badge.plugin"]},
    py_modules=[
        "pytest_local_badge",
    ],
    extras_require={
        "develop": [
            "black>=22.12.0",
            "pytest>=7.1.0,<8",
            "pytest-cov",
            "pytest-mock",
            "flake8-bugbear",
            "flake8-import-order",
            "pep8-naming",
            "flake8-print",
            "flake8-comprehensions",
            "build",
        ]
    },
    install_requires=["pytest>=6.1.0"],
    python_requires=">=3.7",
)
