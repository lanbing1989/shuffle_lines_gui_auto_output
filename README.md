# shuffle_lines_gui_auto_output

本项目是一个用于自动化处理文本行随机排序的图形界面工具。它支持将输入的多行文本随机打乱顺序，并自动输出结果，适合文本处理、数据预处理、抽奖名单随机化等多种需求。

## 功能特点

- 简洁易用的图形化界面
- 支持多行文本输入
- 一键随机打乱所有行
- 自动输出并可复制结果
- 支持导入/导出文件
- 适用于 Windows、macOS、Linux

## 安装与运行

1. 克隆本仓库：

   ```bash
   git clone https://github.com/lanbing1989/shuffle_lines_gui_auto_output.git
   cd shuffle_lines_gui_auto_output
   ```

2. 安装依赖（如有 requirements.txt）：

   ```bash
   pip install -r requirements.txt
   ```

3. 运行程序：

   ```bash
   python main.py
   ```

   > 如果有可执行文件，可直接运行对应平台的可执行文件。

## 使用方法

1. 启动程序后，在文本框中输入或粘贴需要随机打乱的多行文本。
2. 点击“随机打乱”按钮，程序将自动生成新的随机顺序结果。
3. 可点击“复制输出”按钮将结果复制到剪贴板，或选择导出文件。

## 项目结构

- `main.py`：程序主入口
- `gui/`：图形界面相关代码
- `utils/`：文本处理等辅助工具
- `output/`：自动输出文件存放目录

## 贡献

欢迎提交 Issues 和 Pull Requests 改进本项目功能或修复 Bug。

## 许可证

本项目采用 MIT License 许可。详情见 [LICENSE](LICENSE) 文件。

---

如有任何问题，欢迎联系作者或提交 Issue。
