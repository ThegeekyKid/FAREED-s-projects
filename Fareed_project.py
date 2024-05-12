# STEP 1: IMPORT THE QR CODE
import qrcode

# STEP 2: GENERATE THE QR CODE
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L , box_size=20, border=4)

# STEP 3: ADD THE DATA YOU WISH INTO THE QR CODE
qr.add_data("https://x.com/M8zzala/status/1785198803936555449")
qr.make(fit=True)

# STEP 4: QR CODE BACKGROUND EDIT
img = qr.make_image(fill_color='black', back_color='white')

# STEP 4: SAVE THE IMAGE AS A FILE
img.save('fareed_project.png')