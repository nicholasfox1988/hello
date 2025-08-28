import markdown
import os

def convert_md_to_html(md_file_path, html_file_path=None):
    """
    将Markdown文件转换为HTML文件
    
    参数:
        md_file_path (str): Markdown文件的路径
        html_file_path (str, optional): 输出HTML文件的路径。如果未提供，则使用与Markdown文件相同的名称但扩展名为.html
    
    返回:
        str: 生成的HTML文件的路径
    """
    # 如果未提供HTML文件路径，则使用与Markdown文件相同的名称但扩展名为.html
    if html_file_path is None:
        html_file_path = os.path.splitext(md_file_path)[0] + '.html'
    
    # 读取Markdown文件
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    
    # 将Markdown转换为HTML
    html_content = markdown.markdown(md_content)
    
    # 创建完整的HTML文档
    full_html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{os.path.basename(md_file_path)}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }}
            h1, h2, h3, h4, h5, h6 {{
                color: #333;
                margin-top: 20px;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 4px;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 4px;
                overflow-x: auto;
            }}
            blockquote {{
                border-left: 4px solid #ddd;
                padding-left: 16px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # 写入HTML文件
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html_content)
    
    return html_file_path

# 使用示例
if __name__ == "__main__":
    # 替换为你的Markdown文件路径
    md_file = "readme.md"
    # 转换为HTML
    html_file = convert_md_to_html(md_file)
    print(f"转换完成!HTML文件已保存至: {html_file}")
