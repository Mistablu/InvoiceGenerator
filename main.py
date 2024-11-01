import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_no,date = filename.split("-")

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice no.{invoice_no}",ln=1)
    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Date: {date}",ln=1)

    df = pd.read_excel(filepath,sheet_name = "Sheet 1")
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]

    pdf.set_font(family="Times",size=10,style="B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=8,txt=columns[0],border=1)
    pdf.cell(w=70,h=8,txt=columns[1],border=1)
    pdf.cell(w=32,h=8,txt=columns[2],border=1)
    pdf.cell(w=29,h=8,txt=columns[3],border=1)
    pdf.cell(w=29,h=8,txt=columns[4],border=1,ln=1)

    for index,row in df.iterrows():
        pdf.set_font(family="Times",size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=8,txt=str(row["product_id"]),border=1)
        pdf.cell(w=70,h=8,txt=str(row["product_name"]),border=1)
        pdf.cell(w=32,h=8,txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=29,h=8,txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=29,h=8,txt=str(row["total_price"]),border=1,ln=1)
    
    total_price = str(df["total_price"].sum())

    pdf.set_font(family="Times",size=10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30,h=8, border=1)
    pdf.cell(w=70,h=8, border=1)
    pdf.cell(w=32,h=8, border=1)
    pdf.cell(w=29,h=8, border=1)
    pdf.cell(w=29,h=8, txt=total_price, border=1, ln=1)

    pdf.set_text_color(0,0,0)
    pdf.set_font(family="Times",size=12,style = "B")
    pdf.cell(w=30,h=8,txt=f"The total price is: {total_price}", ln=1)

    pdf.set_font(family="Times",size=15, style = "B")
    pdf.cell(w=40,h=8,txt=f"Made in Python")
    pdf.image("pythonhow.png",w=10)

    pdf.output(f"PDFs/{filename}.pdf")