"""Exercise the synchronous adapter without installing or calling a provider."""

import importlib.util
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class FakeTranslator:
    calls = []
    closed = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        type(self).closed = True

    async def translate(self, text, src, dest):
        type(self).calls.append((text, src, dest))
        if dest == "fail":
            raise RuntimeError("provider failure")
        return SimpleNamespace(text="translated")


class TranslationTests(unittest.TestCase):
    def setUp(self):
        FakeTranslator.calls = []
        FakeTranslator.closed = False
        with patch.dict(
            sys.modules, {"googletrans": SimpleNamespace(Translator=FakeTranslator)}
        ):
            spec = importlib.util.spec_from_file_location(
                "translation_under_test", ROOT / "translation.py"
            )
            self.module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.module)

    def test_preserves_text_when_no_translation_is_needed(self):
        adapter = self.module.Translator()
        self.assertEqual(adapter.translate("hello", src="en", dest="en").text, "hello")
        self.assertEqual(adapter.translate(" ", dest="vi").text, " ")
        self.assertEqual(FakeTranslator.calls, [])

    def test_awaits_the_current_async_api_and_closes_the_client(self):
        result = self.module.Translator().translate("hello", src="en", dest="vi")
        self.assertEqual(result.text, "translated")
        self.assertEqual(FakeTranslator.calls, [("hello", "en", "vi")])
        self.assertTrue(FakeTranslator.closed)

    def test_provider_failures_are_propagated_and_client_is_closed(self):
        with self.assertRaisesRegex(RuntimeError, "provider failure"):
            self.module.Translator().translate("hello", dest="fail")
        self.assertTrue(FakeTranslator.closed)


if __name__ == "__main__":
    unittest.main()
