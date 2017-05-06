import math

problem = input('問題はナニ？-->')

if (problem == '累乗'):
    num = input('累乗を計算するネ。値は？--->')
    index = input('指数は？--->')
    ans = math.pow(int(num),int(index))
    print(str(ans))

elif (problem == '平方根'):
    root = input('平方根を求めるネ。値は？--->')
    ans = math.sqrt(int(root))
    print(str(ans))

elif (problem == '対数'):
    print('対数を求めるヨ')
    m = input('真数は？--->')
    a = input('底とする値は？--->')
    ans = math.log(int(m),int(a))
    print(str(ans))

elif (problem == '角度をラジアンに変換'):
    degree = input('角度を変換するヨ。角度は何度？--->')
    ans = math.radians(int(degree))
    print(str(ans))

elif (problem == 'ラジアンを角度に変換'):
    radian = input('ラジアンを角度に変換するネ。ラジアンは？-->')
    ans = math.degrees(float(radian))
    print(str(ans))

elif (problem == '三平方の定理'):
    print('直角三角形の斜辺の長さを求めるヨ')
    x = input('１辺の長さは？--->')
    y = input('他の１辺の値は？--->')
    ans = math.hypot(int(x),int(y))
    print(str(ans))

elif (problem == '三角関数'):
    angle = input('sin,cos,tanを求めるネ。角度は？')
    sin = math.sin(math.radians(int(angle)))
    cos = math.cos(math.radians(int(angle)))
    tan = math.tan(math.radians(int(angle)))
    print('sin' + angle + ' = ' + str(sin))
    print('cos' + angle + ' = ' + str(cos))
    print('tan' + angle + ' = ' + str(tan))

else :
    print('？')
