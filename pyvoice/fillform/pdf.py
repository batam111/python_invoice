import pdfkit
my = pdfkit.from_file('/home/mastro/nandan/invoice generator/invgen/fillform/templates/fillform/Invoice.html', 'out.pdf')

print(type(my))
