# jetson-nano-drone-surveillance
Using the ssd-mobilenet-v1 and the DJI Tello Drone on the Nvidia Jetson Nano for surveillance flights

After First Boot is completed we have to Build all necessary dependencies from source. To get them we use dusty-nv description. 

You will find the full tutorial here :

[https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

The short overview of commands without explanation

```
$ sudo apt-get update
$ sudo apt-get install git cmake libpython3-dev python3-numpy
$ git clone --recursive https://github.com/dusty-nv/jetson-inference
$ cd jetson-inference
$ mkdir build
$ cd build
$ cmake ../
$ make -j$(nproc)
$ sudo make install
$ sudo ldconfig
```

After completion we can rather get some librarys 

$ pip3 install djitellopy

This Library is developed by Damian Fuentes and will be the link between our Dji Tello Drone and our Nvidia Jetson Nano.

[https://github.com/damiafuentes](https://github.com/damiafuentes)

We connect the Tello via wlan with the Jetson Nano.

In this example we use the ssd-mobilenet-v1 model 

You Need to Download this model.

To get this model you have to:

```
$ cd jetson-inference/tools
$ ./download-models.sh
```

Now opens a drop menu where you can choose between the different models.

Select ssd-mobilenet-v1 and install 

This example tello_detections Show Basic surveillance by taking off, turning around and showing live stream with ssd-mobilenet-v1 model in separate Window via opencv 

works also pretty well with the "FaceNet-120" model

After First Boot is completed we have to Build all necessary dependencies from source. To get them we use dusty-nv description. 

You will find the full tutorial here :

[https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md)

The short overview of commands without explanation

```
$ sudo apt-get update
$ sudo apt-get install git cmake libpython3-dev python3-numpy
$ git clone --recursive https://github.com/dusty-nv/jetson-inference
$ cd jetson-inference
$ mkdir build
$ cd build
$ cmake ../
$ make -j$(nproc)
$ sudo make install
$ sudo ldconfig
```

After completion we can rather get some librarys 

$ pip3 install djitellopy

This Library is developed by Damian Fuentes and will be the link between our Dji Tello Drone and our Nvidia Jetson Nano.

[https://github.com/damiafuentes](https://github.com/damiafuentes)

We connect the Tello via wlan with the Jetson Nano.

In this example we use the ssd-mobilenet-v1 model 

You Need to Download this model.

To get this model you have to:

```
$ cd jetson-inference/tools
$ ./download-models.sh
```

Now opens a drop menu where you can choose between the different models.

Select ssd-mobilenet-v1 and install 

This example tello_detections Show Basic surveillance by taking off, turning around and showing live stream with ssd-mobilenet-v1 model in separate Window via opencv 

works also pretty well with the "FaceNet-120" model


Just a little explanation about part of the code:

img = frame_read.frame
	img = cv2.resize(img, (480, 360)) #360,240
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA).astype(np.float32)
	img = jetson.utils.cudaFromNumpy(img)
	detections = net.Detect(img)
	img = jetson.utils.cudaToNumpy(img)
	img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB).astype(np.uint8)
	img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
	cv2.imshow("drone", img)
  
we need to resize the frame of the drone camera output just to safe some space.
and we need to change the datatype of the videoinput so the detection will work.
but its pretty easy because jetson utils cuda does this.
