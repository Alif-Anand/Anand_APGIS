import folium
import pandas as pd

df = pd.read_csv(r"C:\Users\alif anand\Downloads\Tugas_Bali_APGIS\static\Data_Populasi_Bali.csv")

m = folium.Map(
    location=[-8.45,115.15],
    zoom_start=9
)

def warna(kategori):

    if kategori == "Sangat Tinggi":
        return "darkred"

    elif kategori == "Tinggi":
        return "red"

    elif kategori == "Sedang":
        return "orange"

    else:
        return "green"

for _, row in df.iterrows():

    popup = f"""
    <h4>{row['nama']}</h4>

    Populasi:
    {row['populasi']:,} Jiwa

    <br><br>

    Kategori:
    {row['kategori']}
    """

    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=popup,
        tooltip=row["nama"],
        icon=folium.Icon(
            color=warna(row["kategori"])
        )
    ).add_to(m)

legend_html = '''
<div style="
position: fixed;
bottom: 30px;
right: 30px;
width: 220px;
background-color: white;
border-radius: 10px;
padding: 15px;
box-shadow: 0 0 15px rgba(0,0,0,0.2);
z-index:9999;
font-size:14px;
">

<h4 style="margin-top:0;">
Kategori Populasi
</h4>

<p>🟤 > 700.000</p>
<p>🔴 500.000 - 700.000</p>
<p>🟠 300.000 - 500.000</p>
<p>🟢 < 300.000</p>

</div>
'''

m.get_root().html.add_child(folium.Element(legend_html))
m.save("webgis_populasi_bali.html")