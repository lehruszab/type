import logging

from app.telegram_client import TelegramClient


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def main():
    client = TelegramClient()
    client.run()


if __name__ == "__main__":
    main()