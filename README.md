# 个人网站

余俊鋒（Chopin J.F. Yu）的学术个人主页：研究、著作、教学与联系方式。

> 状态：第二版，已从「开发者作品集」改为「学者主页」。纯 HTML + CSS，本地已跑通。

## 本地预览

在项目目录执行：

    python3 -m http.server 8000

浏览器打开 <http://localhost:8000>。改完文件刷新即可，没有构建步骤。

## 文件结构

    personal-website/
    ├── index.html          # 首页：首屏 / 简介 / 研究 / 著作精选 / 教学 / 联系
    ├── publications.html   # 完整清单：期刊论文 / 会议论文 / 学位论文
    ├── style.css           # 全部样式，含深色模式、打印样式、响应式
    ├── assets/
    │   ├── portrait.svg    # 4:5 肖像占位图，换成自己的照片
    │   ├── favicon.svg     # 标签页图标（「余」）
    │   └── pubs/           # 论文 PDF，点「下载 PDF」直接下载
    │       ├── yu-2016-law-and-social-attitudes.pdf
    │       ├── yu-2018-ma-thesis.pdf
    │       └── yu-2021-border-trade-pingxiang.pdf
    ├── README.md
    └── .gitignore

## 内容从哪来

- `CV 2021 Auguest.docx`（iCloud Drive 根目录）：姓名、学历、导师、研究领域、语言、荣誉、2016 年期刊论文、三次会议报告、研究/教学助理经历
- 2021 年〈當代中國的邊境貿易：對廣西壯族自治區憑祥市的初步觀察〉（《人類與文化》46 期，有 DOI）——CV 上没有，从 Downloads 里的 PDF 补入
- 2018 年硕士论文《情慾、身份與法律：十八世紀中國社會中的雞姦犯罪》（東吳大學歷史學系）——全文 PDF 已上站

**没有采用** CV 上的手机号——网站公开，只放邮箱。

## 怎么加一篇论文（含 PDF 下载）

1. 把 PDF 放进 `assets/pubs/`，文件名用英文小写加连字符，例如 `yu-2024-fieldwork.pdf`
2. 打开 `publications.html`，先决定放哪一栏：
   - 期刊论文：`<section id="articles">` 里的 `<ol class="pub-list">`
   - 会议论文：`<section id="conferences">` 里的 `<ol class="pub-list">`
   - 学位论文：`<section id="theses">` 里的 `<ol class="pub-list">`

   复制一个 `<li class="pub">…</li>`，改年份、标题、刊物或会议
3. 在条目里加下载链接（相对路径，GitHub Pages 上直接可用）：

       <div class="pub-links">
         <a class="pub-link" href="assets/pubs/yu-2024-fieldwork.pdf"
            download="yu-2024-fieldwork.pdf" type="application/pdf">
           下载 PDF <span class="pub-size">2.1 MB ↓</span>
         </a>
         <a class="pub-link pub-link-quiet" href="https://doi.org/10.xxxx/xxxx" rel="noopener">DOI ↗</a>
       </div>

4. 本地打开 <http://localhost:8000/publications.html> 点一下，确认能下载
5. push 到 GitHub 后，线上同样可下载；PDF 就是仓库里的普通文件，不需要额外配置

几点说明：

- `download` 属性在同源下生效（Chrome / Firefox / Edge）；Safari 可能直接在标签页里打开 PDF，不影响阅读
- 文件大小写在链接里（如 `1.3 MB`），读者能预判下载量；超过 10 MB 建议压缩
- 投稿前确认出版社允许自存档（绿色 OA）。若不允许，删掉 PDF 链接、只留 DOI 即可
- 文件名不要用中文和空格，部署到 Pages 后更稳

## 还需要补的内容（页面里已标「待补」）

| 位置 | 缺什么 |
| --- | --- |
| `index.html` 首屏 | 真人照片（4:5，建议 800×1000 以上），替换 `assets/portrait.svg` |
| 研究 · 共谋 | 博士论文题目、正式田野地点与时间（2019 年 11 月凭祥两周为初步田野，已写入） |
| `publications.html` | 2022 年以来的新文章、书稿、会议报告 |
| 联系 | 最新 CV 的 PDF（现在写「可来信索取」）、Google Scholar / ORCID 链接 |
| 全站 | 当前身份确认（博士候选人 / 已毕业 / 博士后），首屏和简介里的措辞要跟着改 |

## 上线前改这几处

| 位置 | 现在 | 说明 |
| --- | --- | --- |
| 邮箱 | `chopinfisher@gmail.com` | 首页 2 处、著作页页脚不涉及；替换时全站搜一遍 |
| 肖像 | `assets/portrait.svg` | 换成 `photo.jpg` 后改 `index.html` 里的 `src` |
| 著作 | 2016–2021 条目 | 在 `publications.html` 对应栏目复制一个 `<li class="pub">` 即可加新条目 |
| PDF | `assets/pubs/` 两个文件 | 换版本时同名覆盖即可，不用改 HTML |
| 机构链接 | `https://anthro.ntu.edu.tw/` | 已确认可访问 |

## 设计说明

- **学术版式**：左侧编号栏 + 右侧正文，衬线字体排正文，出版清单按年份悬挂缩进
- **著作分栏**：期刊论文、会议论文、学位论文各自成栏，会议论文只放报告、不放 PDF
- **两页结构**：著作会越来越长，单独一页；首页只放精选（2 篇期刊 + 2 篇会议 + 1 篇学位论文）
- **深色模式**跟随系统，不设切换按钮
- **打印样式**：打印时自动隐藏导航和按钮，适合打 CV 或阅读版
- **零依赖**：没有 JavaScript、外链字体、CDN 和追踪脚本，GitHub Pages 可直接托管

## 部署（GitHub Pages）

仓库已在本地初始化，`main` 分支完成第一次提交。本机没有 Xcode 命令行工具，用的是 GitHub Desktop 自带的 git。

1. 打开 GitHub Desktop → **File → Add Local Repository**，选择本项目目录
2. 右上角 **Publish repository**：名字填 `personal-website`，**不要勾 Private**（免费版 Pages 需要公开仓库）
3. 在 GitHub 网页打开仓库 **Settings → Pages** → Source 选 `main` / `/ (root)` → Save
4. 等 1 分钟，访问 `https://<用户名>.github.io/personal-website/`

以后改完内容，在 GitHub Desktop 里填一句提交信息，点 **Commit to main** → **Push origin**，线上自动更新。

## 待办

- [x] 按 CV 重写文案：简介（中英）、研究、著作、教学、联系
- [x] 拆出 `publications.html`
- [x] 手机端适配 + 深色模式 + 打印样式
- [x] 本地 `python3 -m http.server` 跑通
- [x] 两篇期刊论文的 PDF 下载（2016《史轍》、2021《人類與文化》）
- [x] 2018 年硕士论文全文 PDF 上站（東吳大學歷史學系）
- [x] git 初始化并完成首次提交（GitHub Desktop 自带 git）
- [ ] 换真人照片
- [ ] 补 2022 年以后的发表与当前身份
- [ ] 补博士论文题目、正式田野地点与时间
- [ ] 放最新 CV 的 PDF
- [ ] 加 Google Scholar / ORCID（如果有）
- [ ] 发布到 GitHub、开启 Pages
- [ ] （可选）绑定自己的域名
