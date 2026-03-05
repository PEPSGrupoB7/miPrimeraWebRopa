const puppeteer = require('puppeteer');

describe('Pruebas E2E de mi web', () => {
  test('Página principal carga y título correcto', async () => {
    const browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.goto('http://localhost:9081');

    const title = await page.title();
    expect(title).toBe('Mi Primera Web Ropa');

    await browser.close();
  });
});
