from fpdf import FPDF
import pandas

df = pandas.read_csv('topics.csv')
pdf = FPDF(orientation="P", unit='mm', format="A4")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.line(x1=10,y1=20,x2=200,y2=20)

pdf.output("output.pdf")