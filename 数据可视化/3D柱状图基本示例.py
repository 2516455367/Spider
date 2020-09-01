import math

from pyecharts import options as opts
from pyecharts.charts import Bar3D, Scatter3D, Map3D, Line3D
from pyecharts.faker import Faker
import random


def bar3d_base():
    data = [[i, j, random.randint(0, 20)] for i in Faker.clock for j in Faker.week]
    bar3d = Bar3D(init_opts=opts.InitOpts(width='1100px', height='600px'))
    bar3d.add(" ", data)
    bar3d.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=20),
        title_opts=opts.TitleOpts(title="Bar_3D-基本实例")
    )
    bar3d.render("./bar_3d_base.html")


bar3d_base()


def scatter3d_base():
    data = [
        [random.randint(0, 100),
         random.randint(0, 100),
         random.randint(0, 100)]
        for _ in range(80)
    ]
    scatter3d = Scatter3D(init_opts=opts.InitOpts(width="1440px", height="720px"))
    scatter3d.add(
        "",
        data,
        xaxis3d_opts=opts.Axis3DOpts(type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(type_="value")
    )
    scatter3d.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Scatter3D-基本示例")
    )
    scatter3d.render("./scatter3d_base.html")


scatter3d_base()


def line3d_base():
    data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        data.append([x, y, z])
    line3d = Line3D()
    line3d.add(
        "",
        data,
        xaxis3d_opts=opts.Axis3DOpts(type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(type_="value"),
        grid3d_opts=opts.Grid3DOpts(width=100, depth=100),
    )
    line3d.set_global_opts(
        title_opts=opts.TitleOpts(title="Line3D-基本示例"),
        visualmap_opts=opts.VisualMapOpts(max_=30)
    )
    line3d.render("./line3d_base.html")


line3d_base()
