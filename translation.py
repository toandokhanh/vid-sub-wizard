"""Synchronous facade for the maintained asynchronous googletrans API.

Translation sends text to Google's external service; this is an unofficial client.
"""

import asyncio
from types import SimpleNamespace
from googletrans import Translator as AsyncTranslator


class Translator:
    def translate(self, text, src="auto", dest="en"):
        if not text.strip() or src == dest:
            return SimpleNamespace(text=text)

        async def translate():
            async with AsyncTranslator() as client:
                return await client.translate(text, src=src, dest=dest)

        return asyncio.run(translate())
