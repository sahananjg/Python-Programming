import os
import zipfile

# Project folder structure
project_name = "ecommerce_site_basic"
folders = [
    f"{project_name}/css",
    f"{project_name}/js",
    f"{project_name}/images",
    f"{project_name}/includes",
    f"{project_name}/pages"
]

# Sample files content
files_content = {
    f"{project_name}/index.php": """<?php include('includes/header.php'); ?>
<h1>Welcome to My E-Commerce Site</h1>
<p>Browse products and shop online.</p>
<?php include('includes/footer.php'); ?>""",

    f"{project_name}/includes/header.php": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Site</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
<header>
    <h2>My E-Commerce Site</h2>
    <nav>
        <a href="../index.php">Home</a> |
        <a href="../pages/products.php">Products</a> |
        <a href="../pages/cart.php">Cart</a> |
        <a href="../pages/contact.php">Contact</a>
    </nav>
</header>
<main>""",

    f"{project_name}/includes/footer.php": """</main>
<footer>
    <p>&copy; 2025 My E-Commerce Site</p>
</footer>
<script src="../js/script.js"></script>
</body>
</html>""",

    f"{project_name}/css/style.css": """body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
header { background: #333; color: #fff; padding: 10px; }
header nav a { color: #fff; margin: 0 10px; text-decoration: none; }
h1 { color: #333; }
footer { background: #f1f1f1; text-align: center; padding: 10px; }""",

    f"{project_name}/js/script.js": """console.log("E-commerce site loaded.");""",

    f"{project_name}/pages/products.php": """<?php include('../includes/header.php'); ?>
<h1>Products</h1>
<ul>
    <li>Product 1 - $10</li>
    <li>Product 2 - $20</li>
    <li>Product 3 - $30</li>
</ul>
<?php include('../includes/footer.php'); ?>""",

    f"{project_name}/pages/cart.php": """<?php include('../includes/header.php'); ?>
<h1>Your Cart</h1>
<p>No items in your cart.</p>
<?php include('../includes/footer.php'); ?>""",

    f"{project_name}/pages/contact.php": """<?php include('../includes/header.php'); ?>
<h1>Contact Us</h1>
<form>
    <label>Name:</label><br>
    <input type="text" name="name"><br>
    <label>Email:</label><br>
    <input type="email" name="email"><br>
    <label>Message:</label><br>
    <textarea name="message"></textarea><br>
    <button type="submit">Send</button>
</form>
<?php include('../includes/footer.php'); ?>"""
}

# Create folder structure and files
for folder in folders:
    os.makedirs(folder, exist_ok=True)

for filepath, content in files_content.items():
    with open(filepath, "w") as f:
        f.write(content)

# Create zip file
zip_filename = f"{project_name}.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for root, dirs, files in os.walk(project_name):
        for file in files:
            filepath = os.path.join(root, file)
            zipf.write(filepath, arcname=os.path.relpath(filepath, project_name))

zip_filename
