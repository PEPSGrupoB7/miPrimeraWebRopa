const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox']});
  const page = await browser.newPage();

  await page.goto('http://localhost:3000');

  const title = await page.title();
  console.log("Título:", title);

  await browser.close();
})();
