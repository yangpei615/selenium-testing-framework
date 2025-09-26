A robust web automation testing framework built with Python + Selenium + Pytest, following the Page Object Model (POM) design pattern. Designed for maintainability, scalability, and ease of use in UI test automation.

Perfect for learning, regression testing, and CI/CD integration.

 项目简介

这是一个基于 Python + Selenium + Pytest 构建的 Web 自动化测试框架，采用 Page Object Model (POM) 设计模式，旨在提升代码可维护性、可扩展性和易用性。

适用于：
学习自动化测试
回归测试
持续集成（CI/CD）流程

项目结构
shangma_selenium_test/
│
├── commons/          # 公共工具类（如日志、配置、等待等）
├── data/             # 测试数据文件（JSON/Excel/YAML）
├── report/           # 测试报告输出目录（Allure 或 HTML）
├── script/           # 线性脚本或调试脚本（Page Objects）
├── testcases/        # 测试用例文件（pytest 格式）
├── init.py           # 包初始化
├── main.py           # 主入口脚本
├── pytest.ini        # Pytest 配置文件
└── README.md         # 项目说明文档
