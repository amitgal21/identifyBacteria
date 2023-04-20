from tkinter import *

import globalsVar

global text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14


def put_text_on_screen(window):
    global text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14
    text1 = Label(
        window,
        anchor="nw",
        text="Welcome to BactiVision, a platform that leverages the power of artificial intelligence to identify "
             "bacterial species using images of Gram-stained cells.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text1.place(x=350, y=200)
    text2 = Label(
        window,
        anchor="nw",
        text="Our mission is to make bacterial identification more accurate, efficient, and accessible, by combining "
             "the latest AI technologies with the expertise",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text2.place(x=350, y=220)
    text3 = Label(
        window,
        anchor="nw",
        text="of microbiologists and software developers.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text3.place(x=350, y=240)
    text4 = Label(
        window,
        anchor="nw",
        text="At BactiVision, we believe that AI can revolutionize the field of microbiology, by enabling faster and "
             "more reliable identification of bacterial species,",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text4.place(x=350, y=280)
    text5 = Label(
        window,
        anchor="nw",
        text="even in complex or ambiguous cases. Our team is composed of experts in AI, microbiology, and software "
             "development, who are passionate about",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text5.place(x=350, y=300)
    text14 = Label(
        window,
        anchor="nw",
        text="pushing the boundaries of what is possible with AI in microbiology.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text14.place(x=350, y=320)
    text6 = Label(
        window,
        anchor="nw",
        text="Our platform allows you to upload an image of a Gram-stained cell, and our AI algorithm will "
             "automatically analyze it and provide you with the most",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text6.place(x=350, y=360)
    text7 = Label(
        window,
        anchor="nw",
        text="probable bacterial species based on its Gram staining characteristics. Our AI model is trained on a "
             "large dataset of Gram-stained images, and is",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text7.place(x=350, y=380)
    text8 = Label(
        window,
        anchor="nw",
        text="constantly improving through machine learning techniques.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text8.place(x=350, y=400)
    text9 = Label(
        window,
        anchor="nw",
        text="We understand that bacterial identification can be a daunting task, especially for those who are not "
             "trained inmicrobiology. That's why we have",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text9.place(x=350, y=440)
    text10 = Label(
        window,
        anchor="nw",
        text="designed our platform to be intuitive and user-friendly, with clear instructions and easy-to-understand "
             "results. Whether you are a microbiologist,",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text10.place(x=350, y=460)
    text11 = Label(
        window,
        anchor="nw",
        text="clinician, or researcher, our platform can help you save time and improve your accuracy in identifying "
             "bacterial species.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text11.place(x=350, y=480)
    text12 = Label(
        window,
        anchor="nw",
        text="Thank you for choosing BactiVision, and please don't hesitate to contact us if you have any questions "
             "or feedback.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text12.place(x=350, y=520)
    text13 = Label(
        window,
        anchor="nw",
        text="We are committed to making bacterial identification more accessible and reliable through the power of AI.",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 11 * -1),
        bg="#272A37"
    )
    text13.place(x=350, y=540)


def clear_screen():
    # destroy only the labels that you want to clear
    text1.destroy()
    text2.destroy()
    text3.destroy()
    text4.destroy()
    text5.destroy()
    text6.destroy()
    text7.destroy()
    text8.destroy()
    text9.destroy()
    text10.destroy()
    text11.destroy()
    text12.destroy()
    text13.destroy()
    text14.destroy()
