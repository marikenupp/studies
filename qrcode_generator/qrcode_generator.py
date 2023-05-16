import qrcode
def main():
    def generate_qrcode(text, filename):
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4
        )

        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        img.save(filename)



    def slicer(url):
        (usersite, end) = url.split(".")
        (end, extension) = end.split("com")
        print(usersite)
        print(end)
        print(extension)
        return usersite


    url = input("Enter your url: ")
    filename = url.replace("https://", "").replace(".com", "").replace("/", "_") + ".png"
    generate_qrcode(url,filename)

while True:
    main()
