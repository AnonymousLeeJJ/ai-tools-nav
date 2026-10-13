# 贡献指南 / Contributing

感谢你为 AI Tools 导航添砖加瓦！🎉

## 收录标准

- ✅ 工具**真实可用**，提交前请实际访问官网验证
- ✅ 有明确的 AI 能力（不是传统软件蹭 AI 标签）
- ✅ 每个分类只收**同场景里公认好用**的工具，宁缺毋滥
- ✅ `price` 字段如实标注：`free`（完全免费）/ `freemium`（免费+付费）/ `paid`（纯付费）
- ✅ `cn` 字段如实标注：国内是否可直接访问使用
- ❌ 不收需要邀请码且普通用户无法注册的产品
- ❌ 不接受厂商付费收录

## 提交格式

在 `tools.json` 的 `tools` 数组中添加：

```json
{
  "name": "工具名称",
  "url": "https://官网地址",
  "category": "chat",
  "price": "freemium",
  "cn": false,
  "description": "一句话说明它最突出的能力"
}
```

`category` 可选值：`chat` / `search` / `coding` / `image` / `video` / `audio` / `office` / `agent`

提交后运行 `python build_site.py` 重新生成导航站，一并提交。

## 信息纠错

工具改名、涨价、停服了？开 Issue 标题格式：`[纠错] 工具名称 + 变化内容`。
