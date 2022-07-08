#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from config.config import *
import subprocess, cv2
import numpy as np

#######################POSITON DETECT############################
def detecPos(img,imgOriginal):
    img1=img.copy()
    img2=imgOriginal.copy()
    red=[0,0]
    green=[0,0]
    deteccion=0
    imagen_tratada=cv2.cvtColor(img1.copy(), cv2.COLOR_BGR2HSV)
    imagen_tratada=cv2.rectangle(imagen_tratada.copy(), (0,0), (CAM_LIM_LEFTH,480), (255,255,255),-1)
    imagen_tratada=cv2.rectangle(imagen_tratada.copy(), (0,CAM_LIM_BOTTOM),(720,480), (255,255,255),-1)
    imagen_tratada=cv2.rectangle(imagen_tratada.copy(), (0,0), (720,CAM_LIM_TOP), (255,255,255),-1)
    imagen_tratada=cv2.rectangle(imagen_tratada.copy(), (CAM_LIM_RIGHT,0), (720,480), (255,255,255),-1)
    #cv2.imshow('DETECCION IS - Imagen con contornos y centro de gravedad',imagen_tratada)

    #Apply green mask
    mask=imagen_tratada.copy()
    mask_Verde = cv2.inRange(mask.copy(),GREEN_LOW,GREEN_HIGH)
    
    #Apply red mask
    mask=imagen_tratada.copy()
    mask1 = cv2.inRange(mask.copy(), RED_LOW1, RED_HIGH1)
    mask2 = cv2.inRange(mask.copy(), RED_LOW2, RED_HIGH2)
    mask_Rojo = cv2.add(mask1, mask2)


    #Filtro canny
    #Mascara Roja
    mask_Rojo = cv2.Canny(mask_Rojo.copy(), UMBRAL_MIN, UMBRAL_MAX)
    #Mascara Roja
    mask_Verde = cv2.Canny(mask_Verde.copy(), UMBRAL_MIN, UMBRAL_MAX)
    #img2=mask_Rojo.copy()
    #cv2.imshow('DETECCION DE FIGURAS - Imagen con contornos y centro de gravedad',mask_Rojo)

    contornos=[]
    mask_color=mask_Rojo
    (contornos,_) = cv2.findContours(mask_Rojo.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    mask_color=mask_Verde
    (contornos2,_) = cv2.findContours(mask_color.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    ###RED###
    if len(contornos)>0:
        for c in contornos:
            nuevoContorno=c
            #nuevoContorno = cv2.convexHull(c)
            #rect = cv2.minAreaRect(nuevoContorno)
            #box = cv2.boxPoints(rect)
            #box = np.int0(box)
            #area = cv2.contourArea(box)
            area = cv2.contourArea(c)
            #print('rojo')
            #print(area)
            if area > CAM_AREA_MIN and area < CAM_AREA_MAX:
                deteccion+=1
                #print([globales.triangleAreaMin,gloables.triangleAreaMax])
                M = cv2.moments(nuevoContorno)
                if (M["m00"]==0): M["m00"]=1
                x = int(M["m10"]/M["m00"])
                y = int(M['m01']/M['m00'])
                img2=cv2.circle(img2.copy(), (x,y), 4, (0,0,255), -1)
                #font = cv2.FONT_HERSHEY_SIMPLEX
                pts=CalcularXYZ(x,y)
                #print(int(pts[0]),int(pts[1][0]))
                #img2=cv2.putText(img2.copy(), '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)
        
                #img2=cv2.drawContours(img2.copy(),[box],0,(0,0,255),2)
        if deteccion==1:
            deteccion=0
            red[0]=int(pts[0])
            red[1]=int(pts[1][0])
        elif deteccion>1:
            deteccion=0
            red[0]=0
            red[1]=0
        else:
            deteccion=0
            red[0]=0
            red[1]=0
    else:
        deteccion=0
        red[0]=0
        red[1]=0

   
    ###DETECCION VERDE###
    if len(contornos2)>0:
        for c in contornos2:
            nuevoContorno=c
            #nuevoContorno = cv2.convexHull(c)
            #rect = cv2.minAreaRect(nuevoContorno)
            #box = cv2.boxPoints(rect)
            #box = np.int0(box)
            #area = cv2.contourArea(box)
            area = cv2.contourArea(c)
            if area > CAM_AREA_MIN and area < CAM_AREA_MAX:
                deteccion+=1
                M = cv2.moments(nuevoContorno)
                if (M["m00"]==0): M["m00"]=1
                x = int(M["m10"]/M["m00"])
                y = int(M['m01']/M['m00'])
                img2=cv2.circle(img2.copy(), (x,y), 4, (0,255,0), -1)
                #font = cv2.FONT_HERSHEY_SIMPLEX
                pts=CalcularXYZ(x,y)
                #print(int(pts[0]),int(pts[1][0]))
                #img2=cv2.putText(img2.copy(), '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)
                #img2-cv2.drawContours(img2.copy(),[box],0,(0,0,255),2)
        if deteccion==1:
            deteccion=0
            green[0]=int(pts[0])
            green[1]=int(pts[1][0])
        elif deteccion>1:
            deteccion=0
            green[0]=0
            green[1]=0
        else:
            deteccion=0
            green[0]=0
            green[1]=0
    else:
        deteccion=0
        green[0]=0
        green[1]=0
    
    return img2,red,green

def CalcularXYZ(u,v):#, s):
    # Generamos el vector m
    uv = np.array([[u,v,1]], dtype=np.float).T
    # Obtenemos R a partir de rvec
    R, _ = cv2.Rodrigues(R_VEC)
    Inv_R = np.linalg.inv(R)
    # Parte izquierda m*A^(-1)*R^(-1)
    Izda = Inv_R.dot(np.linalg.inv(MTX).dot(uv))
    # Parte derecha
    Drch = Inv_R.dot(T_VEC)
    # Calculamos S porque sabemos Z = 0
    s = 0 + Drch[2][0]/Izda[2][0]
    XYZ = Inv_R.dot( s * np.linalg.inv(MTX).dot(uv) - T_VEC)
    aux_x=XYZ[0]
    #XYZ[0]=aux_x+(-107.5+0.3075*aux_x-0.0002876*aux_x*aux_x+aux_x*aux_x*aux_x*0.0000000834)
    return XYZ



#####################################################################







def detec_cam():
    try:
        videos=[]
        args = 'ls /dev/video*'
        a1=subprocess.run(args,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        msgs=a1.stdout.decode('utf-8')
        if a1.returncode==0:
            #print('returncode:', a1.returncode)
            aux=0
            for c in range(len(msgs)):
                if msgs[c].isspace():
                    videos.append(msgs[aux:c])
                    aux=c+1
        else:
            videos.append("No hay cámaras disponibles")


        #print(videos)
    except Exception as e:
        videos.append('error de lectura:')
        videos.append(e)

    return videos