#-*- codeing = utf-8 -*-
#@Author: Angious
#@Time : 2020/5/4 10:55
#@File : GET_PDF.py
#@Software : PyCharm

from fpdf import FPDF
from PIL import Image
import os

def makePdf(pdfFileName, listPages):

	cover = Image.open(listPages[0])
	width, height = cover.size

	pdf = FPDF(unit = "pt", format = [width, height])

	for page in listPages:
		pdf.add_page()
		pdf.image(page, 0, 0)

	pdf.output(pdfFileName, "F")

makePdf("result.pdf", [imgFileName for imgFileName in os.listdir('.') \
					   if imgFileName.endswith("png")])


















