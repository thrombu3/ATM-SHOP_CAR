<template>
    <div id="main" style="width: 1260px;height:400px;"></div>
</template>

<script>
    export default {
        name: "SourceNum",
        data() {
            return {
                data: {},
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),
            }
        },
        methods: {
            initialize() {
                this.$axios.get(this.$settings.base_url + `teachers/get_lately_source/?role_id=${this.role_id}`, {
                    headers: {'Authorization': `jwt ${this.token}`}
                }).then(response => {
                    if (response.data.status) {
                        this.$message('网站出错,请联系管理员@lw/@sc')
                    } else {
                        this.data = response.data
                        this.handleRender()
                    }
                });
            },

            // 渲染数据
            handleRender() {
                var chartDom = document.getElementById('main');
                var myChart = this.$echarts.init(chartDom);
                var option;

                option = {
                    title: {
                        text: '最近一次考试成绩区间人数统计',
                        subtext: '题库名字',
                        left: 'center'
                    },
                    tooltip: {
                        trigger: 'item'
                    },
                    // legend: {
                    //     orient: 'vertical',
                    //     left: 'left',
                    // },
                    series: [
                        {
                            name: '人数',
                            type: 'pie',
                            radius: '50%',
                            data: [
                                {value: this.data.a.count, name: this.data.a.name},
                                {value: this.data.b.count, name: this.data.b.name},
                                {value: this.data.c.count, name: this.data.c.name},
                                {value: this.data.d.count, name: this.data.d.name},
                                {value: this.data.e.count, name: this.data.e.name},
                                {value: this.data.f.count, name: this.data.f.name},
                            ],
                            emphasis: {
                                itemStyle: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                };

                option && myChart.setOption(option);
            },

        },
        mounted() {
            this.initialize()
        }
    }
</script>

<style scoped>

</style>