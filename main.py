from flask import Flask, request
import os
from flask import Flask, make_response
import imgkit
from PIL import Image
import io

app = Flask(__name__)

@app.route('/registration', methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        if 'photo' in request.files:
            img = request.files['photo']
            fname = request.form['fname']
            lname = request.form['lname']
            faculty = request.form['faculty']
            phone = request.form['phone']
            email = request.form['email']
            sex = request.form['gender']
            fav = request.form['fav']
#            img_path = (os.path.join(os.getcwd(), 'image.jpg'))
            img_path = '/home/YourPythonAnywhereUsername/mysite/image.jpg'
            img.save(img_path)
            os.system('cp /home/YourPythonAnywhereUsername/mysite/image.jpg /home/YourPythonAnywhereUsername/mysite/static/image.jpg')
            htmlpg = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration_Form</title>
    <link rel="icon" type="image/png" href="https://i.postimg.cc/156t3RHP/image.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@1,500&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,200&display=swap" rel="stylesheet">
    <style>
        body {
            background-color:white;
            -ms-overflow-style:none;
            scrollbar-width:none;
        }
        body::-webkit-scrollbar {
            display:none;
        }
        #header {
            height:max-content;
            width:100%;
        }
        #formD {
            background-color:rgba(255, 255, 255, 0.774);
            overflow-x:hidden;
        }
        #text2 {
            font-family:'Poppins',sans-serif;
            display:flex;
            justify-content:center;
            text-align:center;
        }
        table, th, td {
            border:2px solid;
            border-collapse:collapse;
            border-color:slategrey;
            padding:15px 12px 15px 20px;
            font-family:'Roboto Flex',sans-serif;
        }
        table tr:nth-child(even){background-color: #f2f2f2;}
        #footer {
            display:flex;
            text-align:center;
            justify-content:center;
            font-family:'Comfortaa',cursive;
        }
        #des1 {
            font-family:'Noto Sans Sinhala', sans-serif;
            padding-left:10px;
            padding-top:3px;
            padding-right:3px;
            display:block;
        }
        #text1 {
            text-align:center;
            font-size:90px;
            display:flex;
            justify-content:center;
            font-family:'Raleway',sans-serif;
            text-shadow:3px 3px 10px rgb(248, 182, 0);
        }
        .hr {
            height:1vh;
            width:100%;
            background-image: linear-gradient(90deg,red,orange,yellow,green,blue,indigo,purple,rgba(0, 0, 0, 0.774));
        }
        a:hover {
            font-weight:bolder;
            color:tomato;
        }
        #pto {
            height:200px;
            width:auto;
        }
        #t1 {
            display:flex;
            justify-content:center;
        }
        #signbar {
            display:flex;
            justify-content:right;
            text-align:center;
        }
    </style>
</head>
<body>
    <div id="formD">
        <div id="text2">University of Moratuwa - Application for library member registration.</div>
        <table id="t1">
            <tr>
                <td>Full name</td>
                <td>'''+str(fname)+" "+str(lname)+'''</td>
            </tr>
            <tr>
                <td>Faculty</td>
                <td>'''+str(faculty)+'''</td>
            </tr>
            <tr>
                <td>Phone number</td>
                <td>'''+str(phone)+'''</td>
            </tr>
            <tr>
                <td>Email address</td>
                <td>'''+str(email)+'''</td>
            </tr>
            <tr>
                <td>Gender</td>
                <td>'''+str(sex)+'''</td>
            </tr>
            <tr>
                <td>Favourite categories/genres/subjects</td>
                <td>'''+str(fav)+'''</td>
            </tr>
            <tr>
                <td>Applicant's photo</td>
                <td><img src="https://YourPythonAnywhereUsername.pythonanywhere.com/static/image.jpg" id="pto" alt="Internal error occured when entering your photo. Please use some glue and paste your Passprt sized photo behind the hard copy of this application, like a real human."></td>
            </tr>
        </table>
    </div><br><br><br>
    <div id="signbar">______________________<br>Applicant's signarute</div>
