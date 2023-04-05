import tkinter as tk
import requests
import webbrowser

def check_proxy():
    # Get the HTTP and HTTPS proxy server values from the entry fields
    http_proxy = http_proxy_entry.get()
    https_proxy = https_proxy_entry.get()
    
    # Make a request to the "showmyip.com" website through the HTTP proxy server
    proxy = {
        'http': http_proxy,
        'https': https_proxy
    }
    url = 'https://www.showmyip.com/'
    try:
        response = requests.get(url, proxies=proxy, timeout=10)
        if response.ok:
            response_text.insert(tk.END, f'Proxy is working. IP address: {response.text}\n')
            check_button.config(bg='green')
        else:
            response_text.insert(tk.END, 'Proxy is not working\n')
            check_button.config(bg='red')
    except requests.exceptions.RequestException as e:
        response_text.insert(tk.END, f'Error checking proxy: {e}\n')
        check_button.config(bg='red')
    
def make_request():
    # Get the URL and proxy server values from the entry fields
    url = url_entry.get()
    proxy = {
        'http': http_proxy_entry.get(),
        'https': https_proxy_entry.get()
    }
    
    # Make the request through the proxy server
    response = requests.get(url, proxies=proxy)
    
    # Open the response in a new window
    browser_window = tk.Toplevel(window)
    browser_window.title('Response Content')
    browser_text = tk.Text(browser_window, height=20, width=80)
    browser_text.insert(tk.END, response.content)
    browser_text.pack()
    
    # Update the response text box with the response content
    response_text.delete('1.0', tk.END)
    response_text.insert(tk.END, response.content)

def open_proxies():
    # Open the "https://hidemy.name/en/proxy-list/?type=s&anon=4#list" URL in the user's default web browser
    webbrowser.open_new_tab('https://hidemy.name/en/proxy-list/?type=s&anon=4#list')

# Create the GUI window
window = tk.Tk()
window.title('Proxy Requester')

# Create the entry fields for URL and proxy server
url_label = tk.Label(window, text='URL:')
url_label.grid(row=0, column=0)
url_entry = tk.Entry(window, width=50)
url_entry.grid(row=0, column=1)

http_proxy_label = tk.Label(window, text='HTTP Proxy:')
http_proxy_label.grid(row=1, column=0)
http_proxy_entry = tk.Entry(window, width=50)
http_proxy_entry.grid(row=1, column=1)

https_proxy_label = tk.Label(window, text='HTTPS Proxy:')
https_proxy_label.grid(row=2, column=0)
https_proxy_entry = tk.Entry(window, width=50)
https_proxy_entry.grid(row=2, column=1)

# Create the "Check Proxy" and "Send Request" buttons
check_button = tk.Button(window, text='Check Proxy', command=check_proxy)
check_button.grid(row=3, column=0)
send_button = tk.Button(window, text='Send Request', command=make_request)
send_button.grid(row=3, column=1)

# Create the "Proxies" button to open the "https://hidemy.name/en/proxy-list/?type=s&anon=4#list" URL
proxies_button = tk.Button(window, text='Proxies', command=open_proxies)
proxies_button.grid(row=3, column=2)

# Create the text box for displaying the response and checking the proxy
response_text = tk.Text(window, height=20, width=80)
response_text.grid(row=4, column=0, columnspan=3)

# Start the GUI event loop
window.mainloop()
