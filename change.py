import markdown
import os

def md_to_html(md_filename='readme.md', html_filename='readme.html'):
    """将Markdown文件转换为HTML文件"""
    
    # 获取当前文件所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 构建完整的文件路径
    md_path = os.path.join(current_dir, md_filename)
    html_path = os.path.join(current_dir, html_filename)
    
    try:
        # 读取Markdown
        with open(md_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # 转换为HTML
        html = markdown.markdown(text)
        
        # 写入HTML文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f'成功将 {md_filename} 转换为 {html_filename}')
        return True
        
    except Exception as e:
        print(f'转换失败: {e}')
        return False

if __name__ == '__main__':
    md_to_html()