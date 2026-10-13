# -*- coding: utf-8 -*-
"""Build docs/index.html by inlining tools.json so the site works on GitHub Pages and file://."""
import json, pathlib

root = pathlib.Path(__file__).parent
data = json.loads((root / "tools.json").read_text(encoding="utf-8"))
docs = root / "docs"
docs.mkdir(exist_ok=True)

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Tools 导航 - 精选国内外好用的 AI 工具</title>
<meta name="description" content="精选国内外好用的 AI 工具，按场景分类，标注免费情况，持续更新">
<style>
  :root {
    --bg: #f7f7fb; --card: #ffffff; --text: #1f2328; --muted: #656d76;
    --accent: #7c3aed; --accent-soft: #f1ebfd; --border: #e6e4ee; --radius: 14px;
    --green: #0e9f6e; --green-soft: #e7f6f0; --amber: #b7791f; --amber-soft: #fdf3e3;
    --red: #d64545; --red-soft: #fdecec;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: -apple-system, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif;
         background: var(--bg); color: var(--text); line-height: 1.6; }
  .wrap { max-width: 1080px; margin: 0 auto; padding: 0 20px; }
  header.hero { text-align: center; padding: 64px 20px 36px; }
  header.hero h1 { font-size: 2.4rem; letter-spacing: -0.5px; }
  header.hero p.sub { color: var(--muted); margin-top: 12px; font-size: 1.05rem; }
  .stats { margin-top: 18px; display: flex; gap: 24px; justify-content: center; flex-wrap: wrap; }
  .stat { background: var(--card); border: 1px solid var(--border); border-radius: 999px;
          padding: 6px 18px; font-size: 0.9rem; color: var(--muted); }
  .stat b { color: var(--accent); }
  .toolbar { position: sticky; top: 0; z-index: 10; background: rgba(247,247,251,0.92);
             backdrop-filter: blur(8px); padding: 14px 0 10px; border-bottom: 1px solid var(--border); }
  .search { width: 100%; padding: 12px 18px; border: 1px solid var(--border); border-radius: 999px;
            font-size: 1rem; background: var(--card); outline: none; transition: border-color .15s; }
  .search:focus { border-color: var(--accent); }
  .chips { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
  .chip { padding: 5px 14px; border-radius: 999px; border: 1px solid var(--border);
          background: var(--card); cursor: pointer; font-size: 0.88rem; color: var(--muted);
          transition: all .15s; user-select: none; }
  .chip:hover { border-color: var(--accent); color: var(--accent); }
  .chip.active { background: var(--accent); border-color: var(--accent); color: #fff; }
  main { padding: 28px 0 60px; }
  .cat-title { display: flex; align-items: baseline; gap: 10px; margin: 30px 0 14px; }
  .cat-title h2 { font-size: 1.25rem; }
  .cat-title span { color: var(--muted); font-size: 0.85rem; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 14px; }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
          padding: 18px 20px; transition: transform .15s, box-shadow .15s; display: flex; flex-direction: column; }
  .card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(31,35,40,0.08); }
  .card .head { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
  .card h3 { font-size: 1.02rem; }
  .badges { display: flex; gap: 6px; flex-shrink: 0; }
  .badge { font-size: 0.72rem; border-radius: 6px; padding: 2px 8px; font-weight: 600; }
  .badge.free { background: var(--green-soft); color: var(--green); }
  .badge.freemium { background: var(--amber-soft); color: var(--amber); }
  .badge.paid { background: var(--red-soft); color: var(--red); }
  .badge.cn { background: var(--accent-soft); color: var(--accent); }
  .card p.desc { color: var(--muted); font-size: 0.88rem; margin: 8px 0 0; flex: 1; }
  .card .foot { margin-top: 12px; }
  .btn { display: inline-block; padding: 7px 14px; border-radius: 8px; border: 1px solid var(--border);
         font-size: 0.82rem; background: var(--card); color: var(--accent); text-decoration: none;
         transition: all .15s; }
  .btn:hover { border-color: var(--accent); }
  footer { text-align: center; padding: 36px 20px 48px; color: var(--muted); font-size: 0.88rem; }
  footer a { color: var(--accent); text-decoration: none; }
  .empty { text-align: center; color: var(--muted); padding: 60px 0; }
  .legend { display: flex; gap: 14px; justify-content: center; margin-top: 14px; flex-wrap: wrap;
            font-size: 0.78rem; color: var(--muted); }
  @media (max-width: 600px) { header.hero h1 { font-size: 1.8rem; } }
</style>
</head>
<body>
<header class="hero">
  <h1>🧭 AI Tools 导航</h1>
  <p class="sub">精选国内外好用的 AI 工具 · 按场景分类 · 标注免费情况 · 持续更新</p>
  <div class="stats">
    <div class="stat"><b id="statTools">0</b> 款工具</div>
    <div class="stat"><b id="statCn">0</b> 款国产</div>
    <div class="stat">CC0 协议 · 随意使用</div>
  </div>
  <div class="legend">
    <span>🟢 免费</span><span>🟡 免费+付费</span><span>🔴 付费</span><span>🟣 国产（国内可直接访问）</span>
  </div>
</header>

<div class="toolbar">
  <div class="wrap">
    <input class="search" id="search" type="search" placeholder="🔍 搜索工具，如：PPT、视频、编程…">
    <div class="chips" id="chips"></div>
  </div>
</div>

<main class="wrap" id="main"></main>

<footer>
  <p>用 ❤️ 维护 · <a href="https://github.com/AnonymousLeeJJ/ai-tools-nav" target="_blank" rel="noopener">GitHub 仓库</a> · 欢迎 Star ⭐ 与投稿</p>
</footer>

<script id="tools-data" type="application/json">__DATA__</script>
<script>
const DATA = JSON.parse(document.getElementById('tools-data').textContent);
const { categories, tools } = DATA;
const state = { q: '', cat: 'all' };
const PRICE = { free: '免费', freemium: '免费+付费', paid: '付费' };

document.getElementById('statTools').textContent = tools.length;
document.getElementById('statCn').textContent = tools.filter(t => t.cn).length;

const chipsEl = document.getElementById('chips');
const mainEl = document.getElementById('main');

function renderChips() {
  const all = [{ id: 'all', name: '全部', icon: '✨' }, ...categories,
               { id: 'free', name: '纯免费', icon: '🆓' }, { id: 'cn', name: '国产', icon: '🇨🇳' }];
  chipsEl.innerHTML = all.map(c =>
    `<span class="chip ${state.cat === c.id ? 'active' : ''}" data-id="${c.id}">${c.icon || ''} ${c.name}</span>`
  ).join('');
  chipsEl.querySelectorAll('.chip').forEach(el =>
    el.addEventListener('click', () => { state.cat = el.dataset.id; renderChips(); renderList(); }));
}

function matches(t) {
  if (state.cat === 'free' && t.price !== 'free') return false;
  if (state.cat === 'cn' && !t.cn) return false;
  if (!['all', 'free', 'cn'].includes(state.cat) && t.category !== state.cat) return false;
  if (!state.q) return true;
  const q = state.q.toLowerCase();
  return (t.name + t.description).toLowerCase().includes(q);
}

function renderList() {
  const groups = categories
    .map(c => ({ cat: c, items: tools.filter(t => t.category === c.id && matches(t)) }))
    .filter(g => g.items.length);
  if (!groups.length) {
    mainEl.innerHTML = '<div class="empty">没有找到匹配的工具，换个关键词试试 🧐</div>';
    return;
  }
  mainEl.innerHTML = groups.map(g => `
    <div class="cat-title"><h2>${g.cat.icon} ${g.cat.name}</h2><span>${g.items.length} 款</span></div>
    <div class="grid">${g.items.map(t => `
      <div class="card">
        <div class="head"><h3>${t.name}</h3>
          <div class="badges">
            ${t.cn ? '<span class="badge cn">国产</span>' : ''}
            <span class="badge ${t.price}">${PRICE[t.price]}</span>
          </div></div>
        <p class="desc">${t.description}</p>
        <div class="foot"><a class="btn" href="${t.url}" target="_blank" rel="noopener">🔗 访问官网</a></div>
      </div>`).join('')}
    </div>`).join('');
}

document.getElementById('search').addEventListener('input', e => { state.q = e.target.value.trim(); renderList(); });
renderChips();
renderList();
</script>
</body>
</html>
"""

html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False))
(docs / "index.html").write_text(html, encoding="utf-8")
print("OK ->", docs / "index.html", f"({len(data['tools'])} tools)")
