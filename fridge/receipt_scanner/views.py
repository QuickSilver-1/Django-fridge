from django.shortcuts import render

# Create your views here.
import qr_parser
import requests
from bs4 import BeautifulSoup
import json

"""
filename = 'qr_parser/test_files/photo_2023-02-06_19-03-40.jpg'
image = cv2.imread(filename)

qr = qr_parser.decode(image)
print(qr)

result = qr_parser.parse_data(qr)
print(result)
"""
def my_view_1(request):

    return render(request, 'qr_scanner.html')

def my_view(request):
    
    # View code here...
    """
    return render(request, 'receipt_scanner.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')
    """
    """
    filename = 'qr_parser/test_files/photo_2023-02-04_20-48-48.jpg'
    image = cv2.imread(filename)
    
    qr = qr_parser.decode(image)[0]
    """
    fn = request.GET.get("fn")
    i = request.GET.get("i")
    fp = request.GET.get("fp")

    result = qr_parser.parse_data_1(fn, i, fp)
    soup = BeautifulSoup(result, "html.parser")
    json_result = requests.get(soup.find("a", "msohide")["href"], headers={'Content-type': 'application/json'})
    json_result = json.loads(json_result.text)
    print(json_result)
    #for item in result:


    return render(request, 'receipt_scanner.html', {
        'foo': result, 
        'json': json_result,
    })
