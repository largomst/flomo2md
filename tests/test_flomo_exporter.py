import os
import shutil
import unittest
from datetime import datetime
from flomo_exporter import convert_html_to_markdown

class TestFlomoExporter(unittest.TestCase):

    def setUp(self):
        self.test_input_html = "test_input.html"
        self.test_output_dir = "test_output"
        self.expected_output_files = [
            "2023-10-01 12.00.00.md",
            "2023-10-02 14.30.00.md"
        ]

        # Create a test input HTML file
        with open(self.test_input_html, "w") as f:
            f.write("""
            <div class="memo">
                <time>2023-10-01 12:00:00</time>
                <content>
                    <strong>Important</strong> note.
                </content>
            </div>
            <div class="memo">
                <time>2023-10-02 14:30:00</time>
                <content>
                    <u>Underlined</u> note.
                </content>
            </div>
            """)

    def tearDown(self):
        # Clean up the test input and output files
        os.remove(self.test_input_html)
        shutil.rmtree(self.test_output_dir, ignore_errors=True)

    def test_convert_html_to_markdown(self):
        # Convert the HTML file to Markdown files
        convert_html_to_markdown(self.test_input_html, self.test_output_dir)

        # Check if the output files are created
        for file_name in self.expected_output_files:
            file_path = os.path.join(self.test_output_dir, file_name)
            self.assertTrue(os.path.exists(file_path))

            # Check the file content and creation time
            with open(file_path, "r") as f:
                content = f.read()
                self.assertIn("**Important** note.", content)
                self.assertIn("_Underlined_ note.", content)

            # Check the file creation time
            creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
            expected_time = datetime.strptime(file_name[:19], "%Y-%m-%d %H.%M.%S")
            self.assertEqual(creation_time.year, expected_time.year)
            self.assertEqual(creation_time.month, expected_time.month)
            self.assertEqual(creation_time.day, expected_time.day)
            self.assertEqual(creation_time.hour, expected_time.hour)
            self.assertEqual(creation_time.minute, expected_time.minute)
            self.assertEqual(creation_time.second, expected_time.second)

if __name__ == "__main__":
    unittest.main()
