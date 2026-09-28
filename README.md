# visualization-innovation

科研可视化创新设计 skill：图表二创、新视图发明、交互与多图联动创新、证据驱动的视觉叙事，以及面向发表的 novelty 边界评估。

定位是**机制层的创新设计**——从分析问题出发设计有用、可测试的视觉/交互机制，而不是换配色式的样式打磨。数据语义与学术诚信受严格约束：不虚称 first-ever / SOTA，区分 stored-query / simulation / real recompute，文献线索须回溯一手来源后才能引用。

## 触发场景

- 二创一张参考图表（拆解 → 继承/改变/增益/成本账本）
- 发明新视图或新图表族（视觉语法 + 解码规则 + 基线对比）
- 生成机制上互异的多方案（Familiar+ / Recombined / Speculative 三档发散）
- 设计交互与联动视图（可测试的跨视图链接契约）
- 组织多面板布局（互补证据角色与依赖图）
- 评估发表新颖性（先例检索台账 + 有边界的 claim）

SKILL.md 的 description 中含中英触发词（图表二创 / 新视图 / 交互创新 / 多图联动创新），安装后由 agent 自动路由。

## 目录结构

```
SKILL.md                  # 入口：路由表 + 执行流程 + 护栏
references/               # 按任务加载的方法论文档（反模式、评估量表、先例检索等）
assets/                   # 候选卡 / 设计简报 / 联动契约模板
scripts/                  # 见下
agents/openai.yaml        # agent 平台元信息
```

## 脚本

均需 Python 3，无第三方依赖（`validate_skill.py` 需 PyYAML）：

```bash
python scripts/scaffold_innovation_brief.py --help   # 拷贝设计简报模板
python scripts/score_candidates.py --help            # 候选方案诊断分流（gate 制，不做自动排名）
python scripts/validate_skill.py <skill_dir>         # skill 结构校验
python scripts/package_skill.py --help               # 打包导出
```

## 安装

```bash
git clone https://github.com/techdou/visualization-innovation.git ~/.agents/skills/visualization-innovation
```

或下载 zip 解压到 `~/.agents/skills/` 下。重启会话后生效。

## 配套 skill

与 [research-visual-analytics](https://github.com/techdou/research-visual-analytics) 成对使用：本 skill 负责创新设计，对方负责编码正确性与证据审查；两者共享 coordination-contract 契约模板，也可各自独立工作。

## License

MIT
