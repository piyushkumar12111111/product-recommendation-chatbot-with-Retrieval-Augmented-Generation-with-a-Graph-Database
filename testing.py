from bs4 import BeautifulSoup
import re

# Load your HTML data (for demonstration, a string is used here)
html_data = """
<!DOCTYPE html>
<html lang="en">
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# website: http://ogp.me/ns/website#">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="format-detection" content="telephone=no">
    <title>Fukuoka University Hospital</title>
    <meta name="description" content="Fukuoka University Hospital provides current patient-centered medicine based on the hospital policy of “warm-hearted” medical care, serving as the central leader for medical centers in and around western Fukuoka City.">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Fukuoka University Hospital">
    <meta property="og:site_name" content="Fukuoka University Hospital">
    <meta property="og:description" content="Fukuoka University Hospital provides current patient-centered medicine based on the hospital policy of “warm-hearted” medical care, serving as the central leader for medical centers in and around western Fukuoka City.">
    <meta property="og:url" content="https://www.hop.fukuoka-u.ac.jp/eng/">
    <meta property="og:image" content="https://www.hop.fukuoka-u.ac.jp/img/ogp.jpg">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
    <link href="https://fonts.googleapis.com/css?family=Cantarell|Crimson+Text|Montserrat:700|Noto+Serif&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/style_en.css">
    <link rel="stylesheet" href="/css/style_hp.css">
    <link rel="stylesheet" href="/css/colorbox.css">
    <link rel="stylesheet" href="/css/slick-theme.css"><!-- トップのみ -->
    <link rel="stylesheet" href="/css/slick.css"><!-- トップのみ -->
    <script src="/js/ofi.min.js"></script>
    <script src="/js/jquery.min.js"></script>
    <script src="/js/js.cookie-2.2.1.min.js"></script>
    <script src="/js/jquery.colorbox-min.js"></script>
    <script src="/js/libs.js"></script>
    <script src="/js/script.js" async></script>
    <script src="/js/slick.min.js"></script>
    <!-- カスタム検索コード -->
    <script async src="https://cse.google.com/cse.js?cx=007379604223716601508:eaimex4l4uf"></script>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-36084579-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-36084579-1');
    </script>
</head>
<body>
    <!-- Your body content here -->
</body>
</html>
"""

# Parse the HTML data
soup = BeautifulSoup(html_data, 'html.parser')

# Extract the title
title = soup.title.string if soup.title else 'No title found'

# Extract meta description
description = ''
meta_description = soup.find('meta', attrs={'name': 'description'})
if meta_description:
    description = meta_description.get('content', '')

# Extract all meta tags content
meta_contents = {}
for meta in soup.find_all('meta'):
    name = meta.get('name') or meta.get('property')
    if name:
        meta_contents[name] = meta.get('content', '')

# Extract all text within the body tag (if body exists)
body_text = ''
if soup.body:
    body_text = soup.body.get_text(separator=' ', strip=True)

# Further cleaning if necessary using regex
clean_body_text = re.sub(r'\s+', ' ', body_text)  # Normalize whitespace

# Create a dictionary with the extracted data
extracted_data = {
    'title': title,
    'description': description,
    'meta_contents': meta_contents,
    'body_text': clean_body_text
}

# Print the dictionary to check the result
print(extracted_data)

# Optionally, convert dictionary to a more readable format if needed
import json
pretty_data = json.dumps(extracted_data, indent=4)
print(pretty_data)
