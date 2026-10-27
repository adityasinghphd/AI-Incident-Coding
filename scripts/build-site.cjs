const fs = require('node:fs');
const path = require('node:path');
const MarkdownIt = require('markdown-it');

const root = path.resolve(__dirname, '..');
const output = path.join(root, '_site');
const md = new MarkdownIt({ html: true });
const pages = [
  ...fs.readdirSync(root).filter(name => name.endsWith('.md')),
  'coding-kit/README.md',
  'coding-kit/START_CODING.md',
  'coding-kit/PROTOCOL.md',
  'coding-kit/CODEBOOK.md',
  'coding-kit/materials/CODING_MANUAL.md',
];
const pageSet = new Set(pages);
const navigation = pages.filter(name => /^0\d-/.test(name)).sort();

// Rewrite document links only; code examples and downloadable prompt files stay intact.
const renderLink = md.renderer.rules.link_open || ((tokens, i, options, env, self) => self.renderToken(tokens, i, options));
md.renderer.rules.link_open = (tokens, i, options, env, self) => {
  const href = tokens[i].attrGet('href');
  if (href && !/^(?:[a-z][a-z\d+.-]*:|\/|#)/i.test(href)) {
    const [target] = href.split(/[?#]/);
    const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(env.source), decodeURIComponent(target)));
    if (pageSet.has(resolved)) tokens[i].attrSet('href', href.replace(/\.md(?=[?#]|$)/, '.html'));
  }
  return renderLink(tokens, i, options, env, self);
};

fs.rmSync(output, { recursive: true, force: true });
fs.mkdirSync(output, { recursive: true });
// Keep the complete coding kit downloadable, including unmodified Markdown inputs.
for (const item of ['coding-kit', 'figures', 'LICENSE', '.nojekyll']) {
  fs.cpSync(path.join(root, item), path.join(output, item), { recursive: true });
}
fs.cpSync(path.join(root, 'site/style.css'), path.join(output, 'style.css'));
const escape = md.utils.escapeHtml;
for (const source of pages) {
  const text = fs.readFileSync(path.join(root, source), 'utf8');
  const title = text.match(/^# (.+)$/m)?.[1] || source;
  const prefix = '../'.repeat(source.split('/').length - 1);
  const nav = navigation.map((name, i) => `<a href="${prefix}${name.replace(/\.md$/, '.html')}">${i === 0 ? 'Start here' : String(i).padStart(2, '0')}</a>`).join('');
  const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escape(title)}</title><link rel="stylesheet" href="${prefix}style.css"></head>
<body><main><nav aria-label="Reviewer documents">${nav}<a href="${prefix}coding-kit/README.html">Code your own incidents</a></nav>
${md.render(text, { source })}
<footer>Independent human validation materials must remain separate from held-out model outputs. <a href="${prefix}00-start-here.html">Return to overview</a> · <a href="${prefix}LICENSE-CONTENT.html">Content license</a></footer></main></body></html>\n`;
  const target = path.join(output, source.replace(/\.md$/, '.html'));
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.writeFileSync(target, html);
}
// Both existing entry URLs come from the same Markdown source.
fs.copyFileSync(path.join(output, '00-start-here.html'), path.join(output, 'index.html'));
console.log(`Built ${pages.length + 1} HTML pages in _site/`);
