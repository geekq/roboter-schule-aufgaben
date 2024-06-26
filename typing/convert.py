#!/usr/bin/env python3
import sys
def generate_html_from_text_file(name):
    input_filename = f"{name}.txt"
    output_filename = f"{name}.html"
    # Read lines from the text file
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Start the HTML content
    html_content = ("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
"""
    f"<title>{name}</title>"
    """
<style>
    body {
        width: 80%;
        color: black;
    }
    p {
        margin-left: 7px;
        margin-bottom: 3px;
        width: 100%;
    }
    input[type="text"] {
        width: 100%;
        padding: 8px;
        box-sizing: border-box;
        margin-bottom: 10px;
        margin-left: 0px;
    }
    p, input[type="text"], div.note .boxed {
        font-size: 24px;
        font-weight: bold;
        font-family: 'DejaVu Sans Mono', 'Courier New', Courier, monospace;
    }
    div.note {
        color: purple;
        font-size: 30px;
        margin-top: 20px;
    }
    div.note .boxed {
        border: 2px solid purple;
        padding-left: 5px;
        padding-right: 5px;
    }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    console.log('Page fully loaded');
    var inputs = document.querySelectorAll('input[type="text"]');
    if (inputs.length > 0) {
        inputs[0].focus(); // Focus on the first input field
    }
});

    // Add any additional JavaScript you want to run at start here
    document.addEventListener('DOMContentLoaded', function () {
        const inputs = document.querySelectorAll('input');
        inputs.forEach((input, index) => {
            input.addEventListener('keyup', function(event) {
                if (event.key === 'Enter') {
                    event.preventDefault(); // Prevent the default form submit on Enter key
                    if (index < inputs.length - 1) { // Check if it's not the last input field
                        inputs[index + 1].focus(); // Move focus to the next input field
                    }
                }
            });
        });
    });
</script>
</head>
<body>
"""
f"""
<a href="../typing.html">alle Aufgaben</a>
<h1>{name}</h1>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/QWERTZ-10Finger-Layout.svg/2560px-QWERTZ-10Finger-Layout.svg.png" alt="Tasten Zuordnung" width="100%">
<ol>
""")

    for line in lines:
        # Strip whitespace from the beginning and end of the line
        clean_line = line.strip()
        if clean_line:  # Check if line is not empty
            # Add paragraph and input field for each non-empty line
            if clean_line.startswith('#'):
                s = clean_line[1:].replace("'", "</span>").replace("`", "<span class='boxed'>")
                html_content += f"""<div class="note">{s}</div>"""
            else:
                html_content += f"""<li><p>{clean_line}</p>\n<input type="text" spellcheck="false"><br></li>\n"""

    html_content += '</ol>\n</body>\n</html>'

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

if sys.argv[1] == 'all':
    lessons = list(range(1, 14+1)) + list(range(21, 22+1)) + list(range(41, 41+1))
    for i in lessons:
        generate_html_from_text_file(f'aufgabe{i}')
        print(f"* [Aufgabe {i}](typing/aufgabe{i}.html)")
else:
    generate_html_from_text_file(sys.argv[1]) # e.g. 'aufgabe1'

