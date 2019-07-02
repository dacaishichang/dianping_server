
from math import pi,cos

def get_around(lat,lon,raidus):
    # // 地球的周长是24901公里
    # // 英里和米的换算
    # 单位： 1609米
    # // 维度···································

    # 技算地球一周每一度占多少米
    degree = (24901 * 1609) / 360.0
    # 计算维度上变化一米多少度
    dpmLat = 1 / degree
    # 计算搜索半径在维度的度数
    raidusLat = dpmLat * raidus
    minLat = lat - raidusLat
    maxLat = lat + raidusLat

    # // 经度···································
    # // 我们定位的地点的小圈上的距离变化
    mpdLng = degree * cos(lat * (pi / 180))
    dpmLng = 1 / mpdLng
    raidusLng = dpmLng * raidus
    minLng = lon - raidusLng
    maxLng = lon + raidusLng
    return minLat, minLng, maxLat, maxLng