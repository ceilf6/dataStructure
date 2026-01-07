from pyecharts import options as opts
from pyecharts.charts import Polar

# 数据
producers = [10, 80, 200, 120]
primary_consumers = [3, 20, 50, 30]
secondary_consumers = [1, 2, 5, 3]

# 创建极坐标图
polar = (
    Polar()
    .add_schema(
        angleaxis_opts=opts.AngleAxisOpts(min_=0, max_=255),
        radiusaxis_opts=opts.RadiusAxisOpts(
            type_='category',
            data=['Winter', 'Autumn', 'Summer', 'Spring'],
            z=10,
            axislabel_opts=opts.LabelOpts(is_show=True, margin=10, font_size=14, color='#333', interval=0)
        )
    )
    .add(
        series_name='Producers',
        data=producers,
        type_='bar',
        stack='a',
        itemstyle_opts=opts.ItemStyleOpts(color='#FFCA21'),
        emphasis_opts=opts.EmphasisOpts(focus='series')
    )
    .add(
        series_name='Primary consumers',
        data=primary_consumers,
        type_='bar',
        stack='a',
        itemstyle_opts=opts.ItemStyleOpts(color='#A2BE6A'),
        emphasis_opts=opts.EmphasisOpts(focus='series')
    )
    .add(
        series_name='Secondary consumers',
        data=secondary_consumers,
        type_='bar',
        stack='a',
        itemstyle_opts=opts.ItemStyleOpts(color='#62B5CC'),
        emphasis_opts=opts.EmphasisOpts(focus='series')
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            formatter="{b}: {c}"
        ),
        legend_opts=opts.LegendOpts(data=['Producers', 'Primary consumers', 'Secondary consumers'])
    )
)

# 渲染图表
polar.render("polar_chart.html")
