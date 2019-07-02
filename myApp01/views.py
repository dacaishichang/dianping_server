from django.shortcuts import render
from django.core import serializers
from django.shortcuts import HttpResponse
import json
from .models import Category,City,Prodouct,Shop,User,Address,Orders,Comment
from django.db import connection
from math import ceil
from .utils import get_around
import time
#类别category
def index_Category(request):

    L = []
    with connection.cursor() as cursor:
        cursor.execute('select category_id,count(category_id) number from  prodouct group by category_id order by category_id')
        row = cursor.fetchall()
        for i in row:
            if i[0] == None:
                continue
            L.append({"categoryId":i[0],"categoryNumber":i[1]})
    resp = {
        'state': 1,
        'page': 0,
        'size': 0,
        'count': 0,
    }
    resp['datas'] = L
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
    return response

#列出城市列表cities
def index_City(request):
    resp = {
        'state': 1,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas':None,
        'msg':None
    }
    if request.method == 'GET':
        cities = City.objects.all()
        L = []
        for p in cities:
            p.__dict__.pop("_state")  # 需要除去，否则不能json化
            L.append(p.__dict__)  # 注意，实际是个json拼接的过程，不能直接添加对象

        resp['datas'] = L
        resp['msg'] = "搜索成功"
    else:
        resp['msg']="未能搜索城市"
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
    return response
#列出商品列表，最难

sql_str="prodouct.prodouct_id, prodouct.category_id, prodouct.shop_id, prodouct.sub_category_id, prodouct.city_id,"\
            +"prodouct.prodouct_title,prodouct.prodouct_image, prodouct.prodouct_start_time, prodouct.prodouct_sort_title, prodouct.prodouct_is_over_time ,prodouct.prodouct_value,"\
            +" prodouct.prodouct_price, prodouct.prodouct_ribat, prodouct.prodouct_bought, prodouct.prodouct_minquota, prodouct.prodouct_maxquota,"\
            +" prodouct.prodouct_post, prodouct.prodouct_soldout, prodouct.prodouct_tip, prodouct.prodouct_end_time, "\
            +"prodouct.prodouct_detail, prodouct.prodouct_is_refund," \
            +"shop.shop_id, " \
            +"shop.shop_name, shop.shop_tel, shop.shop_address,"\
            +" shop.shop_area, shop.shop_open_time, shop.shop_lon,"\
            +" shop.shop_lat"

strs_goods=["id","categoryId","shopId","sub_category_id","CityId",
            "title","imgUrl","startTime","sortTitle","isOverTime","value",
            "price","ribat","bought","minQuota","maxQuota",
            "post","soldOut","tip","endTime","detail","isRefund"]#22

strs_shops=["id","name","tel","address","area","opentime","lon","lat"]#不要traffic

# prodouct.prodouct_is_over_time
def index_Goods(request):

    page=int(request.GET.get('page'))
    size=int(request.GET.get('size'))
    try:
        category=int(request.GET.get('category'))
    except :
        category=1
    sql_execute = "select " + sql_str + " from prodouct,shop where prodouct.shop_id=shop.shop_id "
    if category != None and category != 1:
        sql_execute+="and prodouct.category_id="+str(category)
    sql_execute+=" limit " + str(page * size) + "," + str(size)

    print(sql_execute)
    cursor=connection.cursor()
    cursor.execute(sql_execute)
    row = cursor.fetchall()
    resp = {
        'state': 1,
        'page': 0,
        'size': 0,
        'count': 0,
        'msg':None
    }
    L=[]
    #名字--值
    if len(row)>0:
        for i in row:#每条信息
            temp={}
            count=0
            for j in strs_goods:
                temp[j]=i[count]
                count+=1
            temp_2={}
            for j in strs_shops:
                temp_2[j]=i[count]
                count += 1
            temp["shop"]=temp_2
            L.append(temp)
        # print(L)
        cursor.execute("select count(*) from prodouct where 1=1")
        row = cursor.fetchall()
        # print(row)
        count=row[0][0]
        #开始针对查询
        resp["datas"]=L
        resp["page"] = page
        resp["size"] = size
        resp["count"] = int(ceil(count/size))
        resp['msg'] = "查询成功"
    else:
        resp["datas"] = L
        resp['state'] = 0
        resp['msg'] = "查询失败"

    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
    return response

#Search返回对应的周围范围内的场所

#显示附近信息
def index_Nearby(request):
    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))

    raidus = float(request.GET.get('raidus'))
    minLat, minLng, maxLat, maxLng = get_around(lat,lon,raidus)
    sql_near="select " + sql_str + " from prodouct,shop where prodouct.shop_id=shop.shop_id "

    sql_near += " and  shop.shop_lon>" + str(minLng) +" and shop.shop_lon<" + str(maxLng) +" and shop.shop_lat>" + str(minLat) +" and shop.shop_lat<" + str(maxLat)

    sql_near += " limit 1,50"
    print(sql_near)
    cursor = connection.cursor()
    cursor.execute(sql_near)
    row = cursor.fetchall()

    resp = {
        'state': 1,
        'page': 0,
        'size': 0,
        'count': 0,
    }
    L = []
    # 名字--值
    for i in row:  # 每条信息
        temp = {}
        count = 0
        for j in strs_goods:
            temp[j] = i[count]
            count += 1
        temp_2 = {}
        for j in strs_shops:
            temp_2[j] = i[count]
            count += 1
        temp["shop"] = temp_2
        L.append(temp)
    if(len(L)>0):
        resp["datas"] = L
    else:
        resp["datas"] = None
        resp['state']=0
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
    return response

