# 中医自学指南

> 基于北京中医药大学培养方案的中医专业自学指南，仿照 [CS 自学指南](https://csdiy.wiki/) 风格。

[![Deploy](https://github.com/etherealstarry/tcm-self-learning/actions/workflows/deploy.yml/badge.svg)](https://github.com/etherealstarry/tcm-self-learning/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Website](https://img.shields.io/badge/网站-csdiy.wiki-green)](https://etherealstarry.github.io/tcm-self-learning/)

---

## 🌿 在线阅读

**网站地址**：[https://etherealstarry.github.io/tcm-self-learning/](https://etherealstarry.github.io/tcm-self-learning/)

---

## 📖 关于本指南

本指南的诞生，源于笔者在中医学习过程中的切身感受——

中医学习之路，道阻且长。从《黄帝内经》的佶屈聱牙，到方剂学的浩如烟海，再到临床实习时的手足无措……每一个中医学子，都曾经历过这样的迷茫时刻。

本指南试图做一件小事：**把中医专业的核心课程体系，用清晰的结构、详实的笔记、精选的拓展资源，系统地呈现出来**。无论你是刚踏入中医殿堂的大一新生，还是正在备战考研/执业医的高年级同学，希望这里的内容能为你指明方向。

---

## 🗺️ 网站结构

```
tcm-self-learning/
├── docs/
│   ├── index.md                  # 首页
│   ├── 使用指南.md               # 如何使用这本书
│   ├── 学习规划.md               # 分年级学习规划
│   ├── 好书推荐.md               # 中医书籍推荐
│   ├── 后记.md                   # 后记与致谢
│   ├── 必修课程/                 # 核心必修课程
│   │   ├── index.md
│   │   ├── 中医基础/             # 中基、中诊、中药、方剂
│   │   ├── 中医经典/             # 内经、伤寒、金匮、温病
│   │   ├── 临床课程/             # 内、外、妇、儿科
│   │   └── 针灸推拿/             # 经络、针灸、推拿
│   ├── 西医基础/                 # 解剖、生理、病理、药理
│   ├── 拓展资源/                 # 在线课程、古籍数据库等
│   ├── 学习工具/                 # 文献管理、记忆工具等
│   └── 研究方向/                 # 中医各家学说、导师信息等
├── mkdocs.yml                   # MkDocs 配置文件
├── requirements.txt             # Python 依赖
└── .gitignore
```

---

## 🎯 本指南包含什么

- **📋 完整课程体系**：基于北京中医药大学中医专业培养方案，覆盖所有必修课程
- **📝 详细课程笔记**：每门核心课程按章节整理知识点，附思维导图
- **📜 经典导读**：四部经典的核心篇章解读，附历代注家观点
- **🔗 拓展资源**：优质网课、参考书目、学术论文、实用工具推荐
- **💡 学习方法**：中医思维培养、背诵技巧、临床跟诊心得
- **📋 考试指南**：期末考试、执业医师资格考试、考研的备考经验

---

## 🏫 为什么参照北京中医药大学

北京中医药大学（BUCM）是中华人民共和国成立后的第一所中医药高等学府，被誉为"中医药领域的北大清华"。其培养方案经过数十年打磨，课程体系完整、严谨，是国内中医药院校的重要参照标准。

本指南以 BUCM 的中医专业培养方案为蓝本，同时广泛参考上海中医药大学、广州中医药大学等院校的课程设置，力求兼顾系统性与实用性。

---

## 🛠️ 技术栈

- **静态网站生成器**：[MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 主题
- **部署平台**：GitHub Pages
- **构建工具**：`mkdocs gh-deploy --force`

---

## 🚀 本地运行

```bash
# 克隆仓库
git clone https://github.com/etherealstarry/tcm-self-learning.git
cd tcm-self-learning

# 安装依赖
pip install -r requirements.txt

# 本地预览
mkdocs serve
# 访问 http://127.0.0.1:8000

# 构建
mkdocs build

# 部署到 GitHub Pages
mkdocs gh-deploy --force
```

---

## 🤝 贡献方式

本指南是开源项目，欢迎每一位中医学子参与贡献！

- 🐛 **发现错误？**[提交 Issue](https://github.com/etherealstarry/tcm-self-learning/issues)
- ✍️ **想补充内容？**[提交 Pull Request](https://github.com/etherealstarry/tcm-self-learning/pulls)
- 💬 **有疑问或建议？**[参与讨论](https://github.com/etherealstarry/tcm-self-learning/discussions)

### 贡献指南

1. Fork 本仓库
2. 创建你的分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

---

## 📜 版权声明

本指南采用 **MIT 协议**开源。

- 本指南的原创内容（笔记、整理的资料等）采用 MIT 协议
- 引用的课程、书籍、论文等资源，其版权归原作者所有
- 如有侵权，请联系我们删除

---

## 🌿 致谢

- 感谢 [PKUFlyingPig/cs-self-learning](https://github.com/PKUFlyingPig/cs-self-learning) 项目带来的灵感
- 感谢北京中医药大学提供的公开培养方案信息
- 感谢每一位为本指南贡献内容的朋友

---

## 📞 联系方式

- **GitHub Issues**：[提交问题](https://github.com/etherealstarry/tcm-self-learning/issues)
- **邮箱**：（待补充）

---

> 🌿 *"博极医源，精勤不倦。"* —— 孙思邈《大医精诚》