</body>
</html>'''
            f = open("/home/YourPythonAnywhereUsername/mysite/form.html", "w")
            f.write(str(htmlpg))
            f.close()
            del f
            msg = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration_Form</title>
    <link rel="icon" type="image/png" href="https://i.postimg.cc/156t3RHP/image.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@1,500&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,200&display=swap" rel="stylesheet">
    <style>
        body {
            background-color:white;
            -ms-overflow-style:none;
            scrollbar-width:none;
        }
        body::-webkit-scrollbar {
            display:none;
        }
        #header {
            height:max-content;
            width:100%;
        }
        #formD {
            background-color:rgba(255, 255, 255, 0.774);
            overflow-x:hidden;
        }
        #text2 {
            font-family:'Poppins',sans-serif;
        }
        table, th, td {
            border:2px solid;
            border-collapse:collapse;
            border-color:slategrey;
            padding:15px 12px 15px 20px;
            font-family:'Roboto Flex',sans-serif;
        }
        table tr:nth-child(even){background-color: #f2f2f2;}
        #footer {
            display:flex;
            text-align:center;
            justify-content:center;
            font-family:'Comfortaa',cursive;
        }
        #ff {
            font-family:'0Ubuntu Mono',monospace;
            padding:20px 0% 20px 0%;
            background-color: rgba(128, 128, 128, 0.151);
            color:rgba(185, 122, 4, 0.925);
            display:flex;
            justify-content:center;
        }
        #dB {
            padding: 10px 20px 10px 20px;
            width:max-content;
            background-color:rgba(41, 207, 0, 0.973);
            border-radius:5px;
            border-color:green;
            color:white;
            font-size:large;
        }
        #reB {
            padding: 10px 20px 10px 20px;
            width:max-content;
            background-color:rgba(0, 83, 207, 0.973);
            border-radius:5px;
            border-color:rgb(0, 0, 255);
            color:white;
            font-size:large;
        }
        #des1 {
            font-family:'Noto Sans Sinhala', sans-serif;
            padding-left:10px;
            padding-top:3px;
            padding-right:3px;
            display:block;
        }
        #text1 {
            text-align:center;
            font-size:90px;
            display:flex;
            justify-content:center;
            font-family:'Raleway',sans-serif;
            text-shadow:3px 3px 10px rgb(248, 182, 0);
        }
        .hr {
            height:1vh;
            width:100%;
            background-image: linear-gradient(90deg,red,orange,yellow,green,blue,indigo,purple,rgba(0, 0, 0, 0.774));
        }
        a:hover {
            font-weight:bolder;
            color:tomato;
        }
        #pto {
            height:200px;
            width:auto;
        }
        #t1 {
            display:flex;
            justify-content:center;
        }
    </style>
</head>
<body>
    <div id="header">
        <div id="text1">UOM - Library Registration</div><br>
        <div class="hr"></div><br>
        <div id="des1">🔴 මෙහි පහත දැක්වෙන පෝරමය ඔබ විසින් අප වෙත එවනු ලැබූ තොරතුරු මත පදනම් වී ඇත. එම පෝරමය හොඳින් නැවත පරික්ෂා කිරීමක් සිදුකොට;<br><ol><li>එහි නිවැරදි කිරීම් සිදු කිරිමට තිබේ නම් පහත දක්වා ඇති <a href="#reB">"Re-fill Form" බටනය</a> මත ක්ලික් කරන්න.</li><li>පෝරමය පිරවීමේදී ලබාදුන් තොරතුරු සියල්ල නිරවද්‍ය නම් පහත දක්වා ඇති <a href="#dB">"Download Application" බටනය</a> ක්ලික් කර ඉන්පසු බාගත කිරීමට ලැබෙන *.pdf ගොණුවේ දෘඪ පිටපතක් (a print-out) ලබාගෙන එය පුස්තකාල කාර්‍ය මණ්ඩලය වෙත ගෙනැවිත් බාරදෙන්න.</li></ol></div>
    </div>
    <div id="formD">
        <div id="text2">University of Moratuwa - Application for library member registration.</div>
        <table id="t1">
            <tr>
                <td>Full name</td>
                <td>'''+str(fname)+" "+str(lname)+'''</td>
            </tr>
            <tr>
                <td>Faculty</td>
                <td>'''+str(faculty)+'''</td>
            </tr>
            <tr>
                <td>Phone number</td>
                <td>'''+str(phone)+'''</td>
            </tr>
            <tr>
                <td>Email address</td>
                <td>'''+str(email)+'''</td>
            </tr>
            <tr>
                <td>Gender</td>
                <td>'''+str(sex)+'''</td>
            </tr>
            <tr>
                <td>Favourite categories/genres/subjects</td>
                <td>'''+str(fav)+'''</td>
            </tr>
            <tr>
                <td>Applicant's photo</td>
                <td><img src="https://YourPythonAnywhereUsername.pythonanywhere.com/static/image.jpg" id="pto" alt="Internal error occured when entering your photo. Please use some glue and paste your Passprt sized photo behind the hard copy of this application, like a real human."></td>
            </tr>
        </table>
    </div><br><br><br>
    <div id="footer">
        <button id="reB">↫ Re-fill Form</button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<button id="dB">⤓ Download Application</button>
    </div><br><br>
    <script>
        document.getElementById('dB').onclick = function() {
            window.open('https://YourPythonAnywhereUsername.pythonanywhere.com/download_application');
        };
        document.getElementById('reB').onclick = function() {
            location.href = 'https://uom-library-registration.pages.dev';
        }
    </script>
    <div id="ff">
        <p>© 2023-2025 • UOM - ICT Department</p>
    </div>
    <script data-name="BMC-Widget" data-cfasync="false" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="HimalErangana" data-description="Support me on Buy me a Book and Pay some Internet Bills!" data-message="Do you learned something from this demo page? If you learned something and you have an ability to donate some money, Help this demo page creator by donating some money for buy him some books...! ❤" data-color="#018f14" data-position="Right" data-x_margin="18" data-y_margin="18"></script>
</body>
</html>'''
        else:
            msg = "Something went wrong...!"

    return msg

"""
from flask import Flask, make_response
from flask import render_template
from weasyprint import HTML

@app.route('/download_application')
def pdf():
    html = render_template('form.html')
    pdf = HTML(string=html).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=Application.pdf'

    return response
"""


@app.route('/download_application')
def pdf():
    options = {
        'quality': 100
    }
    os.environ['XDG_RUNTIME_DIR'] = '/tmp/runtime-YourPythonAnywhereUsername'
    imgkit.from_file('/home/YourPythonAnywhereUsername/mysite/form.html', '/home/YourPythonAnywhereUsername/mysite/form.png', options=options)
    image = Image.open('/home/YourPythonAnywhereUsername/mysite/form.png')
    pdf = image.convert('RGB')

    # Save the PDF data to a BytesIO object
    pdf_data = io.BytesIO()
    pdf.save(pdf_data, format='PDF')

    # Create a response from the PDF data
    response = make_response(pdf_data.getvalue())

    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=Application.pdf'
    return response


if __name__ == "__main__":
    app.run(debug=True)