#登录或者注册
def index_login_Or_register(request):
    response = None
    flag = request.GET.get('flag')
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    if flag == "login":#登陆
        print("登陆")
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username != None and username != "" and password != None and password != "":
            users = User.objects.filter(name=username).filter(loginPwd=password)
            print(len(users))

            for p in users:
                p.__dict__.pop("_state")
                resp['datas']=p.__dict__
                resp['msg']="登陆成功"
                resp['state']=1
                break

        else:#用户名和密码为空
            resp['msg'] = "用户名或者密码不能为空"

        response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
        return  response
    if flag == "register":  # 登陆
        username = request.GET.get('username')
        password = request.GET.get('password')
        users = User.objects.filter(name=username)
        if len(users)==0:

            User.objects.create(name=username,loginPwd = password,payPwd="111111")#默认支付密码111111
            users = User.objects.filter(name=username).filter(loginPwd=password)
            if len(users)>0:
                for p in users:
                    p.__dict__.pop("_state")
                    resp['state']=1
                    resp['datas'] = p.__dict__
                    resp['msg'] = "注册成功"
                    break
            else:
                resp['msg'] = "注册失败"
        else:
            resp['msg'] = "注册失败"
        response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
        return response

#返回的数据有address
'''
userName
addressName
tel
province
'''
#显示个人信息
def index_showInfo(request):
    username=request.GET.get("username")
    print(username)
    users=User.objects.filter(name=username)#字典

    uid=0
    response = None
    resp = {
        'state': 1,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }

    if len(users)>0:#用户不为空
        p_temp=None#创建实例

        for p in users:
            uid=p.__dict__["id"]
            p_temp=p
            # print(uid)
            break
        adds=Address.objects.filter(userid=uid)

        if len(adds)<1:#地址信息为空,创建一个为空的
            Address.objects.create(userid=p_temp)#实例召唤
            adds = Address.objects.filter(userid=uid)
        for p in adds:
            p.__dict__.pop("_state")
            p_1 = p.__dict__
            p_1['userName'] = username
            resp['datas'] = p_1
            break
        resp['msg'] = "信息获取成功"
    else:
        resp['datas']=None
        resp['msg'] = "获取信息失败"
        resp['state'] = 0
    print(resp)
    response = HttpResponse(content=json.dumps(resp) , content_type='application/json;charset = utf-8')
    return response

