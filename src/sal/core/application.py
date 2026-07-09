"""
Main application class for SAL.
"""

from .version import PROJECT_NAME, SYSTEM_NAME, __version__


class Application:

    def start(self) -> None:
        print("=" * 50)
        print(PROJECT_NAME)
        print(SYSTEM_NAME)
        print(f"Version: {__version__}")
        print("=" * 50)
        print("SAL iniciado correctamente.")
