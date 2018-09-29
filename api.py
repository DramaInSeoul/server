
from flask_restful import Api, Resource
from flask_restful import reqparse
from flask import Flask, request, Response
import flask
import PIL
from PIL import Image
import binascii
from PIL import ImageDraw
from PIL import ImageFont
import jsonpickle
import numpy as np
import cv2
import subprocess
import io
import image
from array import array
app = Flask(__name__)
api = Api(app)


class Image(Resource):
    def post(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('name')
        # parser.add_argument('no')
        # args = parser.parse_args()
        # print(args['name'])
        # print(args['no'])
        # name = args['name']
        # no = args['no']
        # image = Image.open(io.BytesIO(r))
        # image.save("lena.jpg")
        # img = flask.request.files.get("")
        # print(imagefile)
        # convert string of image data to uint8
        r = request
        name = request.headers['name']
        no = request.headers['no']
        print(type(name))
        print(no)
        print(r.data)
        print(r.url)
        # bin_data = binascii.unhexlify(r)
        # print(bin_data)
        # convert string of image data to uint8
        nparr = np.fromstring(r.data, np.uint8)
        print(nparr)
        # # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        #
        # # do some fancy processing here....
        cv2.imwrite('lena.png', img)
        #
        # # build a response dict to send back to client
        response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                    }
        # encode response using jsonpickle
        response_pickled = jsonpickle.encode(response)

        # return Response(response=response_pickled, status=200, mimetype="application/json")
        p = subprocess.Popen(["python3" , 'inference.py', "lena.png"], stdout=subprocess.PIPE)
        print(p.communicate())
        if(name=="1"):
            p = subprocess.Popen(["python3", 'compare.py', "goblin_0"+str(no)+".png","lena.png"], stdout=subprocess.PIPE)
            out=p.communicate()[0].decode('utf-8')

            print(out[:-1])
            p = subprocess.Popen(["python3", 'posecompare.py',"goblin_0"+str(no)], stdout=subprocess.PIPE)

            out2 = p.communicate()[0].decode('utf-8')
            f = open("result.txt", "r")
            res = f.readline()
            # build a response dict to send back to client
            return {"back": out[:-1], "pose": res}
        elif (name == "2"):
            p = subprocess.Popen(["python3", 'compare.py', "myway_0" + str(no) + ".png", "lena.png"],stdout=subprocess.PIPE)
            out = p.communicate()[0].decode('utf-8')

            print(out[:-1])
            p = subprocess.Popen(["python3", 'posecompare.py',"myway_0" + str(no)], stdout=subprocess.PIPE)

            out2 = p.communicate()[0].decode('utf-8')
            f=open("result.txt","r")
            res=f.readline()
            # build a response dict to send back to client
            return {"back": out[:-1],"pose":res}

# api 라우팅 부분
api.add_resource(Image, '/image')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8000)
