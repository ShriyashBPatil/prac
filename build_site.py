import os
import urllib.parse

def build_site():
    base_dir = r"c:\Users\Shriyash_Lab\Desktop\Python Prac"
    output_html = os.path.join(base_dir, "index.html")

    directories = [
        "01_Python_Fundamentals",
        "02_Data_Structures",
        "03_Functions",
        "04_Modules",
        "05_Exception_Handling",
        "06_File_IO",
        "07_Classes_Objects",
        "08_OOP_Concepts",
        "09_Flask_Basics",
        "10_Flask_Forms",
        "11_MySQL_Integration",
        "12_Flask_MySQL_CRUD"
    ]

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Programming Lab Index</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Fira+Code&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0f172a;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --card-bg: rgba(30, 41, 59, 0.7);
            --card-border: rgba(255, 255, 255, 0.1);
            --accent: #3b82f6;
            --accent-hover: #2563eb;
            --code-bg: #020617;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            color: var(--text-main);
            margin: 0;
            padding: 40px 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
        }

        h1 {
            font-weight: 800;
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 10px;
            background: -webkit-linear-gradient(45deg, #60a5fa, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            text-align: center;
            color: var(--text-muted);
            margin-bottom: 40px;
            font-size: 1.1rem;
        }

        .controls {
            display: flex;
            justify-content: center;
            margin-bottom: 40px;
        }

        .download-all {
            display: inline-block;
            padding: 12px 24px;
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            color: white;
            text-decoration: none;
            font-weight: 600;
            border-radius: 8px;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        }

        .download-all:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
        }

        .section {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            margin-bottom: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            overflow: hidden;
        }

        .section summary {
            font-size: 1.3rem;
            font-weight: 600;
            color: #e2e8f0;
            padding: 20px 24px;
            cursor: pointer;
            list-style: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background 0.2s;
        }

        .section summary:hover {
            background: rgba(255, 255, 255, 0.05);
        }

        .section summary::-webkit-details-marker {
            display: none;
        }
        
        .section summary::after {
            content: '+';
            font-size: 1.5rem;
            transition: transform 0.3s;
        }

        .section[open] summary::after {
            content: '−';
            transform: rotate(180deg);
        }
        
        .section[open] summary {
            border-bottom: 1px solid var(--card-border);
            background: rgba(255, 255, 255, 0.03);
        }

        .section-content {
            padding: 24px;
        }

        .program {
            margin-bottom: 20px;
            padding: 16px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 8px;
            transition: background 0.2s;
        }
        
        .program:last-child {
            margin-bottom: 0;
        }

        .program:hover {
            background: rgba(255, 255, 255, 0.05);
        }

        .program-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .program-title {
            font-weight: 600;
            font-size: 1.1rem;
            color: #f1f5f9;
            margin: 0;
        }

        .download-btn {
            padding: 8px 16px;
            background-color: var(--accent);
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 0.9rem;
            transition: background 0.2s;
        }

        .download-btn:hover {
            background-color: var(--accent-hover);
        }

        .code-container {
            position: relative;
            margin-top: 10px;
        }

        pre {
            background: var(--code-bg);
            padding: 16px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 0;
            font-family: 'Fira Code', monospace;
            font-size: 0.9rem;
            color: #a5b4fc;
            border: 1px solid #1e293b;
        }

        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(0,0,0,0.1); 
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.2); 
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(255,255,255,0.3); 
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Python Programming Lab</h1>
        <div class="subtitle">Index of all practical programs</div>
        
        <div class="controls">
            <a href="Python Prac.zip" class="download-all" download>Download Master Key (.zip)</a>
        </div>

"""
    
    for directory in directories:
        dir_path = os.path.join(base_dir, directory)
        if not os.path.isdir(dir_path):
            continue
            
        section_name = directory.replace('_', ' ')
        html_content += f'        <details class="section" id="{directory}">\n'
        html_content += f'            <summary>{section_name}</summary>\n'
        html_content += f'            <div class="section-content">\n'
        
        # Sort files alphabetically
        files = sorted(os.listdir(dir_path))
        for file in files:
            if file.endswith('.py') or file.endswith('.html'):
                file_path = os.path.join(dir_path, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code_content = f.read()
                except Exception as e:
                    code_content = f"Error reading file: {e}"
                
                # Create a data URI for download
                encoded_content = urllib.parse.quote(code_content)
                data_uri = f"data:text/plain;charset=utf-8,{encoded_content}"
                
                html_content += f'''
                <div class="program">
                    <div class="program-header">
                        <h3 class="program-title">{file}</h3>
                        <a href="{data_uri}" download="{file}" class="download-btn">Download Code</a>
                    </div>
                    <div class="code-container">
                        <pre><code>{code_content.replace('<', '&lt;').replace('>', '&gt;')}</code></pre>
                    </div>
                </div>
'''
        html_content += '            </div>\n'
        html_content += '        </details>\n'
        
    html_content += """
    </div>
</body>
</html>
"""

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Site generated successfully at: {output_html}")

if __name__ == "__main__":
    build_site()
