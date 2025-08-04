# Tea 语言编译器
Tea 是一个轻量级的领域特定语言（DSL）编译器，专为简化 Python 编程体验而设计。它将简洁的 .tea 脚本文件编译为可执行的 Python 代码，让开发者能够用更少的代码实现相同的功能。

✨ 核心特性
极简语法：通过直观的函数调用语法降低学习门槛
即时编译：支持一键将 .tea 文件编译为 .py 可执行文件
跨平台兼容：基于 Python 构建，现在支持 Windows
零依赖运行：编译后的 Python 文件无需额外依赖即可执行
🚀 快速开始
安装与配置

bash
## 克隆项目
git clone https://github.com/SY-LSK/tea.git
cd tea

## 创建虚拟环境（可选）
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
## 或 .venv\Scripts\activate  # Windows
基本用法

bash
## 编译并运行示例
python tea.py run -p a.tea

## 查看帮助
python tea.py -h
编写第一个 Tea 程序
创建 hello.tea：


tea
Apply
tout('Hello, Tea!');
tin('请输入你的名字：');
编译后自动生成的 hello.py：


python
Apply
print('Hello, Tea!')
input('请输入你的名字：')
🛠️ 技术架构
项目结构

plainText
tea/
├── tea.py              # 主入口文件
├── using_model/        # 核心编译模块
│   ├── tea_use.py      # 文件处理与编译流程
│   ├── tea_compile.py  # 语法转换引擎
│   ├── tea_object.py   # Token 对象模型
│   └── tea_constant.py # 语言定义常量
├── else_package/       # 工具模块
│   ├── command_parser.py  # 命令行解析
│   └── color_console.py   # 彩色日志输出
├── a.tea               # 示例代码
└── tea.json            # 项目配置
编译流程
词法分析：将 .tea 文件拆分为 Token 流
语法转换：将 Token 映射为 Python 语法结构
代码生成：输出标准 Python 文件
即时执行：可选的自动运行编译结果
📖 语言规范
当前支持的语法
| Tea 语法 | 等效 Python | 说明 | |----------|-------------|------| | tout('文本') | print('文本') | 标准输出 | | tin('提示') | input('提示') | 标准输入 |

扩展语法（开发中）

tea
Apply
var(name, "张三")  # 变量声明
🎯 开发路线图
近期计划
[ ] 添加变量声明与赋值语法
[ ] 支持基础算术运算
[ ] 实现条件判断语句
[ ] 添加循环控制结构
长期愿景
[ ] 类型注解系统
[ ] 模块导入机制
[ ] 调试符号支持
[ ] 性能分析工具
🤝 参与贡献
我们欢迎所有形式的贡献！您可以通过以下方式参与：

报告问题：在 GitHub Issues 提交发现的 Bug
功能建议：分享您对语言特性的想法
代码贡献：提交 Pull Request 改进编译器
文档完善：帮助改进教程和示例
