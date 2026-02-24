import os
from pathlib import Path

# --- 配置区 ---
OUTPUT_FILE = "project_snapshot.md"  # 改为 .md 格式，方便在 GitHub/IDE 中阅读
# 增加现代前端常用的忽略项
IGNORE_DIRS = {
    '.git', 'node_modules', '__pycache__', 'venv', '.vercel', '.vscode', 
    'dist', 'build', '.next', '.turbo', 'out', 'coverage','themes','public'
}
# 增加常见的非文本后缀
IGNORE_EXTS = {
    '.exe', '.pyc', '.pyo', '.png', '.jpg', '.jpeg', '.gif', '.svg', 
    '.zip', '.tar', '.gz', '.mp4', '.pdf', '.ico', '.woff', '.woff2', '.ttf'
}
# 增加需要排除的具体文件名（特别是脚本自身和生成的输出文件）
IGNORE_FILES = {'copy.py', OUTPUT_FILE, 'package-lock.json', 'pnpm-lock.yaml', 'yarn.lock'}

MAX_FILE_SIZE_KB = 100 

def should_ignore(path: Path):
    """判断是否应该忽略该路径"""
    # 检查是否在忽略目录中
    if any(part in IGNORE_DIRS for part in path.parts):
        return True
    # 检查后缀
    if path.suffix.lower() in IGNORE_EXTS:
        return True
    # 检查文件名
    if path.name in IGNORE_FILES:
        return True
    return False

def generate_project_snapshot():
    current_dir = Path.cwd()
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"# Project Snapshot: {current_dir.name}\n\n")
        
        # 1. 生成目录树（使用 Markdown 代码块）
        f.write("## 1. Directory Structure\n")
        f.write("```text\n")
        
        tree_lines = []
        for root, dirs, files in os.walk(current_dir):
            # 过滤目录
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            rel_root = Path(root).relative_to(current_dir)
            level = len(rel_root.parts)
            indent = '  ' * level
            
            if rel_root == Path('.'):
                tree_lines.append(f"{current_dir.name}/")
            else:
                tree_lines.append(f"{indent}{os.path.basename(root)}/")
            
            sub_indent = '  ' * (level + 1)
            for file in sorted(files):
                file_path = Path(root) / file
                if not should_ignore(file_path):
                    tree_lines.append(f"{sub_indent}{file}")
        
        f.write("\n".join(tree_lines))
        f.write("\n```\n\n")
        
        # 2. 写入文件内容
        f.write("## 2. File Contents\n\n")
        
        for root, dirs, files in os.walk(current_dir):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            for file in sorted(files):
                file_path = Path(root) / file
                if should_ignore(file_path):
                    continue
                
                rel_path = file_path.relative_to(current_dir)
                file_size = file_path.stat().st_size / 1024
                
                # 使用 Markdown 三级标题标注文件名
                f.write(f"### 文件路径: `{rel_path}`\n")
                
                if file_size > MAX_FILE_SIZE_KB:
                    f.write(f"> [!WARNING] 文件过大 ({file_size:.2f} KB)，已跳过内容读取。\n\n")
                    continue
                
                # 根据后缀识别代码块语言
                lang = file_path.suffix.lstrip('.')
                if lang == 'py': lang = 'python'
                if lang == 'ts': lang = 'typescript'
                if lang == 'tsx': lang = 'typescript'
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as code_f:
                        content = code_f.read()
                        f.write(f"```{lang}\n")
                        f.write(content)
                        f.write("\n```\n\n")
                except Exception as e:
                    f.write(f"**Error:** 无法读取文件 - {e}\n\n")

if __name__ == "__main__":
    print(f"🚀 正在分析项目并生成 {OUTPUT_FILE}...")
    generate_project_snapshot()
    print(f"✨ 完成！你可以将 {OUTPUT_FILE} 发送给其他开发者或 AI。")