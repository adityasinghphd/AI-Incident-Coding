const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const output = path.join(root, '_site');
function files(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const file = path.join(dir, entry.name);
    return entry.isDirectory() ? files(file) : [file];
  });
}
let links = 0;
for (const file of files(output).filter(file => file.endsWith('.html'))) {
  const html = fs.readFileSync(file, 'utf8');
  for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const url = match[1];
    if (/^(?:[a-z][a-z\d+.-]*:|\/\/|#)/i.test(url)) continue;
    const target = path.resolve(path.dirname(file), decodeURIComponent(url.split(/[?#]/)[0]));
    assert.ok(fs.existsSync(target), `${path.relative(output, file)}: missing ${url}`);
    links++;
  }
}
for (const file of files(path.join(root, 'coding-kit'))) {
  const relative = path.relative(root, file);
  assert.deepEqual(fs.readFileSync(path.join(output, relative)), fs.readFileSync(file), `Coding material changed: ${relative}`);
}
assert.equal(fs.readFileSync(path.join(output, 'index.html'), 'utf8'), fs.readFileSync(path.join(output, '00-start-here.html'), 'utf8'));
console.log(`Checked ${links} local links and assets; coding-kit files are unchanged; entry pages match.`);
