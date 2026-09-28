import logging
from time import sleep

from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from app.config import API_ID, API_HASH
from app.typing_engine import type_text


logger = logging.getLogger(__name__)


class TelegramClient:
    def __init__(self):
        self.app = Client(
            "my_account",
            api_id=API_ID,
            api_hash=API_HASH,
        )

        self._register_handlers()

    def safe_edit(self, message, text: str) -> None:
        while True:
            try:
                message.edit(text)
                return

            except FloodWait as e:
                logger.warning(
                    "FloodWait: waiting %s seconds",
                    e.value,
                )
                sleep(e.value)

    def _register_handlers(self):
        @self.app.on_message(
            filters.command("type", prefixes=".") & filters.me
        )
        def type_message(_, message):
            logger.info("Received typing command")

            _, separator, text = message.text.partition(".type ")

            if not separator or not text:
                logger.warning("Empty .type command")
                return

            def edit_message(content):
                self.safe_edit(message, content)

            type_text(text, edit_message)

    def run(self):
        logger.info("Starting Telegram client...")
        self.app.run()