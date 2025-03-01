import eel

# Initialize the 'www' directory (where your HTML, JS, CSS files are)
eel.init('www')

# Start the Eel server and open the browser
try:
    eel.start('index.html', mode='chrome', host='localhost', port=8000)
except Exception as e:
    print(f"Error starting Eel server: {e}")
