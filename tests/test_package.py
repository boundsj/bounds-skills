"""Ensure package checks reject defects that break selective distribution."""

from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check import check


class PackageValidation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="bounds-package-")
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parents[1]
        for folder in ("skills", "licenses"):
            shutil.copytree(source / folder, self.root / folder)

    def tearDown(self):
        self.temp.cleanup()

    def test_complete_package(self):
        self.assertEqual(len(check(self.root)), 33)

    def test_missing_reference(self):
        (self.root / "skills/bounds-mode/references/hosts.md").unlink()
        with self.assertRaisesRegex(AssertionError, "broken link"):
            check(self.root)

    def test_reference_cannot_depend_on_another_skill(self):
        path = self.root / "skills/bounds-plan/SKILL.md"
        path.write_text(path.read_text() + "\n[Shared reference](../bounds-debug/references/feedback-loops.md)\n")
        with self.assertRaisesRegex(AssertionError, "escapes skill"):
            check(self.root)

    def test_selective_package_keeps_upstream_license(self):
        path = self.root / "skills/bounds-debug/LICENSE.txt"
        path.write_text("MIT\n")
        with self.assertRaisesRegex(AssertionError, "upstream notice"):
            check(self.root)

    def test_selective_tstack_package_keeps_theo_license(self):
        path = self.root / "skills/bounds-ship/LICENSE.txt"
        notice = (self.root / "licenses/Theo-Browne-MIT.txt").read_text()
        path.write_text(path.read_text().replace(notice, ""))
        with self.assertRaisesRegex(AssertionError, "tstack upstream notice"):
            check(self.root)

    def test_selective_emil_package_keeps_emil_license(self):
        path = self.root / "skills/bounds-options/LICENSE.txt"
        notice = (self.root / "licenses/Emil-Kowalski-MIT.txt").read_text()
        path.write_text(path.read_text().replace(notice, ""))
        with self.assertRaisesRegex(AssertionError, "Emil Kowalski upstream notice"):
            check(self.root)

    def test_skill_cannot_carry_private_details(self):
        path = self.root / "skills/bounds-plan/SKILL.md"
        for leak in ("/Users/someone/project", "/mnt/c/Users/someone", "C:\\Users\\someone", "someone@private-mail.dev",
                     "build-box.tail1234.ts.net", "studio.local", "100.101.102.103", "192.168.1.20", "fd7a:115c:a1e0::1"):
            original = path.read_text()
            path.write_text(original + f"\nRun it from {leak}.\n")
            with self.assertRaisesRegex(AssertionError, "private detail"):
                check(self.root)
            path.write_text(original)
        path.write_text(path.read_text() + "\nWrite to sam@example.org.\n")
        check(self.root)

    def test_mode_cannot_silently_become_implicit(self):
        path = self.root / "skills/bounds-mode/SKILL.md"
        path.write_text(path.read_text().replace("disable-model-invocation: true", "disable-model-invocation: false"))
        with self.assertRaises(AssertionError):
            check(self.root)


if __name__ == "__main__":
    unittest.main()
