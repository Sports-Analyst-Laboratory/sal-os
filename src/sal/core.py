"""
Sports Analyst Laboratory
SAL Core
Versión: 0.0.1
"""

def main():
    print("Sports Analyst Laboratory")
    print("SAL Core iniciado correctamente.")


if __name__ == "__main__":
    main()
    """
SAL Entry Point.
"""

from sal.core.application import Application


def main() -> None:
    app = Application()
    app.start()


if __name__ == "__main__":
    main()
    