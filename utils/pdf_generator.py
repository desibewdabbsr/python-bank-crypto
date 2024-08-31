from fpdf import FPDF

def generate_pdf(transactions, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for transaction in transactions:
        pdf.cell(200, 10, txt=str(transaction), ln=True)
    
    pdf.output(filename)
