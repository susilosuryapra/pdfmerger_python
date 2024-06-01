import PyPDF2
import os

merger = PyPDF2.PdfMerger()

# menyimpan List file PDF dan mengurutkannya
pdf_files = sorted([file for file in os.listdir(os.curdir) if file.endswith('.pdf')])

# menggabungkan file PDF sesuai urutan
for file in pdf_files:
    merger.append(file)

# membuat hasil gabungan ke file output
merger.write('combinedPDF.pdf')
merger.close()