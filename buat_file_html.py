# List of tourist attractions
wisata_list = [
    "Bukit Lawang",
    "Sipisopiso",
    "Istana Maimun",
    "Salib Kasih",
    "Pantai Cermin",
    "Tangkahan",
    "Masjid Raya Medan",
    "Gunung Lauser",
    "Sipoholon",
    "Kawah Putih Tinggi Raja",
]

# Template for the HTML content
html_template = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
  
    <link rel="icon" href="favicon.ico" type="image/x-icon">
  
    <meta name="description" content="{description}">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin-left: 25px;
            margin-right: 25px;
            padding: 0;
            color: #333;
            background-color: #f4f4f4;
        }}
        header {{
            background-color: #0066cc;
            color: white;
            padding: 12px;
            text-align: center;
        }}
        .container {{
            display: flex;
            width: 100%;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-radius: 8px;
        }}
        .left, .center, .right {{
            padding: 15px;
        }}
        .left {{
            flex: 1;
            max-width: 20%;
        }}
        .center {{
            flex: 2;
            max-width: 60%;
        }}
        .right {{
            flex: 2;
            max-width: 13%;
            background-color: #f4f4f4;
            margin-left: 50px;
            padding-left: 10px; 
        }}
        .left img {{
            width: 100%;
            height: auto;
            border-radius: 8px;
        }}
        .center h1 {{
            margin-top: 0;
        }}
        .info h2 {{
            background-color: #0066cc;
            color: white;
            padding: 10px;
            border-radius: 8px;
            margin: 0;
        }}
        .info p {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
        }}
        .gallery img {{
            width: 100%;
            max-width: 300px;
            margin: 10px;
            border-radius: 8px;
        }}
        nav {{
            padding: 10px; 
            background-color: #f4f4f4;
            border-top: 1px solid #ddd;
        }}
        nav ul {{
            list-style-type: none;
            padding: 0;
        }}
        nav ul li {{
            margin: 5px 0;
        }}
        nav ul li a {{
            text-decoration: none;
            color: #333;
            display: block;
            padding: 10px;
            background-color: #e0e0e0;
            border-radius: 4px;
        }}
    
        .home-link {{
            display: block;
            text-align: center;
            margin: px 0;
            font-weight: bold;
            color: #e0e0e0;
            height: 30px;
            text-decoration: none;
            background-color: #0066cc;
        }}
    </style>
</head>
<body>
    <header>
        <h1>{title}</h1>
    </header>
   
    <div class="container">
        <div class="left">
            <img src="/gambar/{image_name}" alt="{title}">
        </div>
        <div class="center">
            <p style="font-size: 20px;">{description}</p>
            <div class="gallery">
                <h3>Galeri</h3>
                <img src="/gambar/{image_name2}" alt="Gambar 1" style="width:100%; max-width:300px;">
                <img src="/gambar/{image_name3}" alt="Gambar 2" style="width:100%; max-width:300px;">
                <img src="/gambar/{image_name4}" alt="Gambar 3" style="width:100%; max-width:300px;">
            </div>
        </div>
        <div class="right">
            <nav>
                <a href="Home.html" class="home-link">Home</a>
                <h3>Daftar Wisata</h3>
                <ul>
                    <li><a href="bukitlawang.html">Bukit Lawang</a></li>
                    <li><a href="pulausamosir.html">Pulau Samosir</a></li>
                    <li><a href="sipisopiso.html">Air Terjun Sipisopiso</a></li>
                    <li><a href="istanamaimun.html">Istana Maimun</a></li>
                    <li><a href="salibkasih.html">Salib Kasih</a></li>
                    <li><a href="pantaicermin.html">Pantai Cermin</a></li>
                    <li><a href="tangkahan.html">Tangkahan</a></li>
                    <li><a href="gununglauser.html">Gunung Lauser</a></li>
                    <li><a href="sipoholon.html">Kawah Sipoholon</a></li>
                    <li><a href="kawahputihtinggiraja.html">Kawah Putih Tinggi Raja</a></li>
                </ul>
            </nav>
        </div>
    </div>
</body>
</html>
"""

# Create HTML file for each tourist attraction
for wisata in wisata_list:
    # Replace spaces with underscores for the file name
    file_name = wisata.lower().replace(" ", "") + ".html"
    # Create a description for each attraction (can be customized)
    description = f"{wisata} adalah salah satu tempat wisata terkenal di Sumatera Utara."
    # Example image name for demonstration (customize this if you have specific image names)
    image_name = wisata.lower().replace(" ", "") + "1.jpeg"
    image_name2 = wisata.lower().replace(" ", "") + "2.jpeg"
    image_name3 = wisata.lower().replace(" ", "") + "3.jpeg"
    image_name4 = wisata.lower().replace(" ", "") + "4.jpeg"
    
    # Fill the template with actual content
    html_content = html_template.format(
        title=wisata,
        description=description,
        image_name=image_name,
        image_name2=image_name2,
        image_name3=image_name3,
        image_name4=image_name4
    )
    
    # Write the content to an HTML file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

print("File HTML telah berhasil dibuat untuk setiap objek wisata.")
