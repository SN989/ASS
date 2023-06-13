from tkinter import *
from PIL import ImageTk, Image

def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Animals
            Animals.main()
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Quiz_Time
            Quiz_Time.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()
        elif args == 8:
            from Options import Sentence
            Sentence.main()
        elif args == 9:
            from Options import Artical
            Artical.main()

    def option():

        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#e6fff6',
            border=0,
            justify='center',
        )
        sel_btn1 = Button(
            text="Animals",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Body parts",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Colour",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Fruits",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Quiz_Time",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Vegetable",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        sel_btn7 = Button(
            text="Vehicles",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        
        sel_btn8 = Button(
            text="Sentence",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(8),
        )
        sel_btn9 = Button(
            text="Artical",
            width=18,
            borderwidth=4,
            font=("Poppins", 18),
            fg="#000000",
            bg="#d99b8b",
            cursor="hand2",
            command=lambda: start_game(9),
        )
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )
        sel_btn8.grid(row=7, column=4, pady=(10, 0), padx=50, )
        sel_btn9.grid(row=8, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x550+500+150")
    main_window.resizable(0, 0)
    main_window.title("Zambo word game")
    main_window.configure(background="lightblue")

    img0 = ImageTk.PhotoImage(Image.open("logo1.jpg"))
    img1 = ImageTk.PhotoImage(Image.open("back.png"))

    lab_img = Label(
        main_window,
        image=img0,
        border=3,
        bg='#e6fff5',
    )
    lab_img.pack(pady=(60, 0))

    start_btn = Button(
        main_window,
        text="Start Game",
        width=18,
        borderwidth=4,
        fg="#000000",
        bg="#d99b8b",
        font=("Poppins", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(80, 20))

    main_window.mainloop()


start_main_page()
