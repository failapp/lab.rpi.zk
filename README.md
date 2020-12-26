# rpi.zk
integracion dispositivos zkteco ..

### comandos gestion entorno virtual python.. :

```

// instalar entorno virtual (python 3.6, linux opensuse 15.1) ..
$ pip3 install virtualenv

$ mkdir app
$ cd app 
$ virtualenv venv

// activar entorno virtual python ..
$ source venv/bin/active

// generar archivo con dependencias:
$ pip freeze > requirements.txt 

// desactivar entorno virtual python ..
$ deactivate

```

// obtener template facial de usuario ..
```
#define CMD_USERFACE_RRQ	 150	 // read request
#define CMD_USERFACE_WRQ	 151	 // write request
#define CMD_APPEND_USERFACE  153     // ..
#define CMD_DELETE_USERFACE	 152     // ..
//php ..
define('CMD_USERFACE_RRQ', 16);
define('CMD_USERFACE_WRQ', 17);
```
