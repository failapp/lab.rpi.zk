from zk import ZK, const
from zk.user import User
from app.config import Config
from app.shared.helpers import obj_to_json, obj_to_dict
from datetime import datetime
import json
import time

conf = Config()

def fetch_device_users():
    try:
        zk = ZK(conf.IP_ADDR_DEVICE, port=conf.TCP_PORT_DEVICE, timeout=5, password=0, force_udp=False, ommit_ping=False)
        conn = zk.connect()
        if conn:

            userList = conn.get_users()

            dataList = []
            for user in userList[0:2000]:
                privilege = 'User'
                if user.privilege == const.USER_ADMIN:
                    privilege = 'Admin'
                
                # u = { 'user_uid': user.uid, 'user_id': user.user_id, 'name': user.name, 'privilege': privilege }
                dataList.append(obj_to_dict(user))
            
            return dataList
        else:
            return None

    except Exception as e:
        print ("Process terminate : {}".format(e))
        return None
    

def fetch_device_user(userId):
    try:
        zk = ZK(conf.IP_ADDR_DEVICE, port=conf.TCP_PORT_DEVICE, timeout=5, password=0, force_udp=False, ommit_ping=False)
        conn = zk.connect()
        if conn:

            userList = conn.get_users()
            try:
                _user = list(filter(lambda u: u.user_id == userId, userList))[0]
                return obj_to_json(_user)

            except:
                return {}

        else:
            return None

    except Exception as e:
        print ("Process terminate : {}".format(e))
        return None
    


def store_device_user(payload):
    try:
        zk = ZK(conf.IP_ADDR_DEVICE, port=conf.TCP_PORT_DEVICE, timeout=5, password=0, force_udp=False, ommit_ping=False)
        conn = zk.connect()
        if conn:

            try: 

                user_id = payload['user_id']
                uid = payload['uid']
                name = payload['name']
                privilege = payload['privilege']
                password = payload['password']
                group_id = payload['group_id']
                card = payload['card']

                user = User(uid, name, privilege, password, group_id, user_id, card)

                userList = conn.get_users()
                cnt = len(userList)
                print("userList count -> ", cnt)

                try:
                    if cnt > 0:
                        _user = list(filter(lambda u: u.user_id == user.user_id, userList))[0]
                        user.uid = _user.uid
                    else:
                        if user.uid == 0:
                            uid = 1
                            user.uid = uid

                except:
                    if user.uid == 0:
                        _user = max(userList, key= lambda u: u.uid)
                        uid = _user.uid + 1
                        user.uid = uid
                
                conn.set_user(uid=user.uid, name=user.name, privilege=user.privilege, password=user.password, group_id=user.group_id, user_id=user.user_id, card=user.card)
                
                print("synchronize user ok .. user.user_id -> " + str(user.user_id) + " - user.name -> " + user.name)

                #u = obj_to_json(user)
                return obj_to_dict(user)

            except:
                print("error store user device ..")
                return None

        else:
            return None
    
    except Exception as e:
        print ("Process terminate : {}".format(e))
        return None
    





def delete_device_user(payload):
    try:
        zk = ZK(conf.IP_ADDR_DEVICE, port=conf.TCP_PORT_DEVICE, timeout=5, password=0, force_udp=False, ommit_ping=False)
        conn = zk.connect()
        if conn:

            try: 

                user_id = payload['user_id']
                uid = payload['uid']

                userList = conn.get_users()
                cnt = len(userList)

                try:
                    if cnt > 0:
                        _user = list(filter(lambda u: u.user_id == user_id, userList))[0]
                        conn.delete_user(user_id = _user.user_id)                
                        print("delete user ok -> " + str(_user.user_id))
                        return True
                    else:
                        return False

                except:
                    return False
            
            except:
                print("error delete user device ..")
                return None

        else:
            return None
    
    except Exception as e:
        print ("Process terminate : {}".format(e))
        return None
    