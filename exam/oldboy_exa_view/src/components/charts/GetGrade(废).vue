<template>
    <div id="main" style="width: 1260px;height:400px;"></div>
</template>

<script>
    export default {
        mounted() {
            this.initDate();
        },
        data() {
            return {
                contributeDate: [],
                blogContributeCount: [],
            }
        },
        created() {

        },
        methods: {
            getVirtulData(year) {
                year = year || '2021';
                var date = +echarts.number.parseDate(year + '-01-01');
                var end = +echarts.number.parseDate((+year + 1) + '-01-01');
                var dayTime = 3600 * 24 * 1000;
                var data = [];
                for (var time = date; time < end; time += dayTime) {
                    data.push([
                        echarts.format.formatTime('yyyy-MM-dd', time),
                        Math.floor(Math.random() * 10000)
                    ]);
                }
                return data;
            },
            initDate() {
                var myChart = this.$echarts.init(document.getElementById('container'))
                var option = {

                    //设置背景
                    // backgroundColor: '#d0d0d0',

                    title: {
                        top: 30,
                        text: '个人签到',
                        subtext: '一年内签到的展示图表',
                        left: 'center',
                        textStyle: {
                            color: '#000'
                        }
                    },
                    tooltip: {
                        padding: 10,
                        backgroundColor: '#555',
                        borderColor: '#777',
                        borderWidth: 1,
                    },
                    legend: {
                        top: '30',
                        left: '100',
                        data: ['文章数', 'Top 12'],
                        textStyle: {
                            // 设置字体颜色
                            color: '#000'
                        }
                    },
                    visualMap: {
                        show: true,
                        showLabel: true,
                        categories: ['签到', '迟到', '缺课'],
                        calculable: true,
                        inRange: {
                            symbol: 'rect',
                            color: ['#86b1f1', '#ef7370', '#eaf8f5']
                        },
                        itemWidth: 12,
                        itemHeight: 12,
                        orient: 'horizontal',
                        left: 'center',
                        bottom: 0
                    },
                    calendar: [{
                        top: 100,
                        left: 'center',
                        range: ['2020-12-25', '2021-12-25'],
                        splitLine: {
                            show: true,
                            lineStyle: {
                                // 设置月份分割线的颜色
                                color: '#D3D3D3',
                                width: 4,
                                type: 'solid'
                            }
                        },
                        yearLabel: {show: false},
                        dayLabel: {
                            show: true,
                            formatter: '{start}  1st',
                            fontWeight: 'lighter',
                            nameMap: ['日', ' ', ' ', '三', ' ', ' ', '六',],
                            fontSize: 12
                        },
                        monthLabel: {
                            nameMap: 'cn', // 设置中文显示
                            textStyle: {
                                // 设置月显示颜色
                                color: '#000'
                            }
                        },
                    }],
                    series: {
                        type: 'heatmap',
                        coordinateSystem: 'calendar',
                        data: this.getVirtulData(2021),
                        calendarIndex: 0,
                    }
                };
                myChart.setOption(option);
            }
        }
    }

</script>