#!/usr/bin/env python3
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
        /*color: navy;*/
        margin: 20px;
        width: 100%;
    }
    input[type="text"] {
        width: 100%;
        padding: 8px;
        box-sizing: border-box;
        margin-bottom: 20px;
        margin-left: 30px;
    }
    p, input[type="text"] {
        font-size: 16px;
        font-weight: bold;
        font-family: 'DejaVu Sans Mono', 'Courier New', Courier, monospace;
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
""")

    # Process each line in the file
    for line in lines:
        # Strip whitespace from the beginning and end of the line
        clean_line = line.strip()
        if clean_line:  # Check if line is not empty
            # Add paragraph and input field for each non-empty line
            html_content += f'<p>{clean_line}</p>\n<input type="text"><br>\n'

    html_content += '</body>\n</html>'

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

generate_html_from_text_file('aufgabe1')