#修改信息或者密码
def change_Info_or_pwd(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    if request.GET.get("flag")=="info":#修改信息

        username=request.GET.get("username")
        province=request.GET.get("province")
        tel=request.GET.get("tel")
        address=request.GET.get("address")

        users = User.objects.filter(name=username)
        uid=0
        if len(users)>0:
            for p in users:
                uid = int(p.__dict__["id"])
                # print(uid)
                break
            isOk=Address.objects.filter(userid=uid).update(tel=tel,addressName=address,province=province)
            # print(isOk)
            if isOk==1:
                adds = Address.objects.filter(userid=uid)
                # print(len(adds))
                for p in adds:
                    p.__dict__.pop("_state")
                    p_1 = p.__dict__
                    p_1['userName'] = username
                    print(username)
                    resp['datas'] = p_1
                    resp['msg'] = "修改信息成功"
                    break
            else:
                resp['msg'] = "修改不成功"
            resp['state'] = 1
        else:
            resp['state'] = 0
            resp['datas'] = None
            resp['msg']="没有用户信息可以更改"
    else:#修改密码
        username=request.GET.get("username")
        oldpwd = request.GET.get("oldpwd")
        newPwd = request.GET.get("newPwd")
        user = User.objects.get(name=username)
        if user.loginPwd==oldpwd:
            isOk = User.objects.filter(name=username).update(loginPwd=newPwd)
            if isOk==1:
                user = User.objects.get(name=username)
                user.__dict__.pop("_state")
                resp['datas'] = user.__dict__
                resp['msg'] = "修改成功"
                resp['state'] = 1
                print("成功")
        else:
            resp['state'] = 0
            print("失败")
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
    return response

#购买功能
def index_buy(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }

    username = request.GET.get("username")
    payPwd = request.GET.get("payPwd")
    goodsId = int(request.GET.get("goodsId"))
    price= request.GET.get("price")
    users = User.objects.filter(name=username).filter(payPwd=payPwd)
    p_temp = None
    if len(users)>0:

        for p in users:
            p_temp=p
            break
        Orders.objects.create(user=p_temp,orders_prodouct_id=goodsId,orders_prodouct_count=1,orders_all_price=price,
                              orders_paystate=0,orders_time=str(int(time.time()*1000)))
        resp['state']=1
        resp['msg']="购买成功"

    else:
        resp['state'] = 0
        resp['msg'] = "购买失败"
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
    return response

#显示所有评论
def show_comments(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    userId = request.GET.get("userId")
    user = User.objects.get(id=userId)

    L = []
    if user != None:

        # for p in users:
        #     p_temp=p

        #     break
        p_temp=None
        comments = Comment.objects.filter(user=user).order_by('-comment_time')
        for p in comments:
            # p.__dict__.pop("_state")
            p_temp=p.__dict__
            goodsName =Prodouct.objects.get(id=p.prodouct.id).sortTitle.__str__()
            p_temp['product_name'] = goodsName
            p_temp.pop("_state")
            p_temp.pop('_prodouct_cache')

            L.append(p_temp)

        resp['state'] = 1
        resp['size'] = len(comments)
        resp['msg'] = "返回了所有的数据"
    else:
        resp['state'] = 0
        resp['msg'] = "没有查询到相应数据"

    resp['datas'] = L
    print(resp['datas'])
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')

    return response


#显示所有订单数据
def show_orders(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    userId = request.GET.get("userId")
    user = User.objects.get(id=userId)
    p_temp=None
    temp_1=None
    L = []
    if user!=None:

        # for p in users:
        #     p_temp=p
        #     break
        orders = Orders.objects.filter(user=user).order_by('-orders_time')
        for p in orders:
            p.__dict__.pop("_state")
            goods=Prodouct.objects.get(id=str(p.__dict__["orders_prodouct_id"]))
            temp_1=p.__dict__
            temp_1['goods_name']=goods.sortTitle
            L.append(temp_1)

        resp['state']=1
        resp['size'] = len(orders)

        resp['msg']="返回了所有的数据"
    else:
        resp['state'] = 0
        resp['msg'] = "没有查询到相应数据"

    resp['datas'] = L
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')

    return response

#订单数额统计
def orders_count(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    username = request.GET.get("username")
    user = User.objects.get(name=username)
    if user != None:
        cursor = connection.cursor()
        cursor.execute("select COUNT(*) from orders where user_id=" + str(user.id))
        row = cursor.fetchall()
        # if len(row) > 0:
        resp['datas']=str(row[0][0])
        resp['msg'] = "返回成功"
        resp['state'] = 1
    else:
        resp['datas'] = '0'
        resp['msg'] = "没有用户数据"
        resp['state'] = 0
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')

    return response

#消费总额统计
def wallet_count(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    username = request.GET.get("username")
    user = User.objects.get(name=username)
    if user!=None:

        cursor=connection.cursor()
        cursor.execute("select orders_all_price from orders where user_id="+str(user.id))
        row = cursor.fetchall()
        sum = 0
        if len(row)>0:
            for i in row:
                sum+=float(i[0])
            print(sum)
        resp['datas']=str(sum)
        resp['msg']="成功返回数据"
        resp['state']=1
    else:
        resp['datas'] = '0'
        resp['msg'] = "没有用户数据"
        resp['state'] =0
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')

    return response

# 评论总数
def reciew_count(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    username = request.GET.get("username")
    user = User.objects.get(name=username)
    if user != None:
        cursor = connection.cursor()
        cursor.execute("select COUNT(*) from comment where user_id=" + str(user.id))
        row = cursor.fetchall()
        # if len(row)>0:
        resp['datas'] = str(row[0][0])
        resp['msg'] = "返回成功"
        resp['state'] = 1
    else:
        resp['datas'] = '0'
        resp['msg'] = "没有用户数据"
        resp['state'] = 0
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')

    return response

# 评论功能提交处理
def commentPut(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    username = request.GET.get('username')
    product_id = request.GET.get('goodId')
    comment = request.GET.get('comment')
    #User和Product需要创建

    commentObj = None
    user = User.objects.get(name=username)
    product = Prodouct.objects.get(id=product_id)
    if user!=None and product!=None:
        commentObj=Comment.objects.create(user=user,prodouct=product,comment_conent=comment,comment_time=str(int(time.time()*1000)))
        # commentObj.save()
        resp['state']=1
    else:
        print("没有对象")
        resp['state']=0
    resp['datas']=""
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
    return response

# 评论功能获取处理
def commentGet(request):
    resp = {
        'state': 0,
        'page': 0,
        'size': 0,
        'count': 0,
        'datas': None,
        'msg': None
    }
    productId = int(request.GET.get('productId'))
    #User和Product需要创建
    product = Prodouct.objects.get(id=productId)

    comments = Comment.objects.filter(prodouct=product).order_by('-comment_id')
    if len(comments)>0:
        for p in comments:
            resp['datas']=p.comment_conent
            break
        resp['state']=1
        resp['msg']="返回成功"
    else:
        # print("没有数据")
        resp['state']=0
        resp['msg'] = "没有评论"
        resp['datas']=""
    response = HttpResponse(content=json.dumps(resp), content_type='application/json;charset = utf-8')
    return response



