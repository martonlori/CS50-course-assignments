from fpdf import FPDF, XPos, YPos


def main():

    name = input("Name: ")
    pdf = FPDF(orientation='Portrait', format='A4')
    pdf.add_page()
    pdf.set_font('Helvetica', size=40)
    pdf.cell(text="CS50 Shirtificate", center=True)
    pdf.image('shirtificate.png', x=0, y= 40, keep_aspect_ratio=True)
    pdf.set_font('Helvetica', size=30)
    pdf.set_text_color(255,255,255)
    pdf.cell(text=f"{name} took CS50!", h=180, center=True)
    pdf.output("shirtificate.pdf")

main()
