import puppeteer from "puppeteer-extra";
import StealthPlugin from "puppeteer-extra-plugin-stealth";

puppeteer.use(StealthPlugin());
(async () => {
    const browser = await puppeteer.launch({
        headless: false,
        args: ["--disable-notifications", "--mute-audio", "--enable-automation"],
        ignoreDefaultArgs: true
    });

    // going to sign-in page
    const page = await browser.newPage();
    const navigationPromise = page.waitForNavigation();
    await page.goto("https://accounts.google.com/");

    const context = browser.defaultBrowserContext();
    await context.overridePermissions(
        "https://meet.google.com/", ["microphone", "camera", "notifications"]
    );

    await navigationPromise;

    // typing out email
    await page.waitForSelector('input[type="email"]');
    await page.click('input[type="email"]');
    await navigationPromise;
    await page.keyboard.type(`xxxxx`);  // replace XXXXX with your original email, before the @gmail.com
    await page.waitForTimeout(2000);

    await page.waitForSelector("#identifierNext");
    await page.click("#identifierNext");

    // typing out password
    await page.waitForTimeout(3500);
    await page.keyboard.type(`yyyy`);  // replace YYYYY with your original password
    await page.waitForTimeout(800);
    await page.keyboard.press('Enter');
    await navigationPromise;

    // going to Meet after signing in
    await page.waitForTimeout(2500);
    await page.goto("https://meet.google.com/");
    await page.waitForSelector('input[type="text"]');
    await page.click('input[type="text"]');
    await page.waitForTimeout(1000);
    await page.keyboard.type(`apk-dmrp-ekg`);  // replace aaa-bbbb-ccc with the required Google Meet Code
    await page.waitForTimeout(800);
    await page.keyboard.press('Enter');
    await navigationPromise;

    // turn off cam using Ctrl+E
    await page.waitForTimeout(8000);
    await page.keyboard.down('ControlLeft');
    await page.keyboard.press('KeyE');
    await page.keyboard.up('ControlLeft');
    await page.waitForTimeout(2000);

    //turn off mic using Ctrl+D
    await page.waitForTimeout(1000);
    await page.keyboard.down('ControlLeft');
    await page.keyboard.press('KeyD');
    await page.keyboard.up('ControlLeft');
    await page.waitForTimeout(2000);

    // Join Now

    await page.waitForSelector('.NPEfkd');
    await page.click('.NPEfkd');



    await page.waitForSelector('.HKarue .DPvwYc .Hdh4hc');
    await page.focus('.HKarue .DPvwYc .Hdh4hc');
    await page.click('.HKarue .DPvwYc .Hdh4hc');


    await page.waitForSelector('.KHxj8b');
    await page.click('.KHxj8b ');


    await page.keyboard.type('Hello i am bot :)', { delay: 100 })

    await page.waitForSelector('.ZjFb7c');

    var linkTexts = await page.$$eval(".ZjFb7c", elements => elements.map(item => item.textContent))
    // prints a array of text
    await console.log(linkTexts)






})();