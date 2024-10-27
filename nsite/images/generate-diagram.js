// generate-diagram.js
const puppeteer = require('puppeteer');
const fs = require('fs');

const DIAGRAM_TEXT = `title New Client Check

Wifi Client-> Router: portal check (e.g. http://connectivitycheck.gstatic.com/generate_204)
Router-> OpenNDS: MAC address check
OpenNDS -> FAIServer (on router): passes e-cash token
FAIServer (on router)-> Minibits mint: Melt e-cash to minibits LN URL
Minibits mint -> FAIServer (on router): ACK / NACK
FAIServer (on router)-> OpenNDS: something...?
OpenNDS -> Router: Adjust IP tables for MAC address
OpenNDS -> Wifi Client: Authenticated, can use the internet for ... minutes`;

async function generateDiagram() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Navigate to SequenceDiagram.org
    await page.goto('https://sequencediagram.org');
    
    // Input the diagram text
    await page.evaluate((text) => {
        window.SEQ.store.dispatch({ type: 'SET_SOURCE_TEXT', text });
    }, DIAGRAM_TEXT);
    
    // Wait for diagram to render
    await page.waitForTimeout(2000);
    
    // Get the diagram canvas
    const canvas = await page.$('#diagramCanvas ');
    
    // Take screenshot of the canvas
    await canvas.screenshot({
        path: 'nsite/images/system-flow-diagram.png'
    });
    
    // Export as SVG
    const svgData = await page.evaluate(() => {
        return window.SEQ.api.generateSvgDataUrl(window.SEQ.store.getState().sourceText);
    });
    
    // Save SVG file
    const svgBase64Data = svgData.replace(/^data:image\/svg\+xml;base64,/, '');
    fs.writeFileSync('nsite/images/system-flow-diagram.svg', Buffer.from(svgBase64Data, 'base64'));
    
    await browser.close();
    console.log('Diagram generated successfully!');
}

generateDiagram().catch(console.error);
