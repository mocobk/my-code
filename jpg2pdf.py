import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas


def pic_to_pdf(pic_dir,pdf_file_name):
    file_name_list = []
    for each in os.listdir(pic_dir):
        if each.split(".")[-1] == "jpg" or each.split(".")[-1] == "png":
            file_name_list.append(each)
    print (file_name_list)
    # 当分辨率是72像素/英寸时，A4纸像素长宽分别是842×595px,landscape(A4)=(841.8897637795275, 595.275590551181)
    (height, width) = landscape(A4)
    c = canvas.Canvas(pdf_file_name, pagesize=(width, height))
    for each_pic in file_name_list:
        each_pic_path = pic_dir+"\\"+each_pic
        c.drawImage(each_pic_path, 0, 0, width, height)
        # c.drawImage(each_pic_path, 0, height)
        c.showPage()
    c.save()

 
pic_to_pdf(r"C:\Users\mozai\Desktop\jpg2pdf-master\jpg2pdf-master\test",r"test.pdf")