import requests
import base64
from urllib.parse import urlencode

def render_webpage(url, api_key, javascript_enabled=True, premium_proxy=False):
    """
    Renders a webpage using ScrapingBee API and returns the HTML content.
    
    Args:
        url (str): The URL to render
        api_key (str): Your ScrapingBee API key
        javascript_enabled (bool): Whether to enable JavaScript rendering
        premium_proxy (bool): Whether to use premium proxies
    
    Returns:
        str: The rendered HTML content
        
    Raises:
        requests.exceptions.RequestException: If the API request fails
    """
    # ScrapingBee API endpoint
    api_url = 'https://app.scrapingbee.com/api/v1/'
    
    # Prepare the parameters
    params = {
        'url': url,
        'api_key': api_key,
        'render_js': javascript_enabled,
        'premium_proxy': premium_proxy
    }
    
    try:
        # Make the request to ScrapingBee
        response = requests.get(api_url, params=params)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Return the rendered content
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        raise

def save_rendered_page(html_content, output_file='rendered_page.html'):
    """
    Saves the rendered HTML content to a file.
    
    Args:
        html_content (str): The HTML content to save
        output_file (str): The filename to save to
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

# Example usage
if __name__ == "__main__":
    # Replace with your API key
    API_KEY = 'VVM1PR8XCIILEDFURUTTOPC6Y0YMUSYB8YQ485UR79Y9SX96X5FP0C3721L0VTK218PHR99EI7VKP5N7'
    
    # URL to render
    target_url = 'https://stiri.md'
    
    try:
        # Render the webpage
        rendered_html = render_webpage(
            url=target_url,
            api_key=API_KEY,
            javascript_enabled=True,
            premium_proxy=False
        )
        
        # Save the rendered content
        save_rendered_page(rendered_html)
        print(f"Successfully rendered and saved webpage content")
        
    except Exception as e:
        print(f"Failed to render webpage: {e}")