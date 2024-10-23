# Flomo2MD

## 项目简介
Flomo2MD 是一个将 Flomo 笔记导出为 Markdown 格式的工具。它可以帮助用户将 Flomo 中的笔记批量导出，并保存为 Markdown 文件，方便在其他平台或编辑器中使用。

## 安装

### 使用 Poetry
1. 确保你已经安装了 [Poetry](https://python-poetry.org/docs/#installation)。
2. 克隆项目仓库：
   ```bash
   git clone https://github.com/yourusername/flomo2md.git
   cd flomo2md
   ```
3. 安装依赖：
   ```bash
   poetry install
   ```

### 使用 pip
1. 克隆项目仓库：
   ```bash
   git clone https://github.com/yourusername/flomo2md.git
   cd flomo2md
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用说明

### 导出笔记
1. 运行导出脚本：
   ```bash
   poetry run python flomo_exporter/exporter.py
   ```
   或者
   ```bash
   python flomo_exporter/exporter.py
   ```
2. 按照提示输入 Flomo 的 API 密钥和其他必要信息。
3. 导出的 Markdown 文件将保存在 `output` 目录中。

### 示例
以下是一个导出的 Markdown 文件示例：
```markdown
# 2024-10-23

## 笔记标题
这是一条来自 Flomo 的笔记。

## 另一条笔记
这是另一条笔记的内容。
```

## 贡献
我们欢迎任何形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解更多信息。

## 许可证
本项目采用 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。
