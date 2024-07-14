import streamlit as st
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if hasattr(self,'document_title'):
            self.set_font(family='Verdana',style='B',size=18)
            self.cell(w=0,h=10,txt=self.document_title,border=0,ln=1,align='C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font(family='Verdana',style='I',size=8)
        self.cell(w=0,h=10,txt=f'Page {self.page_no()}',border=0,ln=0,align='C')    
    
    def chapter_title(self,title,font='Verdana',size=14):
        self.set_font(font,style='B',size=size)
        self.cell(w=0,h=10,title=title,border=0,ln=0,align='L') 
        self.ln(10)
        
    def chapter_body(self,body,font='Verdana',size=10):
        self.set_font(font,style='',size=size)
        self.multi_cell(w=0,h=10,body=body) 
        self.ln(1)
        

def create_pdf(filename,document_title,author,chapters,image_path=None):
    pdf=PDF()
    pdf.document_title = document_title
    pdf.add_page()
    if author:
        pdf.set_author(author)
        
    if image_path:
        pdf.image(image_path,x=10,y=25,w=pdf.w-20)
        pdf.ln(120)
        
    for chapter in chapters:
        title,body,font,size=chapter
        pdf.chapter_title(title,font,size)
        pdf.chapter_body(body,font,size)
    
    pdf.output(filename)
    
def main():
    st.title("PDF Generator using Python")
    st.header("Doc Configuration")
    document_title = st.text_input("Document Title", "Document Title")
    author = st.text_input("Author",'')
    uploaded_image = st.file_uploader("upload an image fot the docuement (Optional)",
                                      type=['jpg','png'])
    
    
if __name__  == '__main__':
    main()