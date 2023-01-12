"""Install package."""

import os
import setuptools

import packaging.version


def get_version_num() -> str:
    input_ver = os.environ.get("TOOLCHANGER_PLUGIN_RELEASE_VERSION", "0.0.0dev0")
    return str(packaging.version.parse(input_ver))


setuptools.setup(
    name="pytest-local-badge",
    version=get_version_num(),
    description="Adds Meross Smart Plug support to OctoPrint-PSUControl",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[],
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
    install_requires=["pytest>=6.1.0", "genbadge>=1.1.0,<2"],
    python_requires=">=3.7",
)
