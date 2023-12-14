from fpdf import FPDF



class f(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)




def shirt(i):
    a = f()
    a.add_page(orientation="portrait", format="a4")
    a.set_font("helvetica", size=24)
    a.set_text_color(255,255,255)
    a.cell(0, 213, f"{i} took CS50", align="C")
    a.output("shirtificate.pdf")



n = input("Name: ") # get inpute of user
shirt(n) # convert it