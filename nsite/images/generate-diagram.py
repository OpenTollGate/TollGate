# generate_diagram.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64
import os

# Diagram text
DIAGRAM_TEXT = '''title New Client Check

Wifi Client-> Router: portal check (e.g. http://connectivitycheck.gstatic.com/generate_204)
Router-> OpenNDS: MAC address check
OpenNDS -> FAIServer (on router): passes e-cash token
FAIServer (on router)-> Minibits mint: Melt e-cash to minibits LNURL
Minibits mint -> FAIServer (on router): ACK / NACK
FAIServer (on router)-> OpenNDS: something...?
OpenNDS -> Router: Adjust IP tables  for MAC address
OpenNDS -> Wifi Client: Authenticated, can use the internet for ... minutes'''

def generate_diagram():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Create images directory if it doesn't exist
        os.makedirs('images', exist_ok=True)

        # Navigate to SequenceDiagram.org
        driver.get('https://sequencediagram.org')
        
        # Wait for the page to load and find the source text area
        time.sleep(2)  # Give the page time to fully load
        
        # Execute JavaScript to set the diagram text
        js_code = f'window.SEQ.store.dispatch({{ type: "SET_SOURCE_TEXT", text: `{DIAGRAM_TEXT}` }});'
        driver.execute_script(js_code)
        
        # Wait for the diagram to render
        time.sleep(2)
        
        # Generate  SVG
        svg_data = driver.execute_script('return window.SEQ.api.generateSvgDataUrl(window.SEQ.store.getState().sourceText);')
        
        # Save SVG file
        svg_base64_data = svg_data.split(',')[1]
        svg_data = base64.b64decode(svg_base64_data)
        with open('images/system-flow-diagram.svg', 'wb') as f:
            f.write(svg_data)
        
        # Take screenshot of the canvas for PNG version
        canvas = driver.find_element(By.ID, 'diagramCanvas')
        canvas.screenshot('images/system-flow-diagram.png')
        
        print("Diagram generated successfully!")
        
    finally:
        driver.quit()

if __name__ == '__main__':
    generate_diagram()
