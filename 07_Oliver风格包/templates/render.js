// Render a template page to PNG.
//   node render.js "cover.html?w=1280&h=769&title=..." out.png
// Width and height come from the w/h query (gallery is always 1280x769).
// Needs Playwright (npm i -D playwright, or a global install).
const path = require('path');
const { pathToFileURL } = require('url');
let chromium;
try { ({ chromium } = require('playwright')); } catch { ({ chromium } = require('/opt/node22/lib/node_modules/playwright')); }

(async () => {
  const [, , page, out] = process.argv;
  if (!page || !out) { console.error('usage: node render.js "<template.html?query>" <out.png>'); process.exit(1); }
  // Literal text is fine in the query; a literal "+" is kept as a plus sign, not a space.
  const [file, rawQuery = ''] = page.split('?');
  const query = rawQuery.replace(/\+/g, '%2B');
  const q = new URLSearchParams(query);
  const gallery = path.basename(file).startsWith('gallery');
  const w = gallery ? 1280 : (+q.get('w') || 1280);
  const h = gallery ? 769 : (+q.get('h') || 769);
  const url = pathToFileURL(path.resolve(__dirname, file)).href + (query ? '?' + query : '');
  const browser = await chromium.launch();
  const p = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  await p.goto(url);
  await p.waitForSelector('body[data-ready="1"]', { timeout: 15000 });
  await p.waitForTimeout(300);
  await p.screenshot({ path: out });
  await browser.close();
  console.log('saved', out, w + 'x' + h);
})();
